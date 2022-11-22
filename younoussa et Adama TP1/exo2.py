from ast import FunctionDef
import random
class DataTrans:
    def __init__(self, n, s):
        self.n = n
        self.s = s
        
    
    def liste(self):
        D=[]
        for x in range(self.n):
            l=[random.randint(0,100) for x in range(self.s)]
            D.append(l)
        return D

    def listMin(self, d):
        minList = []
        for l in d:
            minValue = l[0]
            for x in l[1:]:
                if x < minValue:
                    minValue = x
            minList.append(minValue)
        return minList

    def listMax(self, g):
        maxList = []
        for k in g:
            maxValue = k[0]
            for x in k[1:]:
                if x > maxValue:
                    maxValue = x
            maxList.append(maxValue)
        return maxList

    def minGlobal(self, v):
        for i in v:
            miValue = v[0]
            for x in v[1:]:
                if x < miValue:
                    miValue = x
            return miValue
    
    def maxGlobal(self, p):
        for i in p:
            maValue = p[0]
            for x in p[1:]:
                if x > maValue:
                    maValue = x
            return maValue

    def fonction(x):
        return (x**3 + 3*(x**2) - 5)

    def calcul_D(self,h):
        for i in range(len(h)):
            for j in range(len(h[i])):
                t = h[i][j]
                print("Pour x = ",t, "on a : ", self.fonction(t))
    