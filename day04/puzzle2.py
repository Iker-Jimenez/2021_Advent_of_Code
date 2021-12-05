
with open('data.txt', 'r') as data_file:
    first_line = data_file.readline().strip()
    drawn_numbers = list(map(int, first_line.split(',')))
    print("Drawn numbers: " + str(drawn_numbers))
    # Skip blank line
    next(data_file)
    bingo_cards = list()
    num_lines = 0
    bingo_card = list()
    for line in data_file:
        bingo_card.append(list(map(int, line.split())))
        num_lines += 1
        if num_lines == 5:
            bingo_cards.append(bingo_card)
            bingo_card = list()
            num_lines = 0
            # Skip blank line
            next(data_file)

    # print('Bingo cards: ' + str(bingo_cards))

    def print_bingo_card(bingo_card):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in bingo_card]))

    def check_for_bingo(bingo_card):
        print('Checking card for winner')
        print_bingo_card(bingo_card)
        i = 0
        # Check rows
        for row in bingo_card:
            for number in row:
                if number != -1:
                    break
            else:
                print("Found winner in row")
                return True

        # Check columns
        for column_num in range(5):
            for row_num in range(5):
                if bingo_card[row_num][column_num] != -1:
                    break
            else:
                print("Found winner in column")
                return True

        print("No winner found")
        return False

    # Play bingo
    last_winner_card = None
    last_winner_number = -1
    winner_bingo_cards = list()
    for drawn_number in drawn_numbers:
        print("Winners so far: %s" % str(winner_bingo_cards))
        if len(bingo_cards) == len(winner_bingo_cards):
            print("All cards won, stop drawing numbers")
            break
        print('Playing number %d' % drawn_number)
        for bingo_card_num, bingo_card in enumerate(bingo_cards):
            if bingo_card_num in winner_bingo_cards:
                print("Skipping already won bingo card %s" % bingo_card_num)
                continue
            print('-- Checking card %d for number %d --' % (bingo_card_num, drawn_number))
            print_bingo_card(bingo_card)
            number_found = False
            for row_num, line in enumerate(bingo_card):
                for col_num, number in enumerate(line):
                    #print('Processing number %d in line %d from card %d' % (number, line_num, bingo_card_num))
                    if number == drawn_number:
                        print("Found %d in bingo_card %d" % (drawn_number, bingo_card_num))
                        number_found = True
                        line[col_num] = -1
                        if check_for_bingo(bingo_card):
                            print('%d bingo card is a winner!' % bingo_card_num)
                            last_winner_card = bingo_card
                            last_winner_number = drawn_number
                            winner_bingo_cards.append(bingo_card_num)
                        break
                if number_found:
                    break
            else:
                print("Number %d not found in bingo card %d" % (drawn_number, bingo_card_num))
        else:
            continue

    print("Winner number %d" % last_winner_number)
    print("Winner card:")
    print_bingo_card(last_winner_card)

    score = 0
    for line in last_winner_card:
        for number in line:
            if number != -1:
                score += number

    print("Card score is %d" % (last_winner_number * score))
