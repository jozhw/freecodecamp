file_name = input('File name: ')
try:
    open_file = open(file_name)
except:
    print(file_name, ' does not exist.')
    exit()


what_look_for = input("What do you want to search for?")

import re

names = {}
for line in open_file:
    line = line.rstrip()
    lst = re.findall('%s' % what_look_for, line)
    #lst = re.findall('^X.*:', line)
    if len(lst) != 0:
        lst = str(lst)
        names[lst] = names.get(lst, 0) + 1
        #print(lst)
t_order = []

#print(names)

for k,v in names.items():
    new_order = (v,k)
    t_order.append(new_order)

print(sorted(t_order, reverse=True))
