from aocd.models import Puzzle
data = Puzzle(year=2020, day=16).input_data

"""
    Day 16: Ticket Translation (https://adventofcode.com/2020/day/16)

    Puzzle input:
        3 chunks of data: 
            - rules which consist of field name and two ranges of allowable values (variable length)
            - values of unknown field names for your ticket
            - values of unknown field names for other tickets (variable length)

    Task 1:
        Find sum of the numbers in the fields of the alternate tickets that are not allowed 
    
    Task 2:
        Find product of numbers in my ticket whose field starts with 'departure'

    Strategy (Part 1): 
        - Interval Tree for the rules?
            - For this challenge, separation of fields is not important 
            - Interval Tree would allow me to store the field names in the leaves
        - Sort and Merge Intervals for rules?
            - Might have to re-work for the second challenge

        - In either case, I then have to iterate through the alternate values and sum

        - Let's try the interval tree (using pypy IntervalTree)
            - Invariant of the tree is that each node holds a min and max for an interval
                to the left are intervals that start lower than current, and to the right are intervals 
                that end higer than current
            - What about subsets? 
                - store third pointer to subset 
            - Data in each node is the name of the field that created the interval
    
    Strategy (Part 2): 
        - Clean out the invalid alternate tickets as determined by part 1
        - Go through the alternate tickets column-wise and use set intersection to find possible fields
        - Sort the resulting sets by length, keeping track of their position
        - Iterate through the list removing, by set subtraction, any taken field names, loop invariant is that the 
            current_set - taken_set will always yield one element := the field name 
        - return the product in your ticket using the new field names
        
"""

from functools import reduce
from itertools import chain, count
from intervaltree import IntervalTree

"""
Parse the Input Data
"""
with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

inttree = IntervalTree()

rules, mine, alts = data.split('\n\n')
for rule in rules.split('\n'):
    field, bounds = map(str.strip, rule.split(':'))
    for bound in map(str.strip, bounds.split('or')):
        mn, mx = map(int, map(str.strip, bound.split('-')))
        inttree[mn:mx+1] = field

alts = [[int(x) for x in alt.split(',')] for alt in alts.split('\n')[1:]]
mine = [[int(x) for x in alt.split(',')] for alt in mine.split('\n')[1:]]

"""
Part 1
"""

part1 = sum(x for x in chain.from_iterable(alts) if not inttree[x])
print(f"Part 1: {part1}")

"""
Part 2
    - Clean out the invalid alternate tickets as determined by part 1
    - Go through the alternate tickets column-wise and use set intersection to find possible fields
    - Sort the resulting sets by length, keeping track of their position
    - Iterate through the list removing, by set subtraction, any taken field names, loop invariant is that the 
        current_set - taken_set will always yield one element := the field name 
    - return the product in your ticket using the new field names
"""

alts_clean = [x for x in alts+mine if all(inttree[y] for y in x)]
field_names = [set.intersection(*[set(x.data for x in inttree[x[i]]) for x in alts_clean]) for i in range(len(alts[0]))]
sorted_counted = sorted(zip(field_names, count()), key=lambda x: len(x[0]))
 

taken, fields = set(), dict()
for s, i in sorted_counted:
    key = (s-taken).pop()
    fields[key] = i
    taken.add(key)

part2 = reduce(lambda x,y: x*y, (mine[0][y] for x,y in fields.items() if 'departure' in x))
print(f"Part 2: {part2}")
