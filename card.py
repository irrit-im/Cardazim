from typing import Union

import CryptImage


class Card:
    def __init__(
        self,
        name: str,
        creator: str,
        image: CryptImage,
        riddle: str,
        solution: str | None,
    ):
        self.name: str = name
        self.creator: str = creator
        self.image: CryptImage = image
        self.riddle: str = riddle
        self.solution: str = solution

    def __repr__(self) -> str:
        return f"<Card name={self.name}, creator={self.creator}"

    def __str__(self) -> str:
        return f"Card {self.name} by {self.creator}\nRiddle: {self.riddle}\nSolution: {self.solution if self.solution else "unsolved"}"

    @classmethod
    def create_from_class(
        cls,
        name: str,
        creator: str,
        path: Union[str, PathLike],
        riddle: str,
        solution: str,
    ) -> "Card":  # TODO: what is the path type
        pass
