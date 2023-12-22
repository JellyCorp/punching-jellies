import random
import json
import sys
import os
import numpy as np
from copy import deepcopy

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # TODO shitty solution, needs to be cleared ...

from FullyConnected import FullyConnected
from backend.Player import Player
from backend.Map import Map


class Population:
    def __init__(self, nb_players: int = 50, list_players: list = None):
        Player.count = 0
        self.nb_players = nb_players
        self._map = Map(grid_dim=(500, 700), max_t=10)
        if list_players == None:
            self.players = [
                Player(position=(0, 20), map=self._map) for _ in range(nb_players)
            ]
        else:
            self.players = list_players
        self.selected = []

    def evaluate(
        self, steps: int = 1000
    ):  # steps is the time you give the agents to complete
        for _ in range(steps):
            for player in self.players:
                player.decide()
            for player in self.players:
                player.update()

    def _select(self):
        sorted_players = sorted(self.players, key=lambda player: player.checkpoint_step)
        selected = sorted_players[self.nb_players // 2 : self.nb_players]
        print(selected[-3:])
        # path = "/models_data/data.txt"
        # with open(path, "w") as file:
        #     for best in selected[-3:]:  # Show the actions history of the 3 best elements
        #         for el in best.history:
        #             file.write(f"{el[1]}\n")

        # return selected

    def generate_next_population(self, p: float = 0.6):
        # 1. evaluate
        self.evaluate()

        # 2. select
        selected_players = self._select()

        # 3. cross-breed p best and mutate 1-p remaining
        # 3.1. cross-breed p best
        cb_parents = selected_players[
            round((1 - p) * len(selected_players)) :
        ]  # 1-p to end of list gives p values!!
        if len(cb_parents) % 2 != 0:
            cb_parents.append(cb_parents[len(cb_parents) - 1])
        cb_children = []
        cb_parents1 = cb_parents[: int(len(cb_parents) / 2)]
        cb_parents2 = cb_parents[int(len(cb_parents) / 2) :]

        for cbp1, cbp2 in zip(cb_parents1, cb_parents2):
            brain1, brain2 = cbp1.brain.cross_breed(cbp2.brain, sigma=0.05)
            cb_children.append(Player(position=(0, 20), map=self._map, brain=brain1))
            cb_children.append(Player(position=(0, 20), map=self._map, brain=brain2))

        # 3.2. mutate 1-p remaining
        mut_parents = selected_players[: round((1 - p) * len(selected_players))]
        mut_children = []
        for mut in mut_parents:
            child_brain = deepcopy(mut.brain)
            child_brain.mutate()
            mut_children.append(
                Player(position=(0, 20), map=self._map, brain=child_brain)
            )

        # 4. recompose next population
        next_population = cb_parents + cb_children + mut_parents + mut_children
        for player in next_population:
            player.checkpoint_step = 0  # TODO add other values to be reset
            player.position.x, player.position.y = 0, 20

        for i in range(abs(len(next_population) - self.nb_players)):
            next_population = next_population[1:]

        return next_population


if __name__ == "__main__":
    pop = Population()

    print(os.path.dirname(sys.executable))
    for i in range(2):
        players_next = pop.generate_next_population()
        pop_next = Population(list_players=players_next)
        pop = pop_next
