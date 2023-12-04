from time import perf_counter, sleep

class Map:
    def __init__(self,
                grid_dim = (500,700),
                ):
        self.grid_dim = grid_dim
        self._t0 = None

    def get_time(self):
        return perf_counter() - self.t0

    @property
    def t0(self):
        if self._t0 is None:
            self._t0 = perf_counter()
        return self._t0
    
    def is_valid(self, pos, player_size):
        return (
            0 <= pos.y <= self.grid_dim[1]-player_size[1]
        )

    

if __name__ == '__main__':
    myMap = Map()
    for i in range(180):
        print(f"{i}: {myMap.get_time()}")
        sleep(1)