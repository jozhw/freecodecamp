#!/usr/bin/env python3
"""
Exercise  12.5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember that
recv is receiving characters (newlines and all), not lines.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
import socket

URL = input('Url: ')
URL_naked = URL.split('/')[2]

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((URL_naked, 80))
cmd_non = 'GET ' + URL + ' HTTP/1.0\r\n\r\n'
cmd = cmd_non.encode()
my_sock.send(cmd)

data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # Finds the end of header
# Adds four to exclude:'\r\n\r\n'
print(message[header_end_pos:], end='')
while True:                                 # Header in the first data only
    data = my_sock.recv(512)
    if not data:
        break
    print(data.decode())
my_sock.close()
