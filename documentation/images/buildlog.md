## August 12, 2026 - Initial Target Detection

### Objective

Develop an initial detection system capable of location and tracking a colored target in prerecorded video footage.

### Work Completed

Created program `color_detection.py` that, when executed, tracks a moving green object in prerecorded footage and displays a bounding box around it and a dot that marks where the center of the object is.

### What I Learned

I learned a lot while making the color_detection program, notably:
- What a binary mask is and created one.
- How to convert BGR frames to HSV
- What contours are and used them to locate detected regions.
- How a bounding rectangle can be used to determine the center coordinates of a detected target.
- How the target's coordinates can be compared with the center of the videof rame to calculate horizontal and vertical tracking error.

### Current Result

- Successfully tracked the green target throughout the test footage.

### Limitations / Problems Identified

- The current algorithm assumes that the largest detected green region in the footage is the desired target. If there was another large green object in the footage, it might pick that up as the desired target, even if it is not.
- Target-loss handling has not been implemented yet, so tracking-error calculations assume a target has been detected. If the target was not present in the footage, the algorithm would not know that.

### Next Step

Implement target-loss handling so that the program can recognize when no valid target is detected and avoid calculating tracking error from invalid target coordinates.