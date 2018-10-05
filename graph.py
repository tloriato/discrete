# Receives an array of connections and
# return the bitmap representation of it
# ex: [1,2] -> '0b11'
def createMask(arr):
  mask = 0
  for i in arr:
    mask = mask | (1 << (i + 1))
  return mask

# Populate an Adjacency "Matrix" in bitmap
# from the provided file
# Returns: Array[i] = X
#   where X = Int that represents the 
#   bitmap of connections of the i-th node
def populateFromFile(file, nodes):
  graph = [[] * nodes for i in range(nodes)]
  matrix = [[] * nodes for i in range(nodes)]
  for i in range(0, nodes):
    numArray = list(map(lambda x: x - 1, map(int, community.readline().split(','))))[1:]
    if len(graph[i]) == 0:
      graph[i] = numArray
    elif len(numArray) > 0:
      graph[i] = sorted(graph[i] + list(set(numArray) - set(graph[i])))
    for k in graph[i]:
      if len(graph[k]) == 0:
        graph[k] = [i]
      else:
        graph[k] = sorted(graph[k] + list(set([i]) - set(graph[k])))
  for i in range(nodes):
    matrix[i] = createMask(graph[i])
  return matrix

# Receives an empty matrix and fills it 
# with the combinations of count of the list element
# i.e: list = [1,2,3] and count = 2 ->
#      matrix = [[1,2], [1,3], [2,3]]
def fillMatrixOfSubsets(matrix, list, count, prefix=[]):
  if count == 0:
    matrix.append(prefix)
    return
  else:
    for x in range(len(list)):
      fillMatrixOfSubsets(matrix, list[x+1:], count - 1, prefix + [list[x]])

# Implementation of the Math.ceil(n) function,
# that rounds up the number to the next integer
def ceil(a,b):
  return int(a/b + (a%b!=0))

# Finds if the elements in matrix with those indexes
# satisfy the condition that they must be
# friends with at least half of them
def friendlyGroup(indexes, matrix):
  bound = ceil(len(indexes), 2)
  for x in indexes:
    elem = matrix[x]
    rest = indexes[:x] + indexes[x+1 :]
    connections = 0
    for i in rest:
      if connections >= bound:
        break
      if elem & (0 | (1 << (i + 1))):
        connections += 1
    if connections < bound:
      return False
  return True

# Finds the biggest group of friends
# given an Adjacency Matrix implemented in
# an array with bitmap
def findMostFriendlyGroup(matrix):
  largestGroup = []
  for x in range(len(matrix), 0, -1):
    subset = []
    fillMatrixOfSubsets(subset, list(range(0, len(matrix))), x)
    for sset in subset:
      friends = friendlyGroup(sset, matrix)
      if friends == True:
        largestGroup = sset.copy()
        return largestGroup
  return largestGroup


community = open("comunidade.txt", 'r')

nodes = int(community.readline())
matrix = populateFromFile(community, nodes)

largestSubGroup = findMostFriendlyGroup(matrix)

# map(+1) because we start counting from 0 instead of 1
print(list(map(lambda x: x + 1, largestSubGroup)))
