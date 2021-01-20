from aocd.models import Puzzle
data = Puzzle(year=2020, day=14).input_data

"""
    Day 14: Docking Data (https://adventofcode.com/2020/day/14)

    Puzzle input:
        - Part 1
            - 36 bit mask (x's mean to do nothing, 1 or 0 are controlling)
            - List of assignments to memory where the mask is applied to each write 
        - Part 2
            - 36 bit mask (x's mean to do both, 1 is controlling, 0 means to do nothing)
            - List of assignments to memory where the mask is applied to each address

    Task 1:
        - Sum of final values in memory if memory is initiallized to 0
    
    Task 2:
        - Sum of final values in memory if memory is initiallized to 0

    Strategy (Part 1): 
        - make two masks, an 'or' mask and an 'and' mask so that we can perform bitwise arithmetic
    
    Strategy (Part 2): 
        - get permutaions of masks - then for each mask, or it with the address and write the data
"""

class mask_iter:
    def __init__(self, lines):
        self.iter = iter(lines)
        self.mask = next(self.iter)

    def __iter__(self):
        return self

    def __next__(self):
        mask, writes = self.mask, []
        if not self.iter: raise StopIteration
        try:
            current = next(self.iter)
            while not current.startswith('mask'):
                writes.append(current)
                current = next(self.iter)
            mask, self.mask = self.mask, current
            return mask, writes
        except: StopIteration
        self.iter = None
        return mask, writes

def get_permutations(mask):
    if len(mask) == 1: return ['0','1'] if mask == 'X' else [mask]
    else:
        output = []
        for p in get_permutations(mask[1:]):
            if mask[0] != 'X': output.append(mask[0]+p) 
            else: output.extend(['0'+p, '1'+p])
        return output

import re

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

mem = dict()
for mask, writes in mask_iter(data.split('\n')):
    andmask = int(mask.replace('mask = ','').replace('X', '1'),base=2)
    ormask = int(mask.replace('mask = ','').replace('X', '0'),base=2)
    for write in writes:
        addr, val = map(int, re.match(r'mem\[(\d+)\]\s=\s(\d+)', write).groups())
        mem[addr] = (val & andmask) | ormask

part1 = sum(mem.values())

'Part 2'

mem = dict()
for mask, writes in mask_iter(data.split('\n')):
    x_mask = mask.replace('mask = ', '').replace('1','0')
    masks = get_permutations(mask.replace('mask = ',''))
    for mp in map(lambda x: int(x, base=2), masks):
        andmask = int(x_mask.replace('0','1').replace('X','0'), base=2)
        for write in writes:
            addr, val = map(int, re.match(r'mem\[(\d+)\]\s=\s(\d+)', write).groups())
            mem[(addr | mp) & (andmask | mp)] = val

part2 = sum(mem.values())

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

