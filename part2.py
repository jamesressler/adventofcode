#! /bin/python3

# dec3-2.py

def getCommons(rating, bit):
  j = 0
  isOne = 0
  isZero = 0
  while j < len(rating):
    if rating[j][bit] == '1':
      isOne += 1
    if rating[j][bit] == '0':
      isZero += 1
    j += 1

  if isOne > isZero:
    return 1

  if isZero > isOne:
    return 0

  if isOne == isZero:
    return 2

def pruneRating(rating, keep, bit, opp):
  j = 0
  length = len(rating)
  while j < length:
    if keep == 2:
      if rating[j][bit] == opp:
        rating.remove(rating[j])
        j -= 1
        length -= 1

    elif rating[j][bit] != str(keep):
      rating.remove(rating[j])
      j -= 1
      length -= 1

    j += 1

  return


# main

file = "input.txt"
# file = "sample-input.txt"

input = open(file, 'r')

oxygen = []
co2 = []

for i in input:
  oxygen.append(i)
  co2.append(i)

j = 0
length = len(oxygen[0])-1
while j < length:
  mostCommon = getCommons(oxygen, j)

  if len(oxygen) > 1:
    pruneRating(oxygen, mostCommon, j, '0')

  j += 1

j = 0
length = len(co2[0])-1
while j < length:
  mostCommon = getCommons(co2, j)
  
  if mostCommon == 1:
    leastCommon = 0
  if mostCommon == 0:
    leastCommon = 1
  if mostCommon == 2:
    leastCommon = 2

  if len(co2) > 1:
    pruneRating(co2, leastCommon, j, '1')

  j += 1

print(int(oxygen[0], 2) * int(co2[0], 2))

input.close()

exit()