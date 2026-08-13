## August 13, 2026 - Vision Prototype V1 - On-Screen Telemetry

### Objective
Improve the visual output of the tracking program by displaying important tracking information on the video output rather than in the terminal. (for the most part)

### Work Completed
- Added marker to display the calculated center of the video frame.
- Added on-screen directional telemetry showing the target's horizontal and vertical position relative to the frame center.
- Added on-screen X and Y tracking error values.
- Added a large red "TARGET LOST" warning which pops up when no valid target is detected.
- Positioned the "TARGET LOST" warning so that it is horizontally centered relative to the video frame.
- Used `cv2.getTextSize()` to determine the dimensions of displayed text before calculating its position, which helped in centering the "TARGET LOST" text.
- Reorganized some variables for the target-loss text display to make their purpose clearer.
- Reduced some terminal output, there are still functions printing to terminal for debugging purposes though.

### What I learned
I learned how to use `cv2.putText()` to display information directly on an OpenCV video frame.

I also learned that the coordinates supplied to `cv2.putText()` do not represent the center of the text. To horizontally center the "TARGET LOST" warning, I first used `cv2.getTextSize()` to determine the width of the text and then calculated its starting X coordinate relative to the center of the frame.

I learned a bit more about variable scope and program flow when the program initially began producing an error because `lost_text_x` and `lost_text_y` were only being created when a valid target was detected. These variables were needed when no valid target was detected, but they had not been created in that program path. I fixed this by calculating them before the target-detection logic so that they exist regardless of whether a target is detected.

I also began to become more conscious of what I name my variables, because I want to make sure that called variables are easily identifiable when it comes to where they are supposed to link to.

### Testing / Results
The program successfully displays:

- The detected target's bounding box.
- The calculated center of the target.
- The center of the video frame.
- Horizontal and vertical tracking directions.
- Horizontal and vertical error in pixels.
- A centered "TARGET LOST" warning when a valid target cannot be detected.
- Correctly reports the target as centered when both tracking errors fall within the 20-pixel deadband.

The telemetry updates continuously as the target moves throughout prerecorded test footage.

The program continues running correctly when the target enters or leaves the frame.

### Current Limitations
The system still relies on color-based detection using a fixed HSV range.

The largest detected green contour that exceeds the minimum-area threshold is assumed to be the intended target.

The current minimum contour area and deadband are fixed values that may need to be adjusted for different use cases such as camera resolutions, targets, etc.

The system currently processes prerecorded video rather than a live camera feed.

Tracking decisions are currently software outputs only and do not yet control a physical two-axis pan-and-tilt mechanism.

### Next Step
Begin recording tracking data to a CSV file so that the performance of the vision system can be analyzed quantitatively.

Record information such as the time, frame number, target detection status, target coordinates, tracking error, and contour area. The purpose of recording this information is to assess the performance of the tracking system before integrating physical hardware.