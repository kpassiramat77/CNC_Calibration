
import tkinter as tk
from tkinter import ttk

class CNCDriveCalibration:
    """
    This class addresses challenges faced in calibrating CNC machines, especially those involving rack-and-pinion (R&P) systems. 
    The main problem solved by this code stems from Adam's difficulty in tuning his dual R&P system and ensuring accurate 
    calibration settings in software such as Avid CNC. The class helps calculate precise steps-per-unit values, adjust for 
    discrepancies between commanded and actual distances, and manage dual rack systems for synchronized motion.
    """
    def __init__(self, motor_steps_per_revolution, microstepping, pinion_teeth, pinion_diameter, gear_ratio=1):
        """Initialize the CNC Drive Calibration model."""
        self.motor_steps_per_revolution = motor_steps_per_revolution
        self.microstepping = microstepping
        self.pinion_teeth = pinion_teeth
        self.pinion_diameter = pinion_diameter
        self.gear_ratio = gear_ratio

    def calculate_steps_per_unit(self):
        """Calculate steps per unit for the CNC system.
        This calculation is crucial for ensuring accurate motion control in the CNC machine. It directly resolves Adam's issue
        where inaccurate travel distance readings occurred due to misaligned steps-per-unit settings. By computing this value
        based on physical system parameters like motor steps, microstepping, and pinion geometry, this method provides the
        foundation for precise machine operation and calibration.
        """
        # Calculate the pinion circumference
        pinion_circumference = 3.14159 * self.pinion_diameter

        # Calculate the travel distance per revolution
        travel_distance_per_revolution = pinion_circumference / self.gear_ratio

        # Steps per unit calculation
        steps_per_unit = (
            self.motor_steps_per_revolution * self.microstepping / travel_distance_per_revolution
        )
        return steps_per_unit

    def adjust_steps_per_unit(self, commanded_distance, actual_distance, current_steps_per_unit):
        """Adjust steps per unit based on calibration test results.
        This adjustment resolves discrepancies like the one Adam encountered, where the software overestimated 
        travel distances. By comparing commanded and actual distances, this function recalibrates the steps-per-unit 
        value to ensure precision and synchronization with the machine's actual motion.
        """
        return current_steps_per_unit * (commanded_distance / actual_distance)

    def calculate_travel_distance(self, steps_per_unit, steps_moved):
        """Calculate the travel distance based on steps moved and steps per unit."""
        return steps_moved / steps_per_unit

    def calculate_dual_rack_steps_per_unit(self, motor1_steps, motor2_steps):
        """Calculate the average steps per unit for a dual rack system."""
        return (motor1_steps + motor2_steps) / 2

    def fine_tune_backlash(self, current_backlash, adjustment_factor):
        """Fine-tune backlash compensation by applying an adjustment factor."""
        return current_backlash * adjustment_factor

# Function to display results in a panel
def display_results():
    """
    Display calibration results in a graphical user interface panel. 
    This GUI provides an intuitive and organized way for users to view calibration results, including critical values 
    like steps-per-unit, adjusted calibration metrics, and backlash tuning. It assists users in understanding and 
    interpreting the calibration data visually, making it easier to identify and resolve issues in CNC machine operation.
    """
    # Initialize CNC Calibration Model
    cnc = CNCDriveCalibration(
        motor_steps_per_revolution=200,  # Standard stepper motor
        microstepping=16,               # Microstepping driver setting
        pinion_teeth=15,                # Pinion teeth
        pinion_diameter=40,             # Pinion diameter in mm
        gear_ratio=1                    # No additional gearing
    )

    steps_per_unit = cnc.calculate_steps_per_unit()
    commanded_distance = 100  # Commanded distance in mm
    actual_distance = 98      # Measured actual distance in mm
    adjusted_steps_per_unit = cnc.adjust_steps_per_unit(
        commanded_distance, actual_distance, steps_per_unit
    )
    steps_moved = 3200  # Example number of steps moved
    travel_distance = cnc.calculate_travel_distance(adjusted_steps_per_unit, steps_moved)
    motor1_steps = 25.5
    motor2_steps = 24.5
    avg_steps_per_unit = cnc.calculate_dual_rack_steps_per_unit(motor1_steps, motor2_steps)
    current_backlash = 0.05
    adjustment_factor = 1.1
    tuned_backlash = cnc.fine_tune_backlash(current_backlash, adjustment_factor)

    # Display results in a GUI panel
    root = tk.Tk()
    root.title("CNC Calibration Results")

    frame = ttk.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text=f"Steps per unit: {steps_per_unit:.4f}").grid(column=0, row=0, sticky=tk.W)
    ttk.Label(frame, text=f"Adjusted steps per unit: {adjusted_steps_per_unit:.4f}").grid(column=0, row=1, sticky=tk.W)
    ttk.Label(frame, text=f"Travel distance: {travel_distance:.4f} mm").grid(column=0, row=2, sticky=tk.W)
    ttk.Label(frame, text=f"Average steps per unit for dual rack system: {avg_steps_per_unit:.4f}").grid(column=0, row=3, sticky=tk.W)
    ttk.Label(frame, text=f"Tuned backlash compensation: {tuned_backlash:.4f}").grid(column=0, row=4, sticky=tk.W)

    ttk.Button(frame, text="Close", command=root.destroy).grid(column=0, row=5, pady=10)

    root.mainloop()

# Run the application
if __name__ == "__main__":
    display_results()
