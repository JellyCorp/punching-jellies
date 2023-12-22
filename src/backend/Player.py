from enum import Enum
from time import sleep
import sys
import os
from scipy.special import softmax

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # TODO shitty solution, needs to be cleared

from models.FullyConnected import FullyConnected
from .Position import Position
from .Map import Map


class Actions(Enum):
    none = None
    move_right = "move_right"
    move_left = "move_left"


class Player:
    count = 0

    def __init__(self, position: Position, map: Map, brain: FullyConnected = None):
        self.brain = (
            brain if brain is not None else FullyConnected([2, 4, len(Actions)])
        )
        self.id = Player.count
        self.hit_points = 100
        self.stamina = 10
        self.position = Position(position)
        self.history = []
        self.map = map
        self.next_action = Actions.none
        self.size = (32, 32)
        Player.count += 1

        self.checkpoint_step = 0

    def __repr__(self) -> str:
        return f"{self.id} -> {self.position} -> {self.checkpoint_step}\n"

    def decide(self):
        # Pass the input to the model
        thoughts = self.brain(
            [
                self.position.x,
                #  self.size[1],
                self.map.checkpoints[self.checkpoint_step],
            ]
        )

        # Apply softmax to output vector
        thoughts = list(softmax(thoughts))

        # Choose Action with the highest probability
        self.next_action = list(Actions)[thoughts.index(max(thoughts))]

    def move_right(self, dist=1):
        start_position = self.position
        self._move((0, 1), dist)
        self.history.append(
            (self.map.get_time(), Actions.move_right, start_position, self.position)
        )

    def move_left(self, dist=1):
        start_position = self.position
        self._move((0, -1), dist)
        self.history.append(
            (self.map.get_time(), Actions.move_left, start_position, self.position)
        )

    def _move(self, vect: (int, int), dist):
        for _ in range(dist):
            if self.map.is_valid(self.position + Position(vect), self.size):
                self.position += Position(vect)
            # sleep(1 / 60)

    def update(self):
        assert isinstance(self.next_action, Actions)
        match self.next_action:
            case Actions.move_right:
                self.move_right()
            case Actions.move_left:
                self.move_left()
        self.next_action = Actions.none

        if (
            self.position.x <= self.map.checkpoints[self.checkpoint_step]
            and self.map.checkpoints[self.checkpoint_step]
            <= self.position.x + self.size[1]
            and self.checkpoint_step < len(self.map.checkpoints)
        ):
            self.checkpoint_step += 1


if __name__ == "__main__":
    p = Player(position=(5, 20), map=Map((500, 700), 5))
    print(p.position)
    p.decide()
    p.update()
    print(p.position)
    print(len(Actions))
