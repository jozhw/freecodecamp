f_name = input('File name please: ')
try:
    open_file = open(f_name)
except:
    print('File, ', f_name, ' cannot be found.')

alphabet = {}

import re

for line in open_file:
    line = re.sub('[^A-Za-z]', '', line)
    line = line.lower()
    words = line.split()
    for word in words:
        letters = word[:]
        #print(letters)
        for letter in letters:
            #print(letter)
            alphabet[letter] = alphabet.get(letter, 0) + 1

#print(sorted(alphabet.items()))
# without the .items() it only prints out the key and not the value

print(sorted([(v,k) for k,v in alphabet.items()], reverse=True))
