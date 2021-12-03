
counters = [0] * 12

total_records = 0
with open('data.txt', 'r') as data_file:
    for line in data_file:
        total_records += 1
        for position, bit in enumerate(line.strip()):
            counters[position] += int(bit)

print(counters)
gamma_rate = int(''.join(['1' if counter>total_records/2 else '0' for counter in counters]), 2)
print(gamma_rate)

epsilon_rate = int(''.join(['0' if counter>total_records/2 else '1' for counter in counters]), 2)
print(epsilon_rate)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
