from fabric import Connection

server = Connection(host='10.0.0.63', user='ubuntu', connect_kwargs={'password': 'morbed'})


def upload(file):
    server.put(file, '/home/ubuntu/Kaz/Transfer/')


def download(file):
    server.get(file, '/Users/kaznado/Desktop/server-dl/')


