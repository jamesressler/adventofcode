#! /bin/python3

# part1.py

file = "input.txt"

input = open(file, 'r')

catch = 0

last = 1000000000000

for i in input:
  current = int(i)
  if current > last:
    catch += 1
  last = current

print(catch)

input.close()

exit()