import numpy as np
from numpy import random

from MinHeapNode import MinHeapNode
from UnionFind import UnionFind
from Edge import Edge
from MinHeap import MinHeap


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

    @staticmethod
    def generateConnectedGraph(V,probability):
        foundConnected = False
        graph = None
        while foundConnected is False:
            graph = Graph.generateRandomGraph(V,probability)
            if graph.isConnected():
                foundConnected = True
        return graph


    def setMatrix(self,matrix):
        self.matrix = matrix
        for i in range(0,self.V,1):
            for j in range(0,self.V,1):
                if self.matrix[i][j] != 0:
                    self.edges.append(Edge(i,j,self.matrix[i][j]))

    def computeMSTWithKruskal(self):
        A = []
        totalWeight = 0
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
                    totalWeight += edge.weight
                    unionFind.union(u, v)
                    unions +=1
            else:
                break

        return A,totalWeight

    def computeMSTWithPrim(self, rootIndex):
        A = []
        totalWeight = 0
        minHeap = MinHeap()

        for node in self.nodes:
            minHeap.insert(node)
        minHeap.decreaseKey(rootIndex,1)
        sizeAfterFirstExtraction = len(minHeap.A)-1

        while len(minHeap.A) !=1:
            u = minHeap.extractMin()

            if len(minHeap.A) != sizeAfterFirstExtraction:
                A.append(Edge(u.pigreco,u,u.key))
                totalWeight += u.key

            for j in range(0,self.V,1):
                weight = self.matrix[u.value][j]
                if weight != 0:
                    found, v = minHeap.stillContains(j)
                    if found and weight < v.key:
                        v.pigreco = u
                        minHeap.decreaseKey(minHeap.getIndex(v.value),weight)

        return A,totalWeight
