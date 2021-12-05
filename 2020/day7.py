from aocd.models import Puzzle
data = Puzzle(year=2020, day=7).input_data

"""
    Rules of Baggage

    Puzzle input:
        List of rules of the form X contains W, X, Y where each variable is a type of bag
        This list of rules determines a graph of possible containment for the bags, but the bag of interest 
            is the shiny gold bag
    Output 1: Number of bags at the top level which can contain the shiny gold bag

    Strategy:
        - Parse the input into an adjacency list
            - Remove all words with bag from the input, plural and singular
            - split on contain and then comma
            - load into dictionary
        - Use a DFS to find which of the starting nodes lead to shiny gold
"""
from collections import defaultdict
import re

graph = defaultdict(set)

# Preprocessing the input
for line in data.split('\n'):
    line = line.replace('bags', 'bag').replace('bag', '').replace('.','').replace(' no ', ' 0 ')
    container, contained = map(str.strip, line.split('contain'))
    for bag in map(str.strip, contained.split(',')):
        count, name = re.match(r'(\d+)\s([\w\s]+)', bag).groups()
        if name == 'other': graph[container]
        else: graph[container].add((name, int(count)))

#DFS for question 1
goldies = set()

def dfs(name, parent=None):
    if parent == None: parent = name
    if name == 'shiny gold':
        goldies.add(parent)
        return
    for neighbor, count in graph[name]:
        dfs(neighbor, parent)

for bag in (x for x in graph if x != 'shiny gold'):
    dfs(bag)

"""Recursively traverse the Graph and Sum the Counts and Multipliers"""
def get_count(name, multiplier=1):
    if not graph[name]: return multiplier
    sub_count = sum(get_count(x,y) for x,y in graph[name])
    return multiplier * (1 + sub_count)

print(f'Number of bags that can contain a Shiny Gold bag: {len(goldies)}')
print(f'Number of bags inside a Shiny Gold bag: {get_count("shiny gold")-1}')
