import random
import numpy
i=0
r=[random.randint(0,100) for i in range(100)]
print(r)
type (r)
mean = numpy.mean(r)
median=numpy.median(r)
var=numpy.var(r)
sd=numpy.sqrt(r)
print("La moyenne est : " ,mean)
print("La médiane est : " ,median)
print("La variance est : " ,var)
print("L’écart type est : " ,sd)