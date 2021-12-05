from aocd.models import Puzzle
data = Puzzle(year=2020, day=8).input_data

"""
    Infinite loop in Machine Code

    Puzzle input:
        List of op codes and arguments, 

    Task 1:
        There is a loop in the opcodes. Find the value of the accumulation at the 
        start of the loop
    
    Task 2:
        Either change one nop to a jmp or a jmp to a nop to make the program terminate
        return the value of the accumulator when program terminates

    Strategy (Part 1): O(n) time, O(1) space
        - Parse the input into a list of tuples
            - we will traverse this list as a linked list with two pointers
            - slow pointer will move one step at a time and fast will move two
            - when they meet, we have found the loop and are guaranteed to be inside
            - find length of loop, k, then start from beginning, fast and slow move one and 
                fast is k ahead of slow, stop when they meet
            - the fast will be used to track accumulation
    
    Strategy (Part 2):
        - Brute force:
            - for every nop or jmp encountered, swap it and try to find a loop
                if there is not a loop return the acc value
                
"""

class opit:
    def __init__(self, ll, start=0, step=1):
        self.ptr = self.acc = 0
        self.ll = ll
        self.step = step
        for i in range(start):
            next(self)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr < 0 or self.ptr >= len(self.ll): raise StopIteration
        for i in range(self.step):
            cmd, num = self.ll[self.ptr]
            if cmd == 'nop': self.ptr += 1
            elif cmd == 'jmp': self.ptr += num
            elif cmd == 'acc': self.ptr, self.acc = self.ptr+1, self.acc+num
        return self.ptr, self.acc

# Preprocessing the input
ll = [(cmd.lower(), int(num)) for cmd, num in 
        (line.split(' ') for line in data.split('\n'))]

"""PART 1"""
k = 1 #start at 1 because 'next' in while below will take one extra
for (sp, _), (fp, _) in zip(slowit := opit(ll), opit(ll, step=2)):
    if sp == fp: #Get into the loop
        while next(slowit)[0] != sp: #Find length of loop, k
            k += 1
        break
##Start over with fast K ahead of slow
for (sp, _), (fp, acc) in zip(opit(ll), opit(ll, start=k)):
    if sp == fp: break
print(f'Accumulation at Loop Start: {acc}')

"""PART 2"""
for i, (cmd, arg) in enumerate(ll): #Go through whole list
    if cmd in {'jmp', 'nop'}: #Swap if swapable
        ll_aug = [x for x in ll]
        if cmd == 'jmp': ll_aug[i] = ('nop', arg)
        else: ll_aug[i] = ('jmp', arg)
        #Detect Loop
        for (sp, _), (fp, _) in zip(opit(ll_aug), opit(ll_aug, step=2)):
            if sp == fp: break
        else: #If no loop then we have our answer
            for _, acc in opit(ll_aug):
                pass
            break
print(f'Accumulation at End of Opcodes: {acc}')
