import time
import sys
import numpy as np
from collections import OrderedDict
start_time = time.time()

with open('data.txt', 'r') as data_file:
    crab_positions = np.array(data_file.readline().split(','), dtype=int)
    crabs = OrderedDict()
    for crab_position in crab_positions:
        if crab_position in crabs:
            crabs[crab_position] += 1
        else:
            crabs[crab_position] = 1

    min_cost = sys.maxsize
    best_mid_point = sys.maxsize
    for mid_point in range(max(crab_positions) + 1):
        print("Evaluating mid point %d" % mid_point)
        current_cost = 0
        for crab_pos in crabs.__reversed__():
            distance = abs(crab_pos - mid_point)
            cost_per_crab = sum(range(distance + 1))
            num_crabs = crabs[crab_pos]
            current_cost += (cost_per_crab * num_crabs)
            if current_cost > min_cost:
                break
        if current_cost < min_cost:
            print("Found a better cost %d at point %d" % (current_cost, mid_point))
            min_cost = current_cost
            best_mid_point = mid_point

    print("Min cost %d" % min_cost)
    print("Best mid point %d" % best_mid_point)

print("--- %s seconds ---" % (time.time() - start_time))