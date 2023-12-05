class Position:
    def __init__(self, pos):
        self.x = pos[1]
        self.y = pos[0]
    
    def __add__(self, other):
        assert isinstance(other, Position)
        return Position((self.y + other.y, self.x + other.x))
    
    def __repr__(self) -> str:
        return f"pos({self.y},{self.x})"