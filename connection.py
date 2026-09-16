import socket
import struct
from typing import Self


class Connection:
    def __init__(self, connection: socket.socket) -> "Connection":
        self.connection: socket.socket = connection

    @classmethod
    def connect(cls, host, port) -> "Connection":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return cls(connection=sock)

    def __repr__(self) -> str:
        source_ip, source_port = self.connection.getsockname()
        dest_ip, dest_port = self.connection.getpeername()
        return f"<connection from {source_ip} {source_port} to {dest_ip} {dest_port}"

    def send_message(self, message: bytes | str) -> None:
        if isinstance(message, str):
            message = message.encode()
        packed_data = struct.pack(
            f"<l{len(message)}s", len(message), message
        )  # little endian(<), long(l), bytes(s)
        self.connection.sendall(packed_data)

    def receive_message(self) -> str:
        data_len = int.from_bytes(self.connection.recv(4), "little")
        raw_data = self.connection.recv(data_len)
        data = raw_data.decode("utf-8")
        return data

    def close(self) -> None:
        self.connection.close()

    def __enter__(self, *args, **kwargs) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.close()


if __name__ == "__main__":
    with Connection.connect("127.0.0.1", 5006) as c:
        c.send_message("gffj")
        c.send_message("fojghkfjfk")
