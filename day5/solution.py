from aocd.models import Puzzle
data = Puzzle(year=2020, day=5).input_data

data = data.replace('B','1').replace('F','0')
data = data.replace('R','1').replace('L','0')

min_seat, max_seat = float('inf'), float('-inf')
sum_seat = 0
for line in data.split():
    row, seat = int(line[:-3], 2), int(line[-3:], 2)
    sid = row*8+seat
    max_seat = max(max_seat, sid)
    min_seat = min(min_seat, sid)
    sum_seat += sid

my_seat = (max_seat-min_seat+1)*(max_seat+min_seat)//2 - sum_seat

print(f'max seat: {max_seat}; sum {sum_seat}; mine {my_seat}')
