import time
import numpy as np
start_time = time.time()

with open('data.txt', 'r') as data_file:
    num_cols = len(data_file.readline().strip())
    num_rows = sum(1 for line in data_file) + 1

    octopus_map = np.empty((num_rows, num_cols), dtype=int)
    data_file.seek(0, 0)

    for line_num, line in enumerate(data_file):
        for pos, height in enumerate(line.strip()):
            octopus_map[line_num][pos] = int(height)
    print(octopus_map)

    def flash(row, column, flash_map, octopus_map):
        print('Flashing octopus at [%d, %d]' % (row, column))
        flash_map[row, column] = True
        # Process above line
        if row > 0:
            if column > 0:
                octopus_map[row - 1, column - 1] += 1
            octopus_map[row - 1, column] += 1
            if column < num_cols - 1:
                octopus_map[row - 1, column + 1] += 1
        # Process current line
        if column > 0:
            octopus_map[row, column - 1] += 1
        if column < num_cols - 1:
            octopus_map[row, column + 1] += 1
        # Process below line
        if row < num_rows - 1:
            if column > 0:
                octopus_map[row + 1, column - 1] += 1
            octopus_map[row + 1, column] += 1
            if column < num_cols - 1:
                octopus_map[row + 1, column + 1] += 1

    for step in range(1000):
        print('Processing step %d' % step)
        octopus_map += 1
        flash_map = np.zeros((num_rows, num_cols), dtype=bool)
        while len(octopus_map[np.logical_and(octopus_map > 9, ~ flash_map)]) > 0:
            flashable = np.argwhere(np.logical_and(octopus_map > 9, ~ flash_map))
            print('%d flashable \n %s' % (len(flashable), flashable))
            for octopus in flashable:
                if not flash_map[octopus[0], octopus[1]]:
                    flash(octopus[0], octopus[1], flash_map, octopus_map)

        octopus_map[octopus_map > 9] = 0
        print("After step %d" % step)
        print(octopus_map)
        print(flash_map)
        if np.all(flash_map):
            print("All flashed together at step %d" % (step + 1))
            break

print("--- %s seconds ---" % (time.time() - start_time))