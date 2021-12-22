#! /bin/python3

# part1.py

file = "input.txt"
# file = "sample-input.txt"

input = open(file, 'r')

inlist = []

for i in input:
  inlist.append(i)

isOne = 0
isZero = 0

gamma = []
epsilon = []

j = 0
k = 0
while k < len(inlist[0])-1:
  while j < len(inlist):
    if inlist[j][k] == '1':
      isOne += 1
      # print("isOne:  ", isOne, "  bit: ", k, "  entry: ", j)
    if inlist[j][k] == '0':
      isZero += 1
      # print("isZero: ", isZero, "  bit: ", k, "  entry: ", j)
    j += 1

  if isOne > isZero:
    gamma.append('1')
    epsilon.append('0')

  elif isZero > isOne:
    gamma.append('0')
    epsilon.append('1')

  j = 0
  isOne = 0
  isZero = 0
  k += 1

# print(inlist)
# print(gamma, ' ', epsilon )

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

# print(gamma, ' ', epsilon )

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

# print(gamma, ' ', epsilon )

print(gamma * epsilon)

input.close()

exit()