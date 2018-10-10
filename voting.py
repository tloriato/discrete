def calculateVotes(win, loo, maxd, sc=0):
  if (win, loo, maxd, sc) in hashTable:
    return hashTable[win, loo, maxd, sc]
  if win == 0 and loo == 0:
    return 1
  else:
    if loo == 0:
      hashTable[win, loo, maxd, sc] = 0 + calculateVotes(win - 1, loo, maxd, sc + 1)
    else:
      if sc + 1 < maxd and win > 0:
        hashTable[win, loo, maxd, sc] = calculateVotes(win - 1, loo, maxd, sc + 1) + calculateVotes(win, loo - 1, maxd, sc - 1)
      else:
        hashTable[win, loo, maxd, sc] = 0 + calculateVotes(win, loo - 1, maxd, sc - 1)
    return hashTable[win, loo, maxd, sc]

def generateVotes(win, loo, maxd, arr=[], sc=0):
  global outFile
  if win == 0 and loo == 0:
    outFile.write(''.join(arr) + '\n')
    return 1
  else:
    if loo == 0:
      return generateVotes(win - 1, loo, maxd, arr + ['W'], sc + 1)
    else:
      if sc + 1 < maxd and win > 0:
        return generateVotes(win - 1, loo, maxd, arr + ['W'], sc + 1) + generateVotes(win, loo - 1, maxd, arr + ['L'], sc - 1)
      else:
        return generateVotes(win, loo - 1, maxd, arr + ['L'], sc - 1)


## Interface Function ##
def voting (a, b, c):
  global outFile
  winnerVotes = b + ((a - b)/2)
  looserVotes = a - winnerVotes
  results = calculateVotes(winnerVotes, looserVotes, c)
  if results > 1000:
    outFile.write(str(results))
  else:
    generateVotes(winnerVotes, looserVotes, c)



## Main ##
hashTable = {} 
votes = open("voting.txt", 'r')

a = int(votes.readline())
b = int(votes.readline())
c = int(votes.readline())

votes.close()

outFile = open("voting-saida.txt", 'w')

x = voting(a, b, c)

outFile.close()

## End Main ##

## 70 20 30