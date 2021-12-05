
with open('data.txt', 'r') as data_file:
    height = 1000
    width = 1000
    map = [[0] * height for x in range(width)]
    for line in data_file:
        origin, destination = line.strip().split('->')
        origin = tuple((int(x) for x in origin.split(',')))
        destination = tuple((int(x) for x in destination.split(',')))
        # Vertical lines
        if origin[0] == destination[0]:
            if origin[1] < destination[1]:
                start = origin[1]
                end = destination[1]
            else:
                start = destination[1]
                end = origin[1]
            for y in range(start, end + 1):
                map[y][origin[0]] += 1
        # Horizontal lines
        elif origin[1] == destination[1]:
            if origin[0] < destination[0]:
                start = origin[0]
                end = destination[0]
            else:
                start = destination[0]
                end = origin[0]
            for x in range(start, end + 1):
                map[origin[1]][x] += 1
        # Diagonal lines
        else:
            if origin[0] < destination[0]:
                # Going left to right
                x_seq = range(origin[0], destination[0] + 1)
            else:
                # Going right to left
                x_seq = range(origin[0], destination[0] - 1, -1)

            if origin[1] < destination[1]:
                # Going top to bottom
                y_seq = range(origin[1], destination[1] + 1)
            else:
                # Going bottom to top
                y_seq = range(origin[1], destination[1] - 1, -1)

            # print("From %s to %s" % (str(origin), str(destination)))
            # print(x_seq)
            # print(y_seq)
            # Loop both sequences together
            for x, y in zip(x_seq, y_seq):
                map[y][x] += 1

    overlaps_count = 0
    for row in map:
        for position in row:
            if position > 1:
                overlaps_count += 1

    print(overlaps_count)