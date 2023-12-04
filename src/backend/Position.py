class Position:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
    
    def __add__(self, other):
        assert isinstance(other, Position)
        return Position((self.x + other.x, self.y + other.y))
    
    def __repr__(self) -> str:
        return f"pos({self.x},{self.y})"