# CNC_Calibration
This code provides a Python-based CNC calibration model that calculates and adjusts steps-per-unit, synchronizes dual rack systems, fine-tunes backlash, and visually displays the results in a user-friendly GUI.

**CNC Calibration Model Explanation**
**1. Problem Description:**
Adam faced several challenges with his dual rack-and-pinion CNC system, including:
- Inaccurate travel distances: Software overestimated motion due to incorrect steps-per-unit settings.
- Synchronization issues: Dual racks required alignment for coordinated motion.
- Backlash compensation: Mechanical play caused inaccuracies, needing precise tuning.
**2. Key Components:**
a. Calculate Steps Per Unit:
Formula:
Steps Per Unit = (Motor Steps Per Revolution × Microstepping) / Travel Distance Per Revolution

This calculation determines the number of steps needed for the CNC machine to move a single unit of distance. Accurate steps-per-unit are essential for proper motion control.
b. Adjust Steps Per Unit:
Formula:
Adjusted Steps Per Unit = Current Steps Per Unit × (Commanded Distance / Actual Distance)

This adjustment recalculates steps-per-unit to align the software's commands with the machine's actual motion.
c. Synchronize Dual Racks:
Formula:
Average Steps Per Unit = (Motor 1 Steps + Motor 2 Steps) / 2

Synchronizing dual racks ensures both racks move in harmony, preventing mechanical misalignments.
d. Fine-Tune Backlash:
Formula:
Tuned Backlash = Current Backlash × Adjustment Factor

Backlash tuning reduces errors caused by mechanical play, improving the accuracy of CNC operations.
**3. GUI (Graphical User Interface):**
Purpose:
- Provide a user-friendly interface for viewing calibration results.
- Display key metrics like steps-per-unit, adjusted calibration values, travel distance, and backlash tuning results.
**4. Assumptions:**
- Motor steps, microstepping, and pinion dimensions are accurate.
- Dual racks are mechanically aligned for synchronized motion.
- Backlash adjustment is feasible within the system’s tolerances.
**5. Workflow:**
1. Input Parameters: Provide motor, pinion, and motion details.
2. Calculate Steps Per Unit: Use motor specs and pinion geometry.
3. Adjust Calibration: Recompute based on commanded vs. actual distances.
4. Synchronize Racks: Average steps-per-unit for dual racks.
5. Display Results: Visual feedback for user understanding and precision tuning.
This explanation clarifies the logic and usability of the CNC Calibration Model, providing step-by-step insights into how it resolves challenges like inaccurate motion, synchronization issues, and backlash adjustments.
