from random import choice
from time import sleep
import threading

from .Map import Map
from .Player import Player


class Main(threading.Thread):
    def __init__(self, start_positions, grid_dim, max_t):
        super().__init__()

        self.map = Map(grid_dim=grid_dim, max_t=max_t)
        self.nb_players = len(start_positions)
        self.players = [
            Player(start_positions[i], self.map) for i in range(self.nb_players)
        ]

    def is_over(self):
        count = self.nb_players
        for player in self.players:
            if player.hit_points <= 0:
                count -= 1
        return count <= 1 or self.map.get_time() >= self.map.max_t

    def run(self):
        i = 0
        while not self.is_over():
            for player in self.players:
                player.decide()
            for player in self.players:
                player.update()
            sleep(1 / 60)
            i += 1
        print(i)


if __name__ == "__main__":
    main = Main(start_positions=[(368, 20), (368, 648)], grid_dim=(500, 700), max_t=1)
    main.start()
    print(main.players[0].history)
