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

        for value in range(0,V,1):      #nodes are not named A,B,C,... but 1,2,...,V for semplicity
            self.nodes.append(MinHeapNode(value))       #nodes are of type MinHeapNode: it contains all the other types of node

    @staticmethod       #called by another static method
    def generateRandomGraph(V, probability):
        graph = Graph(V)

        for i in range(0,V,1):
            for j in range (0,V,1):
                if j > i:       #upper right part of the matrix: non-oriented graph, simmetry with diagonal
                    n = random.randint(1,100)       #probability of edge existence
                    if n <= probability*100:
                        weight = random.randint(1,100)      #random weight
                        graph.matrix[i][j] = weight
                        graph.matrix[j][i] = weight
                        graph.edges.append(Edge(i,j,weight))        #appends the new edge to the list of edges
        return graph

    def isConnected(self):      #the check relies on UnionFind data structure
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
    def generateConnectedGraph(V,probability):      #calls helper method 'generateRandomGraph()'
        foundConnected = False
        graph = None
        while foundConnected is False:
            graph = Graph.generateRandomGraph(V,probability)
            if graph.isConnected():
                foundConnected = True
        return graph

    def computeMSTWithKruskal(self):
        A = []
        totalWeight = 0
        unionFind = UnionFind()

        for node in self.nodes:
            unionFind.makeSet(node)
        self.edges.sort(key=lambda x: x.weight)     #non-decrescent order

        unions = 0
        for edge in self.edges:
            if unions <= self.V-1:      #stops after (V-1) unions
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
        sizeAfterFirstExtraction = len(minHeap.A)-1     #variable needed to handle the case of the root

        while len(minHeap.A) !=1:
            u = minHeap.extractMin()

            if len(minHeap.A) != sizeAfterFirstExtraction:      #if u is the root passes through
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

    def setMatrix(self,matrix):     #helper method called in some Tests
        self.matrix = matrix
        for i in range(0,self.V,1):
            for j in range(0,self.V,1):
                if self.matrix[i][j] != 0:
                    self.edges.append(Edge(i,j,self.matrix[i][j]))
