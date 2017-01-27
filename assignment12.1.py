try:
    import socket
    url = raw_input('Enter - ')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = url.split('/')
    print host[2]
    mysock.connect((host[2], 80))
except:
    print'Wrong input!'

