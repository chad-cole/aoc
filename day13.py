from aocd.models import Puzzle
data = Puzzle(year=2020, day=13).input_data

"""
    Day 13: Shuttle Search

    Puzzle input:
        - Note about the earliest time you think you could depart
        - Notes about bus schedules where the number of the bus denotes
            the recurrence in minutes of their arrival e.g. bus 7 comes every seven minutes

    Task 1:
        - Find the number of the earliest bus you could take multiplied by the number of minutes you have to wait
    
    Task 2:

    Strategy (Part 1): 
        - Use modulo to find the right bus
    
    Strategy (Part 2): 
        - Chinese Remainder Theorem
"""

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

data = data.split('\n')
start, buses = int(data[0]), data[1] 
bus, mintime = None, float('inf')
for b in (int(x) for x in buses.split(',') if x != 'x'):
    time = start + (b - start%b)
    if time < mintime: bus, mintime = b, time

part1 = (mintime - start)*bus

'Part 2'

from functools import reduce

#Create list of remainders and moduli for the Chinese remainder theorem
crt_input = list((-i, int(x)) for i,x in enumerate(buses.split(',')) if x != 'x')

def chinese_remainder_theorem(r1, n1, r2, n2):
    x, y = pow(n1, -1, n2), pow(n2, -1, n1) #Calculate Modular Inverses
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m, m

part2, _ = reduce(lambda x,y: chinese_remainder_theorem(*x,*y), crt_input)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

