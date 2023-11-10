file = input('File name: ')
try:
    ffile = open(file)
except:
    if file.lower() == 'pikachu':
        print('Gotta catch them all!')
        quit()
    else:
        print('File: ', file,' cannot be found' )
    quit()
count = 0
value = 0
for line in ffile:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        #print(len(line))
        count = count + 1
        print(count)
        colon = line.find(':')
        number = line[colon + 2:]
        fnumber = float(number)
        print(fnumber)
        value = value + fnumber
        print(value)
        print(line)
print('The average is', value/count)
