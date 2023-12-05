from enum import Enum

from .Position import Position
from .Map import Map


class Actions(Enum):
    move_right = "move_right"
    move_left = "move_left"
    none = None


class Player:
    count = 0

    def __init__(self, position, map):
        self.id = Player.count
        self.hit_points = 100
        self.stamina = 10
        self.position = Position(position)
        self.history = []
        self.map = map
        Player.count += 1
        self.next_action = None

    def __repr__(self) -> str:
        return f"{self.id} -> {self.position}\n"

    def move_right(self, dist=10):
        start_position = self.position
        self._move((0, 1), dist)
        self.history.append(
            (self.map.get_time(), Actions.move_right, start_position, self.position)
        )

    def move_left(self, dist=10):
        start_position = self.position
        self._move((0, -1), dist)
        self.history.append(
            (self.map.get_time(), Actions.move_left, start_position, self.position)
        )

    def _move(self, vect, dist):
        for _ in range(dist):
            if self.map.is_valid(self.position + Position(vect), (32, 32)):
                self.position += Position(vect)

    def update(self):
        print(self.next_action)
        match self.next_action:
            case Actions.move_right:
                self.move_right()
            case Actions.move_left:
                self.move_left()
        self.next_action = None


if __name__ == "__main__":
    p = Player((5, 20), Map())
    p.move_left()
