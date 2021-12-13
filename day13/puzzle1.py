import sys
import time

import numpy as np

start_time = time.time()
np.set_printoptions(suppress=True, linewidth=np.nan, threshold=sys.maxsize)

with open('data.txt', 'r') as data_file:
    raw_dots = []
    max_row = 0
    max_column = 0
    for line in data_file:
        if line.strip():
            column, row = map(int, line.strip().split(','))
            if row > max_row:
                max_row = row
            if column > max_column:
                max_column = column
            raw_dots.append((row, column))
        else:
            break
    dots = np.zeros((max_row + 1, max_column + 1), dtype=bool)
    for raw_dot in raw_dots:
        dots[raw_dot[0], raw_dot[1]] = True
    folding_instructions = list()

    for line in data_file:
        folding_instructions.append(line.strip().split('along ')[1].split('='))


    def fold_along_y(dots, row):
        print('Folding along y axis, at row %d' % row)
        new_dots = dots[0:row, :]
        for iteration, folded_row in enumerate(dots[row + 1:, :]):
            modified_row_index = row - (iteration + 1)
            new_dots[modified_row_index] = new_dots[modified_row_index] | folded_row
        return new_dots


    def fold_along_x(dots, column):
        print('Folding along x axis, at column %d' % column)
        new_dots = dots[:, 0:column]
        for iteration, folded_column in enumerate(dots[:, column + 1:].transpose()):
            modified_column_index = column - (iteration + 1)
            new_dots[:, modified_column_index] = new_dots[:, modified_column_index] | folded_column
        return new_dots

    folding_instruction = folding_instructions[0]
    if folding_instruction[0] == 'x':
        dots = fold_along_x(dots, int(folding_instruction[1]))
    elif folding_instruction[0] == 'y':
        dots = fold_along_y(dots, int(folding_instruction[1]))

    print("There are %d dots" % dots.sum())

print("--- %s seconds ---" % (time.time() - start_time))
