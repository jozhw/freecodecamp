import re
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
o = input('file? ')
# added the above
s = open(o)
for line in s:
    lst = re.findall('\S+@\S+', line)
    #
    if len(lst) != 0:
        print(lst)
    else:
        continue
    #this if/else statements prevents the non find from appearing in print
