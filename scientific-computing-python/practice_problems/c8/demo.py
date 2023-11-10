file_name = input('File name: ')
try:
    open_file = open(file_name)
except:
    print('File: ', file_name, ' does not exist or is in the wrong directory.')

for line in open_file:
    words = line.split()
    print(words)
    if words[0] = 'From ':
