import time
import numpy as np
start_time = time.time()

with open('data.txt', 'r') as data_file:
    crab_positions = np.array(data_file.readline().split(','), dtype=int)
    print(crab_positions)
    mid_point = np.percentile(crab_positions, 50)
    print('Mid point is %d' % mid_point)
    total_fuel = 0
    for crab_position in crab_positions:
        total_fuel += abs(crab_position - mid_point)
    print("Total fuel: %d" % total_fuel)

print("--- %s seconds ---" % (time.time() - start_time))