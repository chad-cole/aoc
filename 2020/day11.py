from aocd.models import Puzzle
data = Puzzle(year=2020, day=11).input_data

"""
    Day 11: Seating system

    Puzzle input:
        Grid of seats L = Empty, # = Filled, . = Floor
        - seating rules are: 
            - If seat is empty and all ajacent seats are empty, the seat is filled
            - If seat is full and four or more adjacent seats are full, the seat becomes empty
            - edges are empty
            - These rules apply simultaneously to all the seats

    Task 1:
        - Find the number of filled seats when, after continued application of the rules, no more flips occur
    
    Task 2:

    Strategy (Part 1): 
        - Make function to count empty adjacent seats
        - hold copy of board, can't do this inplace
        - iterate in row-major form applying the rules until the current board == previous
    
    Strategy (Part 2): 
        - Edit function to count empty paths
"""

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

part1 = [[c for c in line] for line in data.split('\n')]

from itertools import chain

"""Part 1"""

adjacent_pos = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1))
def empty_adjacent(board, pos):
    i, j = pos
    count = 0
    for r,c in ((i+di, j+dj) for di, dj in adjacent_pos):
        if r < 0 or r >= len(board): count += 1
        elif c < 0 or c >= len(board[0]): count += 1
        elif board[r][c] in {'L','.'}: count += 1
    return count

def next_board(current, adj=empty_adjacent, th_leave=4):
    nb = [[y for y in x] for x in current]
    for i in range(len(current)):
        for j in range(len(current[0])):
            empties = adj(current, (i,j))
            if current[i][j] == 'L' and empties == 8: nb[i][j] = '#'
            if current[i][j] == '#' and empties <= th_leave: nb[i][j] = 'L'
    return nb

while True:
    nb = next_board(part1)
    if nb == part1: break
    part1 = nb

print(f"Part 1: {sum(s == '#' for s in chain(*part1))}")

"""Part 2"""

part2 = [[c for c in line] for line in data.split('\n')]

def empty_path(board, pos):
    i, j = pos
    count = 0
    for di, dj in adjacent_pos:
        r, c = pos
        while True:
            r, c = r+di, c+dj
            if r < 0 or r >= len(board): count += 1; break
            if c < 0 or c >= len(board[0]): count += 1; break
            if board[r][c] == '.': continue
            else:
                if board[r][c] == 'L': count += 1
                break
    return count

while True:
    nb = next_board(part2, empty_path, 3)
    if nb == part2: break
    part2 = nb

print(f"Part 2: {sum(s == '#' for s in chain(*part2))}")
