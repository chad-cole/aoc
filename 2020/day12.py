from aocd.models import Puzzle
data = Puzzle(year=2020, day=12).input_data

"""
    Day 12: Rain Risk 

    Puzzle input:
        - Set of Vectors for navigation

    Task 1:
        - Find the manhatten distance after following all of the instructions
    
    Task 2:

    Strategy (Part 1): 
        - Make a class to handle direction arithmetic and one to hold current data
    
    Strategy (Part 2): 
"""

with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

part1 = part2 = None

class direction:
    cardinal = ['E','S','W','N'] 

    def __init__(self, c='E', deg=0):
        self.current = c

    def __add__(self, moves):
        return direction(direction.cardinal[(int(self)+moves)%len(direction.cardinal)])

    def __int__(self):
        return direction.cardinal.index(self.current)

    def __str__(self):
        return f"{self.current}"
    
class vec_pair:
    def __init__(self, d='E', x=0, y=0, wx=10, wy=1, useway=False):
        self.dir = direction(d)
        self.pos = (x, y)
        self.way = (wx, wy)
        self.useway = useway

    def rotate(self, deg):
        if self.useway:
            for _ in range(abs(deg) // 90):
                if deg > 0: self.way = (self.way[1], -1*self.way[0])
                else: self.way = (-1*self.way[1], self.way[0])
        else: self.dir = self.dir + deg // 90
    
    @staticmethod
    def _parse_dir(d, m, x, y):
        if d == 'N': y += m
        if d == 'S': y -= m
        if d == 'E': x += m
        if d == 'W': x -= m
        return x, y

    def update(self, d, m):
        cd, x, y, wx, wy = self.dir, *self.pos, *self.way
        if self.useway:
            if d == 'F': 
                for _ in range(m):
                    x, y = x+wx, y+wy
            else: wx, wy = vec_pair._parse_dir(d, m, wx, wy)
        else:
            if d == 'F': d = cd.current
            x, y = vec_pair._parse_dir(d, m, x, y)
        self.pos = (x, y)
        self.way = (wx, wy)

    def __str__(self):
        return f"{self.dir}|{self.pos}|{(self.way if self.useway else None)}"

v = vec_pair()
v2 = vec_pair(useway=True)
for line in data.split('\n'):
    d, m = line[0], int(line[1:])
    if d in ('R','L'): 
        if d == 'R': 
            v.rotate(m)
            v2.rotate(m)
        else: 
            v.rotate(-m)
            v2.rotate(-m)
    else: 
        v.update(d, m)
        v2.update(d, m)

print(f"Part 1: v=({v}), d={sum(map(abs, v.pos))}")
print(f"Part 2: v=({v2}), d={sum(map(abs, v2.pos))}")

