import re

fname = input('Enter file:')
try:
    hand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
lst = []
for line in hand:
    line = line.rstrip()
    num = re.findall('^New Revision:(\s[0-9.]+)',line)
    if len(num) > 0:
        for number in num:
            number = float(number)
        lst.append(number)
avg = sum(lst)/len(lst)
print(avg)
