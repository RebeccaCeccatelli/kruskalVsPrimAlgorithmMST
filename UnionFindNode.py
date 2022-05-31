from Node import Node

class UnionFindNode(Node):      #node for UnionFind: inherits from Node
    def __init__(self, value):
        super().__init__(value)
        self.representative = self      #added attribute

    def setRepresentative(self, representative):
        self.representative = representative

