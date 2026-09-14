import argparse
import sys
import socket
import struct
import threading

HEADERSIZE = 4


def recieve_data(connection) -> None:
    data_len = connection.recv(4)
    raw_data = connection.recv(data_len)
    data = raw_data[4:].decode("utf-8")
    print(f"connected. recieved: {data}")
    connection.close()


def run_server(ip, port) -> None:
    serversocket = socket.socket()
    serversocket.bind((ip, port))
    serversocket.listen(5)
    while True:
        connection, addr = serversocket.accept()
        t = threading.Thread(target=recieve_data, args=(connection))


def get_args():
    parser = argparse.ArgumentParser(description="listen.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
