require 'pry-byebug'
sample_input = <<-SAMPLE
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
SAMPLE

def pop_count(x)
  n = 0
  while x > 0
    x = x & (x - 1)
    n += 1
  end
  n
end

transform1 = -> (x) { x
  .map { |y| y.split('') }
  .transpose
  .map { |y| (pop_count(y.join('').to_i(2)) > x.length / 2 ? 1 : 0).to_s }
  .join('')
}

sample = sample_input.split("\n")
data = File.open('input.txt').readlines.map(&:chomp)

# Part 1: Find product of final horizantal and vertical distance
gamma = transform.call(data).to_i(2)
epsilon = gamma ^ ((1 << data.first.length) - 1)

puts("[Part 1] Gamma: #{gamma}")
puts("[Part 1] Epsilon: #{epsilon}")
puts("[Part 1] Power consumption: #{epsilon * gamma}")

# Part 2:
#puts("[Part 2] Product of distances: #{distances[:forward] * distances[:depth]}")

transform2 = -> (x) { x
  .map { |y| y.split('') }
  .transpose
  .map { |y| (pop_count(y.join('').to_i(2)) > x.length / 2 ? 1 : 0).to_s }
  .join('')
}
