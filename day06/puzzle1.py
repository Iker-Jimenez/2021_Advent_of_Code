import time
start_time = time.time()

num_days = 80
with open('data.txt', 'r') as data_file:
    lanternfishes = list(map(int, data_file.readline().split(',')))
    print(lanternfishes)

    for day in range(num_days):
        print('Processing day %d' % day)
        new_lanternfishes = list()
        num_newborns = 0
        for lanternfish in lanternfishes:
            if lanternfish == 0:
                num_newborns += 1
                lanternfish = 6
            else:
                lanternfish -= 1
            new_lanternfishes.append(lanternfish)

        new_lanternfishes += [8] * num_newborns
        lanternfishes = new_lanternfishes
    print("Final count of lanternfishes: %d" % len(lanternfishes))

print("--- %s seconds ---" % (time.time() - start_time))