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
                print("Target is right")
            elif error_x < -deadband:
                print("Target is left")
            else:
                print("Horizontally centered")
            if error_y > deadband:
                print("Target is down")
            elif error_y < -deadband:
                print("Target is up")
            else:
                print("Vertically centered")
            

            print("Error X:", error_x)
            print("Error Y:", error_y)
        else:
            print("Target Lost!")
    else:
        print("Target Lost!")

    cv2.imshow("Original", frame)
    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(25) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()