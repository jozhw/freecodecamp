file_name = input('File name: ')
lines = [line.strip('\n') for line in open(file_name, 'r')]
# this only works for python to have embedded clauses like the above
word_list = []

for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_list:
            pass
        else:
            word_list.append(word)

print(sorted(word_list))

#I did not do this... found the solution on the internet
