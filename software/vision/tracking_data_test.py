import csv

file = open(
    "testing/tracking_data_test.csv",
    "w",
    newline=""
)

writer = csv.writer(file)

writer.writerow([
    "frame",
    "time",
    "target_detected",
    "target_x",
    "target_y",
    "error_x",
    "error_y",
    "contour_area"
])

writer.writerow([
    1,
    0.0,
    True,
    500,
    300,
    -40,
    20,
    12000
])

file.close()