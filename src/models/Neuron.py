import random


class Neuron:
    def __init__(self, sigma: float, parents: list) -> None:
        self.sigma = sigma
        self.parents = parents
        self.bias = 0 if parents == None else round(random.uniform(-1, 1), 3)
        self.weight = round(random.uniform(-1, 1), 3)

    def compute_value(self) -> float:
        if self.parents is None:
            value = self.value
        else:
            value = self.bias
            for p in self.parents:
                # value += p.weight * p.compute_value()
                value = max(0, value + p.weight * p.compute_value())  # ReLu

        return value


if __name__ == "__main__":
    # Neurons init
    n1 = Neuron(1, None)
    n2 = Neuron(1, None)
    n3 = Neuron(1, [n1, n2])

    # Simulate inputs
    for i in range(3):
        n1.value = i
        n2.value = -i
        print(f"#####################################\n{i} | {-i}")
        print(f"{n1.weight}, {n2.weight}, {n3.bias}, {n3.compute_value()}")
