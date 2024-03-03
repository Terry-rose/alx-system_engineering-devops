#!/usr/bin/env ruby

log_file_path = ARGV[0]

File.open(log_file_path, 'r') do |file|
  file.each_line do |line|
    match_data = line.match(/\[from:(\S+?)\] \[to:(\S+?)\] \[flags:(.*?)\]/)
    if match_data
      sender = match_data[1]
      receiver = match_data[2]
      flags = match_data[3]
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end

