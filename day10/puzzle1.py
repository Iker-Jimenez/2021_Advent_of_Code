import time
import queue
start_time = time.time()

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
syntax = {')': '(', ']': '[', '}': '{', '>': '<'}

with open('data.txt', 'r') as data_file:
    total_score = 0
    for line_num, line in enumerate(data_file):
        print('Processing line %d' % line_num)
        curr_opening_chars = queue.LifoQueue()
        for char in line.strip():
            if char in syntax.values():
                curr_opening_chars.put(char)
            else:
                if curr_opening_chars.get() is not syntax[char]:
                    print('Corrupt line found')
                    total_score += scores[char]
                    break

    print('Total score %d' % total_score)

print("--- %s seconds ---" % (time.time() - start_time))