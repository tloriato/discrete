# Receives an incomplete adjacency matrix with a 
# bitmap representation and completes it
#def correlateMatrix(matrix):
  #for i in range(0, len(matrix)):
    # Goes through every row of matrix and check that
    # everything is right
  #return 0

# Receives a string of connections of a node and
# return the bitmap representation of it
# ex: "1,2,3" -> '0b1110' (14)
def createMask(str):
  mask = 0
  numArray = list(map(int, str.split(',').pop(0)))
  for i in numArray:
    mask = mask | (1 << i)
  return mask

matrix = []

community = open("comunidade.txt", 'r')
nodes = int(community.readline())
graphs = [[] * nodes for i in range(nodes)]

for i in range(0, nodes):
  a = list(map(int, community.readline().split(',')))
  a.pop(0)
  if len(a) == 0:
    break;
  graphs[i] = a
  for k in graphs[i]:
    graphs[k - 1].append(i)
  print(graphs[i])
print(graphs)



#for i in range(0, nodes):
 # matrix[i] = createMask(community.readline())

#matrix = correlateMatrix(matrix)
 
