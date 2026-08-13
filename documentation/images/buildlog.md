## August 13, 2026 - Initial Tracking Data Logging

### Objective
Add data logging to the vision system so that tracking performance can be recorded and analyzed instead of relying only on the heads up display and terminal output.

### Work Completed
- Added Python's CSV module to the tracking program.
- Created a CSV output file for recording tracking data.
- Added a frame counter and video timestamp measurement
- Recorded target detection status, target coordinates, X and Y tracking error, and contour area for every processed frame.
- Recorded frames where no valid target was detected instead of excluding them from the dataset.
- Made the dataset distinguish between frames where there was no detected contour and frames where a contour existed but failed to meet the minimum requirement for area.
- Added lines to .gitignore to prevent cluttering the repository with generated datasets or any cache from my test runs.

### What I Learned
I learned how Python can create and write data to CSV files using the `csv` module.

I also learned why data should be recorded for unsuccessful detections. Excluding these frames would hide periods where the tracking system failed to identify a valid target.

I initially placed the frame counter and timestamp calculations outside of the loop which caused all recorded rows to have the same values. I fixed that by moving these calculations inside the loop.

### Testing / Results
The first test produced 540 logged frames over approximately 18.6 seconds.

310 frames contained a valid target detection and 230 frames recorded the target as lost.

The 6000 square pixel minimum contour-area threshold behaved as expected, contours below the threshold were rejected, and those above were accepted.

### Current Limitations
The recorded X/Y tracking error represents the target's displacement from the center of the stationary camera frame. It does not actually measure the accuracy of the computer-vision detection itself.

The current dataset was collected using prerecorded footage and a stationary camera.


### Next Step
Create a Python data analysis program capable of reading the recorded CSV data and begin visualizing the tracking system's behavior over time.