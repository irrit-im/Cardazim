import argparse
import sys
import threading

from connection import Connection
from listener import Listener

HEADER_SIZE = 4
MAX_CONNECTIONS = 2


def get_message(connection: Connection) -> str:
    assert isinstance(connection, Connection)
    message = connection.receive_message()
    print(f"Rceived: {message}")
    return message


def run_server(ip, port) -> None:
    with Listener(ip, port) as listener:
        print(listener)
        connections = []
        threads = []
        try:
            for _ in range(MAX_CONNECTIONS):
                connection = listener.accept()
                connections.append(connection)
                assert isinstance(connection, Connection)
                t = threading.Thread(target=get_message, args=(connection,))
                t.start()
                threads.append(t)
        finally:
            for thread in threads:
                thread.join()
            for connection in connections:
                connection.close()


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

    run_server(args.server_ip, args.server_port)
    print("Done.")


if __name__ == "__main__":
    sys.exit(main())
