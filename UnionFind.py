from UnionFindSet import Set

class UnionFind:
    def __init__(self):
        self.S = []

    def makeSet(self, x):
        Si = Set(x)
        self.S.append(Si)

    def findSet(self, x):
        representative = None
        for Si in self.S:
            if x in Si.list:
                representative = Si.representative
                break
        return representative

    def union(self, x, y):
        setx = self.findSi(x)
        sety = self.findSi(y)

        toBeRemoved = setx
        toBeExtended = sety
        if sety.size < setx.size:
            toBeRemoved = sety
            toBeExtended = setx
        for element in toBeRemoved.list:
            toBeExtended.addElement(element)
        self.S.remove(toBeRemoved)

    def findSi(self, x):
        set = None
        for Si in self.S:
            if x in Si.list:
                set = Si
                break
        return set

    def findNodeWithValue(self, value):
        x = None
        for Si in self.S:
            for node in Si.list:
                if node.value == value:
                    x = node
                    break

        return x
