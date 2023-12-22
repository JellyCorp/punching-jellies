import random
from copy import deepcopy
import json

from .Neuron import Neuron


class FullyConnected:
    def __init__(self, structure: list) -> None:
        self.structure = structure
        self.network = []
        for layer_index, layer_count in enumerate(structure):
            layer = []
            for _ in range(layer_count):
                if layer_index == 0:
                    layer.append(Neuron(1, None))
                else:
                    layer.append(Neuron(1, self.network[layer_index - 1]))
            self.network.append(layer)

    def __call__(self, inputs: list):
        assert len(inputs) == len(self.network[0])

        for n, input in zip(self.network[0], inputs):
            n.value = input

        outputs = []
        for n in self.network[len(self.network) - 1]:
            outputs.append(n.compute_value())

        return outputs

    def __repr__(self):
        to_print = ""
        for i, layer in enumerate(self.network):
            to_print += f"Biases {i}: {[n.bias for n in layer]}\t"
            to_print += f"Weights {i}: {[n.weight for n in layer]}\n"

        return to_print

    @classmethod
    def load_model(cls, path: str):
        # Computing network structure
        structure = []

        with open(path) as json_file:
            data = json.load(json_file)

            for key in data.keys():
                structure.append(len(data[key]))
            print(structure)

        # Create a network object
        instance = cls(structure)

        # Load weights
        instance._load_weights(path=path)

        return instance

    def mutate(self, sigma: float = 0.5):
        for layer_index, layer in enumerate(self.network):
            for n in layer:
                if layer_index != 0:
                    n.bias = round(random.gauss(mu=n.bias, sigma=sigma), 3)
                    n.weight = round(random.gauss(mu=n.weight, sigma=sigma), 3)
                else:
                    n.weight = round(random.gauss(mu=n.weight, sigma=sigma), 3)

        return self

    def cross_breed(self, breeding_mate, sigma: int = 0.5):
        assert isinstance(breeding_mate, FullyConnected)

        child1 = FullyConnected(self.structure)
        child2 = FullyConnected(self.structure)

        for layer_index, (
            layer_self,
            layer_mate,
            layer_child1,
            layer_child2,
        ) in enumerate(
            zip(self.network, breeding_mate.network, child1.network, child2.network)
        ):
            for n_self, n_mate, n_child1, n_child2 in zip(
                layer_self, layer_mate, layer_child1, layer_child2
            ):
                if layer_index != 0:
                    n_child1.bias = round(
                        random.gauss(mu=(n_self.bias + n_mate.bias) / 2, sigma=sigma), 3
                    )
                    n_child1.weight = round(
                        random.gauss(
                            mu=(n_self.weight + n_mate.weight) / 2, sigma=sigma
                        ),
                        3,
                    )
                    n_child2.bias = round(
                        random.gauss(mu=(n_self.bias + n_mate.bias) / 2, sigma=sigma), 3
                    )
                    n_child2.weight = round(
                        random.gauss(
                            mu=(n_self.weight + n_mate.weight) / 2, sigma=sigma
                        ),
                        3,
                    )
                else:
                    n_child1.weight = round(
                        random.gauss(
                            mu=(n_self.weight + n_mate.weight) / 2, sigma=sigma
                        ),
                        3,
                    )
                    n_child2.weight = round(
                        random.gauss(
                            mu=(n_self.weight + n_mate.weight) / 2, sigma=sigma
                        ),
                        3,
                    )

        return child1, child2

    def _load_weights(self, path: str):
        with open(path) as json_file:
            data = json.load(json_file)

        for key, layer in zip(data.keys(), self.network):
            for n_saved, n in zip(data[key], layer):
                n.weight, n.bias = n_saved[0], n_saved[1]

    def save_model(self, path):
        dict_network = {}
        for i, layer in enumerate(self.network):
            list_layer = []
            for n in layer:
                # print((n.weight, n.bias))
                list_layer.append((n.weight, n.bias))
            dict_network[f"{i}"] = list_layer

        with open(path, "w") as outfile:
            json.dump(dict_network, outfile)


if __name__ == "__main__":
    net = FullyConnected.load_model(path="./models_data/network_structure.json")
    print(net([-1, -1]))
    net2 = deepcopy(net)
    net2.mutate()
    print(net2)
    child1, child2 = net.cross_breed(net2, sigma=0.05)

    print(child1)
    print(child2)
