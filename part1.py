#! /bin/python3

# dec1-1.py

file = "puzzle-inputs/input-dec1.txt"

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