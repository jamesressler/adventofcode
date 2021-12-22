#! /bin/python3

# part2.py

file = "input.txt"
# file = "sample-input.txt"

input = open(file, 'r')

aim = 0
horiz = 0
depth = 0

inlist = []

for i in input:
  inlist.append(i)

j = 0
while j < len(inlist):
  temp = inlist[j].split()
  if temp[0] == 'up':
    aim -= int(temp[1])
  if temp[0] == 'down':
    aim += int(temp[1])
  if temp[0] == 'forward':
    horiz += int(temp[1])
    depth += aim * int(temp[1])
  j += 1

print(horiz * depth)

exit()