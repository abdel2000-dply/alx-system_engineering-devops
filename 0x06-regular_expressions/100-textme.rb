#!/usr/bin/env ruby
# Advanced

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
