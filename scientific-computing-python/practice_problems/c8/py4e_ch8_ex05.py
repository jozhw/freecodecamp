file_name = input('File name:')
try:
    open_file = open(file_name)
except:
    print('File name ', file_name, 'not found')
    quit()

email_list = []
for line in open_file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    elif words[0] == 'From':
        #print(words[1])
        email_list.append(words[1])
Rank = 0
for email in email_list:
    Rank = Rank + 1
    print(Rank, ': ', email)
