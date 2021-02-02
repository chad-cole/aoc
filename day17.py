from aocd.models import Puzzle
data = Puzzle(year=2020, day=17).input_data

"""
    Day 17: Conway Cubes

    Puzzle input:
        - 2-D slice of a 3D (4D for part 2) space with # for active and . for inactive points
        - Rules at every cycle are
            - if inactive and 3 neighbors are active, become active
            - if active and 2 or 3 neighbors are active, stay active, else go inactive

    Task 1:
        - count number of active points after 6 cycles
    
    Task 2:
        - expand to 4 dimensions

    Strategy (Part 1): 
        - state changes are simultaneous -> duplicate data
        - keep set of coordinates that are active
            - check every neighbor of every coordinate in planes of active + 1 on either side, if active, add to count
            - check restrictions for remaining / becomming active
    
    Strategy (Part 2): 
"""

"""
Parse the Input Data
"""
from itertools import product

def conway(active, dimensions, cycles):
    delta = (-1, 0, 1)
    for _ in range(cycles):
        new = set()
        for coord_set in product(*map(lambda x: range(min(x)-1, max(x)+2), zip(*active))):
            count = 0
            for delta_set in product(delta, repeat=dimensions):
                if any(x != 0 for x in delta_set):
                    if tuple(x + dx for x,dx in zip(coord_set, delta_set)) in active:
                        count += 1

            if ((coord_set not in active and count == 3) or (coord_set in active and count in (2, 3))):
                    new.add(coord_set)
        active = new
    return len(active)

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass
data = data.split('\n')

active = set((r,c,0) for r,l in enumerate(data) for c,p in enumerate(l) if p == '#')
print(f'Part 1: {conway(active, 3, 6)}')

active = set((r,c,0,0) for r,l in enumerate(data) for c,p in enumerate(l) if p == '#')
print(f'Part 2: {conway(active, 4, 6)}')
