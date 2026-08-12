## August 12, 2026 - Initial Python and OpenCV Setup

### Objective

Set up the Python development environment and begin processing real video data with the use of OpenCV.

### Work Completed

- Installed Python and configured it for use with Visual Studio Code.
- Created virtual environment for the project.
- Created a `.gitignore` file to prevent unnecessary files from being uploaded to Github.
- Learned some basic Python concepts including:
    - Variables
    - Arithmetic operations
    - `if`, `elif`, and `else` statements
    -  Basic tracking error calculations
    - Deadbands
- Installed OpenCV and NumPy.
- Recorded test footage using a smart phone and loaded the video into OpenCV.
- Used OpenCV to read the video frame by frame.
- Determined the dimensions of each video frame.
- Calculated center coordinates of the video automatically.
- Added a visual marker to display the center of the frame.

### What I learned From This

I learned that video can be treated as a sequence of individual images, which are frames. OpenCV can retrieve each frame individually, allowing for calculations and image processing to be performed before displaying the frame.

I also learned how the position of a future tracking target can be represented using X and Y coordinates. The center of the camera image represents the desired target position. Tracking error can therefore be calculated by using the detected target coordinates and comparing those with the center coordinates.

The equation I created to find both the horizontal and vertical error is as follows:
`error = target_axisdirection - center_axisdirection`

In the project, the equations are:
`horizontal_error = target_x - center_x`
`vertical_error = target_y - center_y`

A positive or negative error indicates which direction the target is displaced from the center.

I also experimented with a deadband, which creates an acceptable range around the center where small tracking errors can be ignored. I decided to add a deadband in the hopes to prevent unnecessary motor movement or oscillation later on into the project.

### Current Result

The program can successfully:

1. Open pre-recorded test footage.
2. Read the footage frame by frame
3. Determine the resolution of the video.
4. Calculate the center of the frame.
5. Display a marker at the calculated center.

The system does not detect the target automatically yet.

### Problems Encountered

An if statement had incorrect indentation. This problem was nothing significant and was fixed quickly.

### Next Step

Implement basic computer vision to distinguish a colored target from its sorroundings, determine the target's X/Y coordinates, and compare those coordinates with the center of the frame.