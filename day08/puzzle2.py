import time
start_time = time.time()

with open('data.txt', 'r') as data_file:
    final_result = 0
    for line in data_file:
        signals, output = line.split('|')
        signals = [set(x) for x in signals.split()]
        output = [set(x) for x in output.split()]
        print(signals)
        print(output)
        mappings = [{} for x in range(10)]
        for digit in signals:
            length = len(digit)
            if length == 2:
                mappings[1] = digit
            elif length == 3:
                mappings[7] = digit
            elif length == 4:
                mappings[4] = digit
            elif length == 7:
                mappings[8] = digit

        for digit in signals:
            length = len(digit)
            # 2, 3 or 5
            if length == 5:
                if len(digit.intersection(mappings[1])) == 2:
                    mappings[3] = digit
                elif len(digit.intersection(mappings[4])) == 3:
                    mappings[5] = digit
                else:
                    mappings[2] = digit
            # 0, 6 or 9
            elif length == 6:
                if len(digit.intersection(mappings[4])) == 4:
                    mappings[9] = digit
                elif len(digit.intersection(mappings[1])) == 2:
                    mappings[0] = digit
                else:
                    mappings[6] = digit

        dictionary = {}
        for idx, mapping in enumerate(mappings):
            dictionary[frozenset(mapping)] = idx

        print(dictionary)
        result = ''
        for digit in output:
            result += str(dictionary[frozenset(digit)])
        final_result += int(result)

print('Final result is %d' % final_result)
print('--- %s seconds ---' % (time.time() - start_time))