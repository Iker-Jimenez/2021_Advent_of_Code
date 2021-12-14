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
    pairs = Counter()
    for idx in range(1, len(polymer_template)):
        pairs[polymer_template[idx - 1: idx + 1]] += 1
    print(pairs)

    for step in range(1, 41):
        print('Step {:d}'.format(step))
        new_pairs = Counter()
        for pair in pairs.keys():
            num_instances = pairs[pair]
            middle_value = insertion_rules[pair]
            new_pairs[pair[0] + middle_value] += num_instances
            new_pairs[middle_value + pair[1]] += num_instances
        print(new_pairs)
        pairs = new_pairs

    char_counter = Counter()
    for pair in pairs:
        num_instances = pairs[pair]
        char_counter[pair[0]] += num_instances

    # Last character is not counted in the loop above and is always the same in every iteration
    char_counter[polymer_template[-1]] += 1
    most_common = char_counter.most_common(1)[0]
    least_common = char_counter.most_common()[-1]
    print(most_common)
    print(least_common)
    print('Result is {:d} - {:d} = {:d}'.format(most_common[1], least_common[1], most_common[1] - least_common[1]))

print("--- %s seconds ---" % (time.time() - start_time))
