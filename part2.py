#! /bin/python3

# part2.py

file = "input.txt"

input = open(file, 'r')

catch = 0

inlist = []

for i in input:
  inlist.append(int(i))

hold = 1000000000
i = 0

while i < len(inlist)-2:
  slide = inlist[i] + inlist[i+1] + inlist[i+2]
  if slide > hold:
    catch += 1
  hold = slide
  i += 1

print(catch)

input.close()

exit()