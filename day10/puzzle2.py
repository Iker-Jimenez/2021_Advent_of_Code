import time
import queue

start_time = time.time()

scores = {')': 1, ']': 2, '}': 3, '>': 4}
syntax = {')': '(', ']': '[', '}': '{', '>': '<'}

final_scores = list()
with open('data.txt', 'r') as data_file:
    for line_num, line in enumerate(data_file):
        print('Processing line %d' % line_num)
        score = 0
        curr_opening_chars = queue.LifoQueue()
        corrupt_line = False
        for char in line.strip():
            if char in syntax.values():
                curr_opening_chars.put(char)
            else:
                if curr_opening_chars.get() is not syntax[char]:
                    print('Corrupt line found')
                    corrupt_line = True
                    break
        if not corrupt_line:
            while not curr_opening_chars.empty():
                opening_char = curr_opening_chars.get()
                closing_char = next(key for key, value in syntax.items() if value == opening_char)
                score = score * 5 + scores[closing_char]
            final_scores.append(score)

    final_scores.sort()
    print('Final scores %s' % final_scores)
    print('Score is %d' % final_scores[int(len(final_scores)/2)])


print("--- %s seconds ---" % (time.time() - start_time))