class Player:

    count = 0

    def __init__(self, pos):
        self.id = Player.count 
        self.hit_points = 100
        self.stamina = 10
        self.pos = pos
        self.history = []
        Player.count += 1

    def __repr__(self) -> str:
        return f"{self.id} -> {self.pos}\n"