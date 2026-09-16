import argparse
import sys

from listener import Listener

HEADERSIZE = 4


def run_server(ip, port) -> None:
    with Listener(ip, port) as listener:
        print(listener)
        with listener.accept() as connection:
            print(connection.receive_message())


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
