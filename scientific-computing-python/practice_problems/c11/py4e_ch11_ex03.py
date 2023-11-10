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
    item = line.split()
    #the problem with this code is right here - you split
    for value in item:
        #print(value)
    #number_find = re.findall('%s' % what_to_find, line)
        number_find = re.findall('New Revision:(\s[0-9.]+)', value)
        #the above produces a list
        print(number_find)
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
except:
    print('no values were obtained')

print(average, total, count)
