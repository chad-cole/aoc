from aocd.models import Puzzle
data = Puzzle(year=2020, day=9).input_data

"""
    Day 9: Encoding Error

    Puzzle input:
        List of numbers comprised of a preamble of 25 and then every number after is must be a sum of
        two of the previous 25

    Task 1:
        Find the first number in the list that is not a sum of the previous 25
    
    Task 2:
        Find a contiguous set that sums to the number found and return the sum of the smallest and the largest

    Strategy (Part 1): 
        - Keep an lru cache of the preamble size
        - check for sum for each item in the queue
    
    Strategy (Part 2): 
        - Use two pointers, advance the fast pointer until sum of window exceeds target, 
            advance slow pointer until sum of window is less than target
        - If on any movement, the sum == the target, return sum of min and max in window
"""
from collections import OrderedDict, deque
from itertools import islice

"""Part 1"""
preamble_size = 25
nums = iter(int(x) for x in data.split('\n'))
queue = OrderedDict({x: None for x in islice(nums, preamble_size)})

for part1 in nums:
    assert(len(queue) == preamble_size) #loop invariant
    if not any(part1-x in queue for x in queue): break
    queue.popitem(last=False)
    queue[part1] = None

print(f'First incorrect number: {part1}')

"""Part 2"""
nums = iter(int(x) for x in data.split('\n'))

window = deque(islice(nums, 2))
minn, maxn, ws = min(window), max(window), sum(window)

while ws != part1:
    if ws < part1: 
        n = next(nums)
        window.append(n)
        ws += n
    else: 
        ws -= window.popleft()

print(f'Part 2: {min(window) + max(window)}')
