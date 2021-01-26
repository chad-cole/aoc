from aocd.models import Puzzle
data = Puzzle(year=2020, day=15).input_data

"""
    Day 15: Rambunctious Recitation (https://adventofcode.com/2020/day/15)

    Puzzle input:
        - Part 1
            - Sequence of starting numbers
        - Part 2

    Task 1:
        - Sequence is created by saying the distance from the current number to the last time it was seen
            or saying 0 if it hasn't been seen
        - return 2020th value of the sequence
    
    Task 2:
        - return 2020th value of the sequence

    Strategy (Part 1): 
        - use a dictionary encoding numbers with their latest turn
    
    Strategy (Part 2): 
        - return the 30,000,000th value
        
"""

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

def find_n(data, goal):
    data = [int(x) for x in data.split(',')]
    turns = {v:i for i,v in enumerate(data[:-1], 1)}
    t, c = len(data)+1, data[-1]

    while t <= goal:
        n = t-turns[c]-1 if c in turns else 0
        turns[c], c, t = t-1, n, t+1
    return c

print(f"Part 1: {find_n(data, 2020)}")
print(f"Part 2: {find_n(data, 30000000)}")
