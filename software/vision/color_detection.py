import cv2
import numpy as np

video = cv2.VideoCapture("testing/videos/color_target_test_02.mov")

lower_green = np.array([35,50,30])
upper_green = np.array([85,255,255])
minimum_area = 6000
deadband = 20

while True:
    success, frame = video.read()
    if not success:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    height, width, channels = frame.shape
                
    center_x = width // 2
    center_y = height // 2

    # Calculate the position for the "TARGET LOST" text here:
    lost_text = "TARGET LOST"
    font = cv2.FONT_HERSHEY_SIMPLEX
    lost_font_scale = 2
    lost_thickness = 2
    (text_width, text_height), _ = cv2.getTextSize(lost_text, font, lost_font_scale, lost_thickness)
    lost_text_x = center_x - text_width // 2
    lost_text_y = center_y + 300 + text_height // 2

    cv2.circle(
        frame,
        (center_x, center_y),
        5,
        (0,0,255),
        -1
    )

    mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        contour_area = cv2.contourArea(largest_contour)
        print("Contour area:", contour_area)

        if contour_area > minimum_area:
            x, y, w, h = cv2.boundingRect(largest_contour)

            target_x = x + w // 2
            target_y = y + h // 2

            cv2.rectangle(
                frame,
                (x,y),
                (x+w,y+h),
                (0,0,255),
                2
            )

            cv2.circle(
                frame,
                (target_x, target_y),
                6,
                (255,0,0),
                -1
            )
            
            error_x = target_x - center_x
            error_y = target_y - center_y


            if error_x > deadband:
                horizontal_direction = "RIGHT"
            elif error_x < -deadband:
                horizontal_direction = "LEFT"
            else:
                horizontal_direction = "CENTERED"
            if error_y > deadband:
                vertical_direction = "DOWN"
            elif error_y < -deadband:
                vertical_direction = "UP"
            else:
                vertical_direction = "CENTERED"

            if horizontal_direction == "CENTERED" and vertical_direction == "CENTERED":
                direction = "CENTERED"
            else:
                direction = f"Horizontal: {horizontal_direction}, Vertical: {vertical_direction}"
            cv2.putText(
                frame,
                direction,
                (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
                )
            

            print("Error X:", error_x) # Leaving print statement for debug purposes, will remove later once it is not required.
            cv2.putText(
                frame,
                f"Error X: {error_x}",
                (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
            print("Error Y:", error_y) # Leaving this print statement for debug purposes, will remove later once it is not required.
            cv2.putText(
                frame,
                f"Error Y: {error_y}",
                (50, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
        else:
            cv2.putText(
                frame,
                lost_text,
                (lost_text_x, lost_text_y),
                font,
                lost_font_scale,
                (0, 0, 255),
                lost_thickness
            )
    else:
        cv2.putText(
            frame,
            lost_text,
            (lost_text_x, lost_text_y),
            font,
            lost_font_scale,
            (0, 0, 255),
            lost_thickness
        )

    cv2.imshow("Original", frame)
    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(25) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()