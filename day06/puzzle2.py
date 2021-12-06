import time
start_time = time.time()

num_days = 256
with open('data.txt', 'r') as data_file:
    input = list(map(int, data_file.readline().split(',')))
    lanternfishes = [0] * 9
    for fish in input:
        lanternfishes[fish] += 1

    print(lanternfishes)

    for day in range(num_days):
        print('Processing day %d' % day)
        new_lanternfishes = [0] * 9
        for age in range(8, -1, -1):
            if age == 0:
                new_lanternfishes[6] += lanternfishes[0]
                new_lanternfishes[8] = lanternfishes[0]
            else:
                new_lanternfishes[age - 1] = lanternfishes[age]
        lanternfishes = new_lanternfishes

    print("Final count of lanternfishes: %d" % sum(lanternfishes))

print("--- %s seconds ---" % (time.time() - start_time))