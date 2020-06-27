import socket
import time

host = 'localhost'
port = 9000
address = (host, port)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
f = open('ExperimentFakeP300.txt', 'w')

while True:
    x = input("Press Enter to send P300 (q + enter - to quit):")
    ts = time.time()
    if x == "q":
        break
    print(ts)
    data = b'0x01'
    udp_socket.sendto(data, address)
    f.write(str(ts) + '\n')
    print("Sent P300")

f.close()
udp_socket.close()
