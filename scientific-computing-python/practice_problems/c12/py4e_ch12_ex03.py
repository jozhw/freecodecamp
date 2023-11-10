import urllib.request, urllib.parse, urllib.error

url = input('URL: ')

fhand = urllib.request.urlopen(url)

count = 0
max_count = 3000

for line in fhand:
    words = (line.decode().strip())
    count = count + len(words)
    if count >= max_count:
        break
    else:
        print(line)

print(count)




print(count)
