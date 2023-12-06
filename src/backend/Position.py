class Position:
    def __init__(self, pos):
        self.y = pos[0]
        self.x = pos[1]

    def __add__(self, other):
        assert isinstance(other, Position)
        return Position((self.y + other.y, self.x + other.x))

    def __repr__(self) -> str:
        return f"pos({self.y},{self.x})"


if __name__ == "__main__":
    p1 = Position((0, 0))
    p2 = Position((0, 1))

    print(p1 + p2)

    pp1 = (0, 0)
    pp2 = (2, 3)