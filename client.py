import argparse
import sys
import socket
import struct

###########################################################
####################### YOUR CODE #########################
###########################################################


def send_data(server_ip, server_port, data: bytes):
    '''
    Send data to server in address (server_ip, server_port).
    '''
    bytes_data = data.encode("utf-8")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    packed_data = struct.pack(f"<l{len(bytes_data)}s",len(bytes_data), bytes_data) #little endian(<), long(l), bytes(s)
    s.sendall(packed_data)

###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help="the server's ip")
    parser.add_argument('server_port', type=int,
                        help="the server's port")
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        send_data(args.server_ip, args.server_port, args.data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())


