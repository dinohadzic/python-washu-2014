import random
from merge_sort import *
from bubble_sort import *
import timeit
import pylab as py
import sys

def sorttime(n,iter):
    bubble_time = []
    merge_time = []
    for k in range(iter):
        test = random.sample(range(n),n)
        time1 = timeit.default_timer()
        bubble_sort(test)
        time2 = timeit.default_timer()
        merge_sort(test)
        time3 = timeit.default_timer()   
        bubble_time.append(time2 - time1)
        merge_time.append(time3 - time2)
    return sum(bubble_time)/len(bubble_time), sum(merge_time)/len(merge_time) #returns the means

random.seed(1379) #So that graph can be reproduced.

bubble_time = []
merge_time = []
n = 500
for i in range(2,n):
    times = sorttime(i,20)
    bubble_time.append(times[0])
    merge_time.append(times[1])

py.rcParams['legend.loc'] = 'best'
def fig(x1,y1,x2,y2,label1,label2):
    py.plot(x1, y1, label = label1)
    py.plot(x2, y2, label = label2)
    py.ylabel('Average Sorting Time (seconds)')
    py.xlabel('Size of Unsorted Input')
    py.legend()

fig(range(2,n), bubble_time, range(2,n), merge_time, 'Bubble', 'Merge')
py.savefig('sort_graph.png')