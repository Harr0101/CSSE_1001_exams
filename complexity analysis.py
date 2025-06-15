import timeit
import random
import matplotlib
import matplotlib.pyplot

def partition(values: list[int]) -> tuple[int, int, int]: 
    positives = 0 
    zeros = 0 
    negatives = 0 
    for value in values: 
        if value == 0: 
            zeros += 1 
        elif value > 0: 
            positives += 1 
        else: 
            negatives += 1 
    return (positives, zeros, negatives)
xs=[]
ys=[]

for i in range(1,50):
    x = i**3
    list = [random.randint(-3,3) for j in range(x)]
    xs.append(x)
    ys.append(timeit.timeit(lambda: partition(list),number=100))
    print(i)

matplotlib.pyplot.plot(xs,ys)
matplotlib.pyplot.show()