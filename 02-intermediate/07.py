# Write a Python program that calculates the distance between two 3D points.

# The points are represented by two lists with three elements.

# The first element is the x-coordinate.

# The second element is the y-coordinate.

# The third element is the z-coordinate.


example_list = [
    {"point_a": [1, 2, 3], "point_b": [1, 2, 3]},       # 0.0
    {"point_a": [3, 4, 5], "point_b": [1, 3, 5]},       # 2.2361
    {"point_a": [-3, 4, -5], "point_b": [2, 0, -4]},    # 6.4807
    {"point_a": [1, 2, -3], "point_b": [12, -32, 3]},   # 36.2353
    {"point_a": [15, -32, -23], "point_b": [0, 42, 33]} # 94.0053
]


def find_distance(point_a, point_b):
    x_a = point_a[0]
    y_a = point_a[1]
    z_a = point_a[2]
    x_b = point_b[0]
    y_b = point_b[1]
    z_b = point_b[2]

    distance = ((x_a-x_b)**2 + (y_a-y_b)**2 + (z_a-z_b)**2)**0.5

    print(round(distance, 4))


for example in example_list:
    find_distance(example["point_a"], example["point_b"])

