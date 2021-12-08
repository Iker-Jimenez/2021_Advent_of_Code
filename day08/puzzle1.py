import time
start_time = time.time()

with open('data.txt', 'r') as data_file:
    count_known_digits = 0
    for line in data_file:
        output = line.split('|')[1].split()
        for digit in output:
            length = len(digit)
            if length == 2 or length == 3 or length == 4 or length == 7:
                count_known_digits += 1

    print('There are %d digits' % count_known_digits)
print("--- %s seconds ---" % (time.time() - start_time))