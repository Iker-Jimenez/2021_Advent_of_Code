import time
from collections import Counter
start_time = time.time()

with open('data.txt', 'r') as data_file:
    polymer_template = data_file.readline().strip()
    insertion_rules = dict()
    # Skip empty line
    data_file.readline()
    for line in data_file:
        element_pair, inserted_element = line.strip().split(' -> ')
        insertion_rules[element_pair] = inserted_element

    print(insertion_rules)

    print(polymer_template)
    current_polymer = polymer_template
    for step in range(1, 41):
        print('Step {:d}'.format(step))
        new_polymer = current_polymer[0]
        for idx in range(1, len(current_polymer)):
            pair = current_polymer[idx - 1: idx + 1]
            if pair in insertion_rules:
                new_polymer += insertion_rules[pair] + pair[1]
            else:
                new_polymer += pair
        current_polymer = new_polymer
        print('Current polymer has length {:d} and value {:s} '.format(len(current_polymer), current_polymer))

    counter = Counter(new_polymer)
    most_common = counter.most_common(1)[0]
    least_common = counter.most_common()[-1]
    print(most_common)
    print(least_common)
    print('Result is {:d} - {:d} = {:d}'.format(most_common[1], least_common[1], most_common[1] - least_common[1]))

print("--- %s seconds ---" % (time.time() - start_time))
