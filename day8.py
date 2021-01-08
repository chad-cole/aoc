from aocd.models import Puzzle
data = Puzzle(year=2020, day=8).input_data

"""
    Infinite loop in Machine Code

    Puzzle input:
        List of 

    Strategy:
        - Parse the input into a list of tuples
            - we will traverse this list as a linked list with two pointers
            - slow pointer will move one step at a time and fast will move two
            - when they meet, we have found the loop and are guaranteed to be inside
            - find length of loop, k, then start from beginning, fast and slow move one and 
                fast is k ahead of slow, stop when they meet
            - the fast will be used to track accumulation
"""
from collections import defaultdict
import re

"""Small Example"""
#with open("short.txt", 'r') as f:
#    data = f.read().rstrip()

class cmd_iter:
    def __init__(self, ll, start=0, step=1):
        self.ptr = self.acc = 0
        self.ll = ll
        self.step = step
        for i in range(start):
            next(self)
        
    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.step):
            cmd, num = self.ll[self.ptr]
            if cmd == 'nop': self.ptr += 1
            elif cmd == 'jmp': self.ptr += num
            elif cmd == 'acc': self.ptr, self.acc = self.ptr+1, self.acc+num
        return self.ptr, self.acc

# Preprocessing the input
ll = [(cmd.lower(), int(num)) for cmd, num in 
        (line.split(' ') for line in data.split('\n'))]

k = 1 #start at 1 because 'next' in while below will take one extra
for (sp, _), (fp, _) in zip(slowit := cmd_iter(ll), cmd_iter(ll, step=2)):
    if sp == fp: #Get into the loop
        while next(slowit)[0] != sp: #Find length of loop, k
            k += 1
        break

acc = 0
##Start over with fast K ahead of slow
for (sp, _), (fp, fa) in zip(cmd_iter(ll), cmd_iter(ll, start=k)):
    if sp == fp: acc = fa; break

print(f'Accumulation at Loop Start: {acc}')


















