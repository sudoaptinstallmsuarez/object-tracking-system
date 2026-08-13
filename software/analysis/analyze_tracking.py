import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("testing/data/tracking_data_01.csv")
print(data.head())

detected_data = data[data["target_detected"] == True]
print(detected_data.head())

horizontally_centered_data = detected_data[
    (detected_data["error_x"] >= -20) & (detected_data["error_x"] <= 20)
]

total_frames = len(data)
detected_frames = len(detected_data)
centered_frames = len(horizontally_centered_data)

detection_rate = (detected_frames / total_frames) * 100
horizontal_center_rate = (centered_frames / detected_frames) * 100
print(
    "Horizontal center rate:",
    round(horizontal_center_rate, 1), "%"
)

print("Total frames:", total_frames)
print("Detected frames:", detected_frames)
print("Detection rate:", round(detection_rate, 1), "%")
print("Horizontally centered frames:", centered_frames)

vertically_centered_data = detected_data[
    (detected_data["error_y"] >= -20) & (detected_data["error_y"] <= 20)
]
vertically_centered_frames = len(vertically_centered_data)
vertical_center_rate = (vertically_centered_frames / detected_frames) * 100

print("Vertical center rate:", round(vertical_center_rate, 1), "%")

fully_centered_data = detected_data[
    (detected_data["error_x"] >= -20) &
    (detected_data["error_x"] <= 20) &
    (detected_data["error_y"] >= -20) &
    (detected_data["error_y"] <= 20)
]

fully_centered_frames = len(fully_centered_data)
fully_centered_rate = (fully_centered_frames / detected_frames) * 100
print("Fully centered rate:", round(fully_centered_rate, 1), "%")

mean_absolute_x_error = detected_data["error_x"].abs().mean()
mean_absolute_y_error = detected_data["error_y"].abs().mean()

print("Mean Absolute X Error:", round(mean_absolute_x_error, 1), "pixels")
print("Mean Absolute Y Error:", round(mean_absolute_y_error, 1), "pixels")

maximum_absolute_x_error = detected_data["error_x"].abs().max()
maximum_absolute_y_error = detected_data["error_y"].abs().max()

print("Maximum Absolute X Error:", round(maximum_absolute_x_error, 1), "pixels")
print("Maximum Absolute Y Error:", round(maximum_absolute_y_error, 1), "pixels")

rms_x_error = np.sqrt((detected_data["error_x"] ** 2).mean())
rms_y_error = np.sqrt((detected_data["error_y"] ** 2).mean())

print("RMS X Error:", round(rms_x_error, 1), "pixels")
print("RMS Y Error:", round(rms_y_error, 1), "pixels")

plt.plot(
    data["time"],
    data["error_x"]
)

plt.axhline(
    y=0,
    linestyle="-",
    linewidth=2,
    label="Frame Center"
)
plt.axhline(
    y=20,
    linestyle="--",
    linewidth=1,
    label="Deadband"
)
plt.axhline(
    y=-20,
    linestyle="--",
    linewidth=1
)
plt.legend()

plt.xlabel("Time (seconds)")
plt.ylabel("X Error (pixels)")
plt.title("Horizontal Tracking Error vs. Time")
plt.savefig("results/v1_horizontal_tracking_error.png", dpi=300, bbox_inches="tight")
plt.show()
