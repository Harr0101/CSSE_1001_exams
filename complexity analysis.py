import timeit
import random
import matplotlib
import matplotlib.pyplot

def reverse_and_remove(xs: list[int]) -> list[int]: 
    ans = [] 
    for k in range(len(xs)): 
        ans.append(xs[-k-1])     
    return [x for x in ans if x >= 0]

x=[]
y=[]

for i in range(1,25):
    list = [random.randint(-3,3) for j in range(i**4)]
    x.append(i**2)
    y.append(timeit.timeit(lambda: reverse_and_remove(list),number=100))
    print(i)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()