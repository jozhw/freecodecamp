import re

a_string = "The quick brown fox jumped over the lazy dog."
pattern = input("name?")
match = re.search("%s" % pattern, a_string)
if match != 'chicken':
    print('success')

print(match)
