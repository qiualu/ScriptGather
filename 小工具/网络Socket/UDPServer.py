import socket

BUFSIZE = 1024
ip_port = ('127.0.0.1', 1001)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
server.bind(ip_port)

while True:
    data, client_addr = server.recvfrom(BUFSIZE)

    zl = data.decode().split(",")
    # server.sendto(data.upper(), client_addr)
    print('server收到的数据', zl)

server.close()


