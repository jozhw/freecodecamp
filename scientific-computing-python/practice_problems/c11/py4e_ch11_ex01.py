file_name = input('File name: ')
try:
    open_file = open(file_name)
except:
    print(file_name, ' does not exist.')
    exit()

count = 0

what_look_for = input("What do you want to search for?")

import re

for line in open_file:
    line = line.rstrip()
    #if re.search(re.escape(what_look_for), line):
        #use re.escape(variable) to put in a variable and eliminate escape
            #variable like \ for python
    if re.search("%s" % what_look_for, line):
        #do not filter escape characters
        # so you can use the ^ for indicate first in the line
        count = count + 1
    else:
        continue

print(what_look_for, 'occurs', count, 'times.')
