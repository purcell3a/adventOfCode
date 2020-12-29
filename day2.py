
filename = 'day2.txt'

# ************************************************************************************

file = open(filename, mode = 'r')
lines = file.readlines()

list_of_lines = []
for line in lines:
    line = line.replace(':', ' ')
    line = line.replace('-', ' ')
    line = line.replace('\n', ' ')
    line = line.split(' ')
    list_of_lines.append(line)

valid_passwords = 0
for line in list_of_lines:
    first_index = int(line[0]) - 1
    second_index = int(line[1])  -1
    letter = line[2]
    input_list = line[4]
    if input_list[first_index] == letter and input_list[second_index] != letter:
        valid_passwords += 1
    if input_list[second_index] == letter and input_list[first_index] != letter:
        valid_passwords += 1
print(valid_passwords)


# ************************************************************************************ 
#  too low = 324
#  too high = 686