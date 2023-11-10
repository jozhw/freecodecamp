file_name = input('File name: ')
try:
    open_file = open(file_name)
except:
    print(file_name, ' does not exist.')
    exit()

count = 0
total = 0
import re

#what_to_find = input('What would you like to find? ')

for line in open_file:
    line = line.rstrip()
    number_find = re.findall('^New Revision:(\s[0-9.]+)', line)
    #print(number_find)
    if len(number_find) > 0:
        for number in number_find:
            try:
                int_number = int(number)
                #print(int_number)
                total = total + int_number
                count = count + 1
            except:
                    continue
    else:
        #print('none')
        continue


try:
    average = total/count
    print(average, total, count)
except:
    print('no values were obtained')
    exit()
