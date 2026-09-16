import socket
import struct


class Connection:
    def __init__(self, connection: socket.socket) -> "Connection":
        self.connection: socket.socket = connection

    @classmethod
    def connect(cls, host, port) -> "Connection":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = sock.connect((host, port))
        return cls(connection=connection)

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
        print(f"Received: {data}")

    def close(self) -> None:
        self.connection.close()

    def __enter__(self, host, port) -> None:
        self.connect(host, port)

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.close()


if __name__ == "__main__":
    with Connection.connect("127.0.0.1", 5000) as c:
        c.send_message("fdshjhgjkdfhdhfhgh")
