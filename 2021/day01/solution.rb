data = File.open('input.txt').readlines.map(&:chomp).map(&:to_i)

def count_increases(data)
  data.each_cons(2).count { |p, c| p < c }
end

# Part 1: count pairwise increases
puts("Total number of increases: #{count_increases(data)}")

# Part 2: count pairwise sliding-window of 3 sums increases
window_sums = data.each_cons(3).map { |window| window.reduce(&:+) }
puts("Total number of window increases: #{count_increases(window_sums)}")

# Turns out there is an insight (thanks @lugray) since two of the values will always
# be in consecutive sums, you can always compare the first number of each window to
# tell which will be larger
puts("Total number of window increases: #{data.each_cons(4).count { |a, _, _, b| a < b } }")

