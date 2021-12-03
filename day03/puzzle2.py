
records = list()
with open('data.txt', 'r') as data_file:
    for line in data_file:
        records.append(line.strip())


def process_records(records, position, keep_most_common):
    counter = 0
    records_to_keep = list()
    num_records = 0
    for record in records:
        num_records += 1
        counter += int(record[position])
    if keep_most_common:
        most_common_value = 1 if counter >= num_records/2 else 0
    else:
        most_common_value = 0 if counter >= num_records/2 else 1

    for record in records:
        if int(record[position]) == most_common_value:
            records_to_keep.append(record)
    return records_to_keep


potential_records = records
position = 0
while len(potential_records) > 1:
    potential_records = process_records(potential_records, position, True)
    position += 1

oxygen_generator_rating = int(potential_records[0], 2)
print(oxygen_generator_rating)

potential_records = records
position = 0
while len(potential_records) > 1:
    potential_records = process_records(potential_records, position, False)
    position += 1

co2_scrubber_rating = int(potential_records[0], 2)
print(co2_scrubber_rating)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating)
