import time

import numpy as np

start_time = time.time()

with open('data.txt', 'r') as data_file:
    num_cols = len(data_file.readline().strip())
    num_rows = sum(1 for line in data_file) + 1

    height_map = np.empty((num_rows, num_cols), dtype=int)
    data_file.seek(0, 0)
    # Populate map
    for line_num, line in enumerate(data_file):
        for pos, height in enumerate(line.strip()):
            height_map[line_num][pos] = int(height)

print(height_map)

# Find all low_points
low_points = list()
for (row, column), height in np.ndenumerate(height_map):
    print('Processing row %d, column %d' % (row, column))
    # Check above
    if row > 0 and height_map[row - 1, column] <= height:
        continue  # Lower or equal height above
    # Check below
    if row < num_rows - 1 and height_map[row + 1, column] <= height:
        continue  # Lower or equal height below
    # Check left
    if column > 0 and height_map[row, column - 1] <= height:
        continue  # Lower or equal height left
    # Check right
    if column < num_cols - 1 and height_map[row, column + 1] <= height:
        continue  # Lower or equal height right
    print('Found a min of value %d' % height)
    low_points.append((row, column))

    print(low_points)


def calculate_basin_size(row, column, basin_members):
    # base case
    if height_map[row, column] == 9 or (row, column) in basin_members:
        return 0
    else:
        size = 1
        basin_members.add((row, column))
        # Check above
        if row > 0:
            size += calculate_basin_size(row - 1, column, basin_members)
        # Check below:
        if row < num_rows - 1:
            size += calculate_basin_size(row + 1, column, basin_members)
        # Check left
        if column > 0:
            size += calculate_basin_size(row, column - 1, basin_members)
        # Check right
        if column < num_cols - 1:
            size += calculate_basin_size(row, column + 1, basin_members)
        return size

basin_sizes = []
for row, column in low_points:
    basin_size = calculate_basin_size(row, column, set())
    print('Low point %d, %d basin size is %d' % (row, column, basin_size))
    basin_sizes.append(basin_size)

basin_sizes.sort(reverse=True)
print(basin_sizes)
print('Result %d' % (basin_sizes[0] * basin_sizes[1] * basin_sizes[2]))

print("--- %s seconds ---" % (time.time() - start_time))