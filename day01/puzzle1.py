import sys

last_measurement = sys.maxsize
num_increments = 0
with open('data.txt', 'r') as data_file:
    for line in data_file:
        measurement = int(line)
        if measurement > last_measurement:
            num_increments += 1
        last_measurement = measurement

print("There are %d increments" % num_increments)
