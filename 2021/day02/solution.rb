data = File.open('input.txt').readlines.map(&:chomp).map(&:split)

# Part 1: Find product of final horizantal and vertical distance
distances = data.each_with_object(Hash.new(0)) { |(dir, dis), h| h[dir.to_sym] += dis.to_i }
horizantal = distances[:forward]
vertical = distances[:down] - distances[:up]

puts("[Part 1] Total horizantal distance: #{horizantal}")
puts("[Part 1] Total vertical distance: #{vertical}")
puts("[Part 1] Product of distances: #{horizantal * vertical}")

# Part 2:
distances = data.each_with_object(Hash.new(0)) do |(dir, dis), h|
  dir, dis = dir.to_sym, dis.to_i
  case dir
  when :up; h[:aim] -= dis
  when :down; h[:aim] += dis
  when :forward
    h[:forward] += dis
    h[:depth] += h[:aim] * dis
  end
end

puts("[Part 2] Total horizantal distance: #{distances[:forward]}")
puts("[Part 2] Total vertical distance: #{distances[:depth]}")
puts("[Part 2] Product of distances: #{distances[:forward] * distances[:depth]}")
