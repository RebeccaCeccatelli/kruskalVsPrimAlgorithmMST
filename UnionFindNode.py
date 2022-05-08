from Node import Node

class UnionFindNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.representative = self

    def setRepresentative(self, representative):
        self.representative = representative

    def printNode(self):
        print("value: ", self.value, "repr: ", self.representative.value)
