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
    total_risk = 0
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
        total_risk += (height + 1)

    print('Total risk %d' % total_risk)

print("--- %s seconds ---" % (time.time() - start_time))