"""
Not sure how to solve this as of 3.5.22. I need to brush up on html to produce
a code that will allow for me to locate the footers.

"""
import socket

URL = input('Url: ')
URL_naked = URL.split('/')[2]

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((URL_naked, 80))
cmd_non = 'GET ' + URL + ' HTTP/1.0\r\n\r\n'
cmd = cmd_non.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if len(data) < 1: break
    data = data.decode()
    print(data)
