import socket


class Connection:
    def __init__(self, connection: socket.socket) -> "Connection":
        pass

    def __repr__(self) -> str:
        return f"<connection from {source} to {dest}"

    def send_message(self, message: bytes) -> None: ...

    def receive_message(self) -> str: ...

    @classmethod
    def connect(cls, host, port) -> None: ...

    def close(self) -> None: ...

    def __enter__(self): ...

    def __exit__(self): ...
