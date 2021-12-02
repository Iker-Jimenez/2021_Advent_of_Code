
horizontal_pos = 0
depth = 0

with open('data.txt', 'r') as data_file:
    for line in data_file:
        command_set = line.split()
        command = command_set[0]
        amount = int(command_set[1])
        if command == "forward":
            horizontal_pos += amount
        elif command == "down":
            depth += amount
        elif command == "up":
            depth -= amount

print("Horizontal: %d, Depth:%d" % (horizontal_pos, depth))
print("Position is %d " % (horizontal_pos * depth))
