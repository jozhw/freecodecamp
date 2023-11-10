fname = input('File name: ')
try:
    file_open = open(fname)
except:
    print('File: ', fname, ' does not exist.')
    exit()

emails = {}

for line in file_open:
    words = line.split()
    for word in words:
        if len(words) == 0 or words[0] != 'From':
            #print('no email')
            continue
        else:
            #print(words[1])
            emails[words[1]] = emails.get(words[1], 0) + 1
            # you do not want to do word[1] for that references the character
            # in the string
print(emails)

lst = []

for k,v in emails.items():
    newrang = (v,k)
    lst.append(newrang)
lst = sorted(lst, reverse=True)
print(lst)

# a embedded code for the above in one line is below
# print = (sorted([(v,k) for k,v in emails.items()], reverse=True))
