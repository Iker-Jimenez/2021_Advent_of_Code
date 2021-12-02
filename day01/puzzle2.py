import sys

pos_0 = None
pos_1 = None
pos_2 = None
last_agg_measurement = sys.maxsize
num_increments = 0

with open('data.txt', 'r') as data_file:
    for line in data_file:
        measurement = int(line)
        pos_0 = pos_1
        pos_1 = pos_2
        pos_2 = measurement
        if pos_0 is not None and pos_1 is not None and pos_2 is not None:
            agg_measurement = pos_0 + pos_1 + pos_2
            if agg_measurement > last_agg_measurement:
                num_increments += 1
            last_agg_measurement = agg_measurement

print("There are %d increments" % num_increments)
