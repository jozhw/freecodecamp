file = input('File name: ')
ofile = open(file)
count = 0
for line in ofile:
    count = count + 1
    linecap = line.upper()
    print(linecap)
print('There are ', count , 'lines')
