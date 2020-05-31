import socket

host = 'localhost'
port = 9000
address = (host, port)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    x = input("Press Enter to send P300")
    data = b'0x01'
    udp_socket.sendto(data, address)
    print("Sent P300")

udp_socket.close()
