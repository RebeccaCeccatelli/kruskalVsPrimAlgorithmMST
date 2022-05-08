from UnionFindNode import UnionFindNode

class Set:
    def __init__(self, firstElement):
        self.list = [firstElement]
        self.representative = firstElement
        self.size = 1

    def addElement(self, element):
        self.list.append(element)
        element.setRepresentative(self.representative)
        self.size +=1

    def printSet(self):
        for x in self.list:
            print(x.value)
        print("repr: ", self.representative.value)
        print(self.size)
        print("----------------")
