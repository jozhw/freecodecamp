import re
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
o = input('Message: ')
s = open(o)
names = {}
for line in s:
    line = line.rstrip()
    #lst = re.findall('\S+@\S+', line)
    lst = re.findall('^X-\S+:', line)
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
