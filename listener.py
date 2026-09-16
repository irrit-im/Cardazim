import socket

from connection import Connection
from typing import Self


class Listener:
    def __init__(self, host: str, port: int, backlog: int = 1000) -> "Listener":
        self.host = host
        self.port = port
        self.backlog = backlog
        self.socket = socket.socket()

    def __repr__(self) -> str:
        return f"Listener(host = {self.host}, = {self.port}, backlog = {self.backlog})"

    def start(self) -> None:
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.backlog)
        print("bound and listening")

    def stop(self) -> None:
        self.socket.close()

    def accept(self) -> Connection:
        connection, _addr = self.socket.accept()
        print(f"connected to {connection.getpeername()}")
        return Connection(connection)

    def __enter__(self) -> Self:
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.stop()


if __name__ == "__main__":
    with Listener("127.0.0.1", 5006) as listener:
        print(listener)
        with listener.accept() as connection:
            print(connection.receive_message())
