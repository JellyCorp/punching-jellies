from Map import Map
from Player import Player
    
class Main:

    def __init__(self,
                start_positions,
                grid_dim = (500,700),
                ):
        self.map = Map(grid_dim)
        nb_players = len(start_positions)
        self.players = [Player(start_positions[i]) for i in range(nb_players)]

if __name__ == "__main__":
    main = Main(start_positions=[(368, 20), (368, 648)])
    print(main.players)