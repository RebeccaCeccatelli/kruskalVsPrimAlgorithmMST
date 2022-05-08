from UnionFindNode import UnionFindNode
from MinHeapNode import MinHeapNode
from UnionFind import UnionFind
from Edge import Edge
from MinHeap import MinHeap

import numpy as np
from numpy import random

class Graph:
    def __init__(self, V):
        self.V = V
        self.nodes = []
        self.edges = []
        self.matrix = np.zeros((V,V))

        for value in range(0,V,1):
            self.nodes.append(MinHeapNode(value))

    @staticmethod
    def generateRandomGraph(V, probability):
        graph = Graph(V)

        for i in range(0,V,1):
            for j in range (0,V,1):
                if j > i:
                    n = random.randint(1,100)
                    if n <= probability*100:
                        weight = random.randint(1,100)
                        graph.matrix[i][j] = weight
                        graph.matrix[j][i] = weight
                        graph.edges.append(Edge(i,j,weight))
        return graph

    def isConnected(self):
        connected = False

        unionFind = UnionFind()
        for node in self.nodes:
            unionFind.makeSet(node)

        for i in range (0,self.V, 1):
            for j in range (0, self.V, 1):
                if self.matrix[i][j] != 0:
                    x = unionFind.findNodeWithValue(i)
                    y = unionFind.findNodeWithValue(j)
                    if unionFind.findSet(x) != unionFind.findSet(y):
                        unionFind.union(x,y)

        if len(unionFind.S) == 1:
            connected = True
        return connected


    def printMatrix(self):
        print(self.matrix)
        #for node in self.nodes:
        #    print(node.value, node.representative.value)

    def setMatrix(self, matrix):
        self.matrix = [[0,10,12,0,0,0,0,0,0],[10,0,9,8,0,0,0,0,0],[12,9,0,0,3,1,0,0,0],[0,8,0,0,7,0,8,5,0],[0,0,3,7,0,3,0,0,0],[0,0,1,0,3,0,0,6,0],[0,0,0,8,0,0,0,9,2],[0,0,0,5,0,6,9,0,11],[0,0,0,0,0,0,2,11,0]]
        for i in range (0,self.V,1):
            for j in range(0,self.V,1):
                if self.matrix[i][j] !=0:
                    self.edges.append(Edge(i,j,self.matrix[i][j]))

    def setMatrix2(self):
        self.matrix = [[0,24,13,13,22],[24,0,22,13,13],[13,22,0,19,14],[13,13,19,0,19],[22,13,14,19,0]]
        for i in range(0,self.V,1):
            for j in range(0,self.V,1):
                if self.matrix[i][j] != 0:
                    self.edges.append(Edge(i,j,self.matrix[i][j]))

    def setMatrix3(self):
        self.matrix = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,0],[0,19,51,0,31],[0,42,0,31,0]]
        for i in range(0,self.V,1):
            for j in range(0,self.V,1):
                if self.matrix[i][j] != 0:
                    self.edges.append(Edge(i,j,self.matrix[i][j]))

    def computeMSTWithKruskal(self):  #testato, funziona
        A = []
        unionFind = UnionFind()
        for node in self.nodes:
            unionFind.makeSet(node)
        self.edges.sort(key=lambda x: x.weight)

        unions = 0
        for edge in self.edges:
            if unions <= self.V-1:
                u = unionFind.findNodeWithValue(edge.u)
                v = unionFind.findNodeWithValue(edge.v)
                if unionFind.findSet(u) != unionFind.findSet(v):
                    A.append(edge)
                    unionFind.union(u, v)
                    unions +=1
            else:
                break

        return A

    def computeMSTWithPrim(self, rootIndex):
        minHeap = MinHeap()
        for node in self.nodes:
            minHeap.insert(node)
        minHeap.decreaseKey(rootIndex,0)

        while len(minHeap.A)!=1:
            u = minHeap.extractMin()
            for j in range(0,self.V,1):
                weight = self.matrix[u.value][j]
                if weight != 0:
                    found, v = minHeap.stillContains(j)
                    if found and weight < v.key:
                        v.pigreco = u
                        minHeap.decreaseKey(minHeap.getIndex(v.value),weight)
        #capire cosa dare in output qui
