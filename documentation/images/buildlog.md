## August 12, 2026 - Target Validation and Directional Tracking

### Objective
Improve the target detection system so that my system can determine whether a detected region is a valid target, handle situations where the target is lost / out of the frame, and determine which direction the target is located relative to the center of the camera frame.

### Work Completed
- Added target-loss handling so that the program no longer assumes a target is present in every frame.
- Added contour-area measurement using OpenCV.
- Added a minimum contour area requirement of 6000 square pixels to help prevent small green areas in the frame from being falsely identified as the desired target.
- Added 20-pixel deadband around the center of the video frame.
- Used horizontal and vertical tracking error to determine whether the target is left, right, up, down, or sufficiently centered.
- Tested the program with footage where the target enters and leaves the camera frame.
- Reorganized the program so that target coordinates along with tracking errors are only calculated when there is a valid target.

### What I Learned
I learned that detecting a contour does not necessarily mean that the intended target has been identified. To reduce any potential occurences of this problem, I measured the area of the largest detected contour and required it to have an area greater than 6000 square pixels before the program would accept it as a valid target.

I also learned more about conditional program flow. At one point, the program attempted to use the variables `x`, `y`, `w`, and `h` even when the detected contour did not meet the minimum-area requirement. Because those variables had not been created yet in that situation, the program crashed. I fixed this by making the calculations that depend on these variables occur only after a target has been validated.

### Testing / Results
The program was tested using prerecorded footage containing periods where the green target was visible and periods where it was completely out of the frame.

The prorgam successfully:
- Detected the green target when visible
- Rejects detected contours below the minimum area requirement
- Reports when the target has been lost.
- Resumes tracking when the target reappears.
- Calculates horizontal and vertical tracking error.
- Determines whether the target is left, right, above, below, or centered within the deadband.

### Current Limitations
The system still assumes that the largest sufficiently large green region is the intended target. A different green object in the camera frame that satisfies the HSV and minimum-area requirements could therefore be incorrectly tracked.

The current system also uses a fixed HSV range, minimum contour area, and deadband. These values would likely need to be adjusted for different targets, lighting conditions, tracking requirements, or any case that is not covered by the current configuration.

### Next Step
Improve the visual output of the tracking program by displaying useful tracking information directly on the video.

After organization and improvements are finished with the prototype, begin preparing for integration with a physical pan-and-tilt camera system.