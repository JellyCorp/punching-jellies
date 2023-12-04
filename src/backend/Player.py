from Position import Position
from time import sleep
from Map import Map

class Player:

    count = 0

    def __init__(self, pos, map):
        self.id = Player.count 
        self.hit_points = 100
        self.stamina = 10
        self.pos = Position(pos)
        self.history = []
        self.map = map
        Player.count += 1

    def __repr__(self) -> str:
        return f"{self.id} -> {self.pos}\n"
    
    def move_right(self, dist=10):
        for _ in range(dist):
            if (self.map.is_valid(self.pos + Position((1,0)), (32,32))):
                self.pos += Position((1,0))
            print(self.pos)
            sleep(1e-1)

    def move_left(self, dist=10):
        for _ in range(dist):
            if (self.map.is_valid(self.pos + Position((-1,0)), (32,32))):
                self.pos += Position((-1,0))
            print(self.pos)
            sleep(1e-1)

if __name__ == "__main__":
    p = Player((5, 20), Map())
    p.move_left()

