from aocd.models import Puzzle
data = Puzzle(year=2020, day=18).input_data

"""
    Day 18: Operation Order

    Puzzle input:
        - List of expressions consisting of addition and multiplication operations 

    Task 1:
        - Multiplication and addition have the same precidence in this system - what is the sum of the results of the expressions
    
    Task 2:
        - Addition has higher precidence than multiplication in this system - what is the sum of the results of the expressions

    Strategy (Part 1): 
        - Make a number class where I override addition to perform multiplication and subtraction to perform addition
            - The reason for doing this is because I can't override precidence 
        - let eval take care of it
    
    Strategy (Part 2): 
        - Make a number class where I override division to perform addition
"""

"""
Parse the Input Data
"""

class aoc_num:
    def __init__(self, val):
        self.val = val

    def __add__(self, x):
        return aoc_num(x.val*self.val)
    
    def __sub__(self, x):
        return aoc_num(x.val+self.val)
    
    def __neg__(self, x):
        return aoc_num(-self.val)
    
    def __truediv__(self, x):
        return aoc_num(x.val+self.val)
    
    def __int__(self):
        return self.val

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

"""
Part 1
"""
import re

part1 = 0

for line in data.split('\n'):
    line = line.replace('+', '-').replace('*', '+')
    line = re.sub(r'(\d+)',r'aoc_num(\1)', line)
    part1 += eval(line).val

print(f"Part 1: {part1}")

"""
Part 2
"""

part2 = 0

for line in data.split('\n'):
    line = line.replace('+', '/').replace('*', '+')
    line = re.sub(r'(\d+)',r'aoc_num(\1)', line)
    part2 += eval(line).val

print(f"Part 2: {part2}")
