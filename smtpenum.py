#!/usr/bin/python
import socket
import sys

def rcptto(username):
# RCPT TO a user
        user = (username).encode()
        s.send(b'HELO example.com' + b'\r\n')
        s.recv(1024)
        s.send(b'MAIL FROM: x@example.com'+ b'\r\n')
        s.recv(1024)
        s.send(b'RCPT TO: ' + user + b'\r\n')
        result = s.recv(1024)
        print(result)

# VRFY a user
def vrfy(username):
        user = (username).encode()
        s.send(b'VRFY ' + user + b'\r\n')
        result = s.recv(1024)
        print(result)

# EXPN a user
def expn(username):
        user = (username).encode()
        s.send(b'HELO example.com' + b'\r\n')
        s.recv(1024)
        s.send(b'EXPN ' + user + b'\r\n')
        result = s.recv(1024)
        print(result)

if len(sys.argv) != 3:
        print("Usage: smtpenum.py <username> <target_ip>")
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
ip = sys.argv[2]
connect = s.connect((ip,25))

# Receive the banner
banner = s.recv(1024)

print(banner)

rcptto(sys.argv[1])
vrfy(sys.argv[1])
expn(sys.argv[1])

# Close the socket
s.close()
