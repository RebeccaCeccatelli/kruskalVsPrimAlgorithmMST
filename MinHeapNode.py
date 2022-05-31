from UnionFindNode import UnionFindNode

#inherits from UnionFindfNode because its attributes are needed to compute graph's connectivity (see in method Graph::isConnected())
class MinHeapNode(UnionFindNode):

    def __init__(self, value, key=10000):
        super().__init__(value)
        self.key = key      #added attributes
        self.pigreco = None

