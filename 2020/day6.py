from aocd.models import Puzzle
data = Puzzle(year=2020, day=6).input_data

"""
    Puzzle input:
        Groups of letters separated by a blank line
    Output 1: Sum of the unique letters in each group
    Output 1: Sum of the letters which are present in every line of each group
"""

from itertools import chain
from functools import reduce

uniques = 0
intersections = 0
for group in data.split('\n\n'):
    group_data = set(chain(*group.split()))
    intersection = reduce(lambda x,y: x.intersection(y), (set(chain(*line)) for line in group.split()))
    uniques += len(group_data)
    intersections += len(intersection)

print(f'Sum of unique Answers: {uniques}, Intersection = {intersections}')
