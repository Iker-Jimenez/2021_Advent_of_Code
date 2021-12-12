import time
import copy
from collections import Counter
start_time = time.time()

with open('sample_data.txt', 'r') as data_file:
    paths = dict()
    for path in data_file:
        source, destination = path.strip().split('-')
        # Add straight paths, unless their destination is 'start or origin is 'end'
        if source != 'end' and destination != 'start':
            if source in paths:
                paths[source].add(destination)
            else:
                paths[source] = set([destination])
        # Add reverse paths, unless their destination is 'end' or origin is 'start'
        if destination != 'end' and source != 'start':
            if destination in paths:
                paths[destination].add(source)
            else:
                paths[destination] = set([source])
    print(paths)

    valid_paths = list()


    def follow_destination(destination, current_path):
        if destination == 'end':
            current_path.append(destination)
            valid_paths.append(current_path)
        elif destination.isupper() or destination not in current_path:
            current_path.append(destination)
            for next_destination in paths[destination]:
                follow_destination(next_destination, copy.deepcopy(current_path))
        else:
            # Just one small cave can be visited twice
            small_caves = Counter([cave for cave in current_path if cave.islower()])
            if 2 not in small_caves.values():
                current_path.append(destination)
                for next_destination in paths[destination]:
                    follow_destination(next_destination, copy.deepcopy(current_path))


    for destination in paths['start']:
        follow_destination(destination, ['start'])

    #print(valid_paths)
    print('There are %d valid paths' % len(valid_paths))

print("--- %s seconds ---" % (time.time() - start_time))