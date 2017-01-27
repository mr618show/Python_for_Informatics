import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/intro-short.txt HTTP/1.0\n\n')
count = 0
while True:
    data = mysock.recv(512) 
    if(len(data)<1):break
    count = count+len(data)
    if count <3000:
        print data
    print count
mysock.close()