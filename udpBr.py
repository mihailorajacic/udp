import argparse, socket

UDP_IP= "127.0.0.1"


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(1024)
        print("Primio sam poruku: ",data)
def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tekst=input("Unesi tekst koji zelis: ")
    b = bytearray()
    b.extend(map(ord, tekst))
    sock.sendto(b, (UDP_IP, port))




if __name__ == '__main__':
    choices = {'klijent': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)