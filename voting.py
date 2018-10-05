def iVoting(win, loo, maxd, sc=0):
  if (win, loo, maxd, sc) in hashTable:
    return hashTable[win, loo, maxd, sc]
  if win == 0 and loo == 0:
    return 1
  else:
    if loo == 0:
      hashTable[win, loo, maxd, sc] = 0 + iVoting(win - 1, loo, maxd, sc + 1)
    else:
      if sc + 1 < maxd and win > 0:
        hashTable[win, loo, maxd, sc] = iVoting(win - 1, loo, maxd, sc + 1) + iVoting(win, loo - 1, maxd, sc - 1)
      else:
        hashTable[win, loo, maxd, sc] = 0 + iVoting(win, loo - 1, maxd, sc - 1)
    return hashTable[win, loo, maxd, sc]

def voting (a, b, c):
  winnerVotes = b + ((a - b)/2)
  looserVotes = a - winnerVotes
  maxDifference = c
  if not winnerVotes.is_integer() or not looserVotes.is_integer() or c <= b:
      raise ValueError('Wrong parameters!')
  return iVoting(winnerVotes, looserVotes, maxDifference)

## Main ##
hashTable = {} 
votes = open("voting.txt", 'r')

a = int(votes.readline())
b = int(votes.readline())
c = int(votes.readline())

votes.close()

out = open("voting-saida.txt", 'w')

x = voting(a, b, c)

print(a, b, c)
print(x)

out.close()

#print("Testando voting(70, 20, 30) :D")
#print(voting(70,20,30))
