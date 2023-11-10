import socket


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
count = 0

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
#print('error below')
cmd_not = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd_not.encode()
# have to break up the above because the encode will do the string first
# before the string addition.
#print('error below')
mysock.send(cmd)
#print('error below')

while True:
    data = mysock.recv(512)
    if count >= 3000 or len(data) < 1:
        break
    count = count + len(data)
    print(data.decode(),end='')


mysock.close()
print(' Total character count is: ', count)
