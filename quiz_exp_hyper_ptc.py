import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
# Use the telnet program as shown in lecture to retrieve the headers and content.