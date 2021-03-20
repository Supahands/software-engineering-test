require 'yaml'
require 'date'
require 'set'
PYNAME = 'seed.py'.freeze
python_output = `python3 #{PYNAME}`

end_date = nil
difference = 0

timestamps = Set.new

# Let's parse and convert input into set so we get constant search time
# and no repeating dates
YAML.safe_load(python_output).each do |timestamp|
  timestamps.add(Date.parse(timestamp))
end

timestamps.each do |date|
  # Don't calcuate when previous date is already in the set
  # means we already calulated the difference
  next if timestamps.include?(date - 1)

  current_date = date
  current_difference = 1

  # Let's keep increasing the date until the gap is not 1 day
  while timestamps.include?(current_date + 1)
    current_date += 1
    current_difference += 1
  end

  # Pick the global or local max
  difference = [difference, current_difference].max

  # only set when local max is picked
  end_date = current_date if difference == current_difference
end

# Logic to prin the output
puts '---------------------------------------------'
puts '|    START    |     END    |     LENGTH     |'
puts '---------------------------------------------'
puts "| #{end_date - difference + 1}  | #{end_date} |       #{difference}        |"
puts '---------------------------------------------'
