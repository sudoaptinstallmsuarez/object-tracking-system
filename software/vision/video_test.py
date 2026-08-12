import cv2

video = cv2.VideoCapture("testing/videos/color_target_test_01.mov")

while True:
    success, frame = video.read()
    if not success:
        break
    height, width, channels = frame.shape
    center_x = width // 2
    center_y = height // 2

    print("Camera center:", center_x, center_y)

    cv2.circle(
        frame,
        (center_x, center_y),
        8,
        (0, 255, 0),
        -1
    )

    cv2.imshow("Object Tracking Test", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()