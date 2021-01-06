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
        - Because we are looking for the shiny gold bag, reverse the direction of the graph so it shows 
            'is contained by' rather than 'contains'. This should give us some performance gain as we can 
            start from the shiny gold bag and work toward the container bags
        - Use a BFS to get to all the leaf nodes
        - Becareful of cycles
"""

