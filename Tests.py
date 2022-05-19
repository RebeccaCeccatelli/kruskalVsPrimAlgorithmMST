import unittest

from timeit import default_timer as timer
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from Graph import Graph

class MyTestCase(unittest.TestCase):
    def testKruskal(self):
        matrix1 = [[0,10,12,0,0,0,0,0,0],[10,0,9,8,0,0,0,0,0],[12,9,0,0,3,1,0,0,0],[0,8,0,0,7,0,8,5,0],[0,0,3,7,0,3,0,0,0],[0,0,1,0,3,0,0,6,0],[0,0,0,8,0,0,0,9,2],[0,0,0,5,0,6,9,0,11],[0,0,0,0,0,0,2,11,0]]
        graph1 = Graph(9)
        graph1.setMatrix(matrix1)
        A = graph1.computeMSTWithKruskal()

        expectedA = [2,5,1,  6,8,2,  2,4,3,  3,7,5,  5,7,6,  1,3,8,  3,6,8,  0,1,10]
        i = 0
        for edge in A:
            self.assertEqual(edge.u,expectedA[i])
            i +=1
            self.assertEqual(edge.v,expectedA[i])
            i+=1
            self.assertEqual(edge.weight,expectedA[i])
            i+=1

        matrix2 = [[0,24,13,13,22],[24,0,22,13,13],[13,22,0,19,14],[13,13,19,0,19],[22,13,14,19,0]]
        graph2 = Graph(5)
        graph2.setMatrix(matrix2)
        A = graph2.computeMSTWithKruskal()

        expectedA = [0,2,13,  0,3,13,  1,3,13,  1,4,13]
        i = 0
        for edge in A:
            self.assertEqual(edge.u,expectedA[i])
            i +=1
            self.assertEqual(edge.v, expectedA[i])
            i +=1
            self.assertEqual(edge.weight,expectedA[i])
            i +=1

        matrix3 = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,0],[0,19,51,0,31],[0,42,0,31,0]]
        graph3 = Graph(5)
        graph3.setMatrix(matrix3)
        A = graph3.computeMSTWithKruskal()

        expectedA = [0,1,9,  1,3,19,  3,4,31,  2,3,51]
        i = 0
        for edge in A:
            self.assertEqual(edge.u,expectedA[i])
            i +=1
            self.assertEqual(edge.v,expectedA[i])
            i +=1
            self.assertEqual(edge.weight, expectedA[i])
            i +=1

    def testPrim(self):
        matrix1 = [[0,10,12,0,0,0,0,0,0],[10,0,9,8,0,0,0,0,0],[12,9,0,0,3,1,0,0,0],[0,8,0,0,7,0,8,5,0],[0,0,3,7,0,3,0,0,0],[0,0,1,0,3,0,0,6,0],[0,0,0,8,0,0,0,9,2],[0,0,0,5,0,6,9,0,11],[0,0,0,0,0,0,2,11,0]]
        graph1 = Graph(9)
        graph1.setMatrix(matrix1)
        A = graph1.computeMSTWithPrim(1)

        expectedA = [0,1,10,  1,3,8,  3,7,5,  7,5,6,  5,2,1,  5,4,3,  3,6,8,  6,8,2]
        i = 0
        for edge in A:
            self.assertEqual(edge.u.value,expectedA[i])
            i +=1
            self.assertEqual(edge.v.value,expectedA[i])
            i+=1
            self.assertEqual(edge.weight,expectedA[i])
            i+=1

        matrix2 = [[0,24,13,13,22],[24,0,22,13,13],[13,22,0,19,14],[13,13,19,0,19],[22,13,14,19,0]]
        graph2 = Graph(5)
        graph2.setMatrix(matrix2)
        A = graph2.computeMSTWithPrim(2)

        expectedA = [1,3,13,  1,4,13,  3,0,13,  0,2,13]
        i = 0
        for node in A:
            self.assertEqual(node.u.value,expectedA[i])
            i +=1
            self.assertEqual(node.v.value, expectedA[i])
            i +=1
            self.assertEqual(node.weight,expectedA[i])
            i +=1

        matrix3 = [[0,9,75,0,0],[9,0,95,19,42],[75,95,0,51,0],[0,19,51,0,31],[0,42,0,31,0]]
        graph3 = Graph(5)
        graph3.setMatrix(matrix3)
        A = graph3.computeMSTWithPrim(3)

        expectedA = [2,3,51,  3,1,19,  1,0,9,  3,4,31]
        i = 0
        for node in A:
            self.assertEqual(node.u.value,expectedA[i])
            i +=1
            self.assertEqual(node.v.value,expectedA[i])
            i +=1
            self.assertEqual(node.weight, expectedA[i])
            i +=1

    def testSameMSTWeight(self):
        V = 20
        probability = 60/100
        graph = Graph.generateConnectedGraph(V,probability)

        A, weightWithKruskal = graph.computeMSTWithKruskal()
        A, weightWithPrim = graph.computeMSTWithPrim(1)

        self.assertEqual(weightWithKruskal,weightWithPrim)

    def testComplexityIncreasingV(self):
        fixedProbability = 80/100
        maxV = 40
        V = np.arange(1,maxV,1)

        kruskalComplexity = [0]*len(V)
        primComplexity = [0]*len(V)

        totExperiments = 10
        for experiment in range (0,totExperiments,1):
            for v in V:
                index = np.where(V == v)[0][0]

                graph = Graph.generateConnectedGraph(v,fixedProbability)

                startKruskal = timer()
                graph.computeMSTWithKruskal()
                endKruskal = timer()
                startPrim = timer()
                graph.computeMSTWithPrim(1)
                endPrim = timer()

                kruskalComplexity[index] += endKruskal-startKruskal
                primComplexity[index] += endPrim - startPrim

        for value in kruskalComplexity:
            value /= totExperiments
        for value in primComplexity:
            value /= totExperiments

        plt.plot(V,kruskalComplexity,'r',V,primComplexity,'g')
        plt.title("Comparison between Kruskal's and Prim's time complexity, with fixed probability and increasing V")
        plt.xlabel("V (number of nodes)")
        plt.ylabel("seconds")
        redPatch = mpatches.Patch(color = 'red', label = "Kruskal's Algorithm for MST")
        greenPatch = mpatches.Patch(color = 'green', label = "Prim's Algorithm for MST")
        plt.legend(handles = [redPatch, greenPatch])
        plt.show()

    def testComplexityIncreasingProbability(self):
        fixedV = 20
        minProbability = 10
        maxProbability = 100
        probabilities = np.arange(minProbability,maxProbability,5)

        kruskalComplexity = [0]*len(probabilities)
        primComplexity = [0]*len(probabilities)

        totExperiments = 10
        for experiment in range(0,totExperiments,1):
            for p in probabilities:
                index = np.where(probabilities == p)[0][0]

                graph = Graph.generateConnectedGraph(fixedV,p/100)

                startKruskal = timer()
                graph.computeMSTWithKruskal()
                endKruskal = timer()
                startPrim = timer()
                graph.computeMSTWithPrim(1)
                endPrim = timer()

                kruskalComplexity[index] += endKruskal-startKruskal
                primComplexity[index] += endPrim-startPrim

        for value in kruskalComplexity:
            value /= totExperiments
        for value in primComplexity:
            value /= totExperiments

        plt.plot(probabilities,kruskalComplexity,'r',probabilities,primComplexity,'g')
        plt.title("Comparison between Kruskal's and Prim's time complexity, with increasing probability and fixed V")
        plt.xlabel("probability (out of 100)")
        plt.ylabel("seconds")
        redPatch = mpatches.Patch(color = 'red', label = "Kruskal's Algorithm for MST")
        greenPatch = mpatches.Patch(color = 'green', label = "Prim's Algorithm for MST")
        plt.legend(handles = [redPatch, greenPatch])
        plt.show()


if __name__ == '__main__':
    unittest.main()
