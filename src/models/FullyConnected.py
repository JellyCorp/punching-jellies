import random

from .Neuron import Neuron
import json


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
    print(net)
