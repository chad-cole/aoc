from aocd.models import Puzzle
data = Puzzle(year=2020, day=10).input_data

"""
    Day 10: Adapter Array

    Puzzle input:
        List of numbers representing Joltage for your various power adapters.

    Task 1:
        Order them in a chain where all will be used and then return the number of 
        1 Jolt increases times the number of 3 Jolt increases
    
    Task 2:
        Calculate number of valid orderings for the adapters in the bag

    Strategy (Part 1): 
        Sort the input then iterate over the list counting the differences from
        current and prevous. Last one will always be a difference of 3
    
    Strategy (Part 2): 
        Create an adjacency list for next moves
        Create a recursive count function that counts leaves and memoize it
"""

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import tee

import operator

"""Part 1"""

def pairwise(i):
    a, b = tee(i)
    next(b, None)
    return zip(a, b)

data = [0] + sorted(int(x) for x in data.split('\n'))
data.append(data[-1]+3)
counts = Counter(p-c for c,p in pairwise(data))

print(f"Part 1: {(counts[1])*(counts[3])}")

"""Part 2"""

graph = defaultdict(tuple)
for x in reversed(data):
    graph[x] = tuple(x+i for i in range(1,4) if x+i in graph)

@lru_cache()
def count_ways(node):
    if not graph[node]: return 1
    return sum(count_ways(x) for x in graph[node])

print(f"Part 2: {count_ways(0)}")
