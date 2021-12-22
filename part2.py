#! /bin/python3

# part2.py

class card():
  numbers = []
  hits = []
  won = 0
  
  def __init__(self):
    self.numbers = []
    self.hits = [
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]
    self.won = 0
  
  def checkWin(self):
    i = 0
    while i < len(self.hits[0]):
      catch = 0
      j = 0
      while j < len(self.hits):
        if self.hits[j][i] == 1:
          catch += 1
        j += 1

      if catch == 5 and self.won == 0:
        self.won = 1
        return 1

      i += 1
      
    i = 0
    while i < len(self.hits):
      catch = 0
      j = 0
      while j < len(self.hits[i]):
        if self.hits[i][j] == 1:
          catch += 1
        j += 1
      if catch == 5 and self.won == 0:
        self.won = 1
        return 1

      i += 1
    return 0

def getCards(cards, input):
  newCard = card()
  for line in input:
    if line != "\n":
      newCard.numbers.append(line.split())

    else:
      cards.append(newCard)
      newCard = card()

  cards.append(newCard)
  return

def playBingo(cards, number):
  # read in a number and check for a win
  i = 0
  while i < len(cards):
    j= 0
    while j < len(cards[i].numbers):
      k = 0
      while k < len(cards[i].numbers[j]):
        if cards[i].numbers[j][k] == number:
          cards[i].hits[j][k] = 1
        k += 1
      j += 1
    i += 1
    
  i = 0
  while i < len(cards):
    if cards[i].checkWin() == 1:
      score = getScore(cards[i], number)
      print("WINNER!!!! Card %(i)i wins with a score of %(score)i" % {"i": i+1, "score": score})
      # print(number)
      # return score
    i += 1

  return 0

def getScore(card, lastNumber):
  # calculate the score of a winning card
  score = 0
  j= 0
  while j < len(card.numbers):
    k = 0
    while k < len(card.numbers[j]):
      if card.hits[j][k] == 0:
        score += int(card.numbers[j][k])
      k += 1
    j += 1
  return score * int(lastNumber)

file = "input.txt"
# file = "sample-input.txt"

with open(file, 'r') as input:
  numberPool = input.readline().split(',')
  input.readline()

  cards = []
  getCards(cards, input)

i = 0
remainingCards = len(cards)-1
while i < len(numberPool):
  if playBingo(cards, numberPool[i]) > 0:
    if remainingCards == 0:
      break
    remainingCards -= 1
  i += 1

# i = 0
# while i < len(cards):
#   print("card %i" % i, " has 'won' set to ", cards[i].won)
#   i += 1

# print(cards[53].numbers)
# print(cards[53].hits)
# print(getScore(cards[53], 93))

exit()