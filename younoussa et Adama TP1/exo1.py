import math
class Resolution:
    def __init__(self, N):
        self.N=N
        self.L=list(range(-self.N, self.N+1))
        
    def f(self, x):
        return x/(x**2 + 1)
    
    def g(self, x):
        return math.atan(x)
    
    def liste(N):
        L=list(range(-N,N+1))
        return L
    
    def calcul(self):
        print(self.L)
        return sum([pow(( (x/(x**2 + 1)) - (math.atan(x)) ), 2) for x in self.L])

              
