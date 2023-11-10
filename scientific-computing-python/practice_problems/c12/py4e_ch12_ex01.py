import socket
#http://data.pr4e.org/romeo.txt

url = input('URL: ')
try:
    if '/' in url:
        host_name = url.split('/')[2]
        print(host_name)

    else:
        print(url, ' is not a valid url link.')
        exit()

except:
    print(url, ' is not a valid url link.')
    exit()


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
print('error below')
cmd_not = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd_not.encode()
# have to break up the above because the encode will do the string first
# before the string addition.
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
