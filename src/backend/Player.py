from Position import Position
from time import sleep

class Player:

    count = 0

    def __init__(self, pos):
        self.id = Player.count 
        self.hit_points = 100
        self.stamina = 10
        self.pos = Position(pos)
        self.history = []
        Player.count += 1

    def __repr__(self) -> str:
        return f"{self.id} -> {self.pos}\n"
    
    def move_right(self, dist=4):
        for _ in range(dist):
            self.pos += Position((1,0))
            sleep(1e-1)

    def move_left(self, dist=4):
        for _ in range(dist):
            self.pos += Position((-1,0))
            sleep(1e-1)

if __name__ == "__main__":
    p = Player((368, 20))
    print(p)
    p.move_left()
    print(p)
    p.move_right()
    print(p)
