target_x = 490
target_y = 300

camera_center_x = 500
camera_center_y = 250

error_x = target_x - camera_center_x
error_y = target_y - camera_center_y

deadband = 20

print("Horizontal error:", error_x)
print("Vertical error:", error_y)

if error_x > deadband:
    print("Target is to the right of the camera center.")

elif error_x < -deadband:
    print("Target is to the left of the camera center.")

else:
    print("Target is centered")