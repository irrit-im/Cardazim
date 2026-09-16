import argparse
import sys
import socket
import struct
import threading

HEADER_SIZE = 4


def recieve_data(socket: socket.socket) -> None:
    connection, _addr = socket.accept()
    data_len = int.from_bytes(connection.recv(HEADER_SIZE), "little")
    raw_data = b""
    while data_len > 0:
        new_data = connection.recv(data_len)
        raw_data += new_data
        data_len -= len(new_data)

    data = raw_data.decode()
    print(f"connected. received: {data}")


def run_server(ip, port) -> None:
    with socket.socket() as serversocket:
        serversocket.bind((ip, port))
        serversocket.listen(5)
        while True:

            t = threading.Thread(target=recieve_data, args=(serversocket,))
            t.start()


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
