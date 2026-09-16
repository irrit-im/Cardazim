from connection import Connection


class Listener:
    def __init__(self, host: str, port: int, backlog: int = 1000) -> "Listener":
        pass

    def __repr__(self) -> str:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def accept(self) -> Connection:
        pass

    def __enter__(self) -> None:
        self.start()

    def __exit__(self) -> None:
        self.stop()
