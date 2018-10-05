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

def friendlyGroup(array):
  return False

# Finds the biggest group of friends
# given an Adjacency Matrix implemented in
# an array with bitmap
def findMostFriendlyGroup(matrix):
  largestGroup = []
  for x in range(len(matrix), 0, -1):
    subset = []
    fillMatrixOfSubsets(subset, matrix, x)
    for sset in subset:
      friends = friendlyGroup(sset)
      if friends == True:
        largestGroup = sset.copy()
        break;
  return 0


community = open("comunidade.txt", 'r')

nodes = int(community.readline())
matrix = populateFromFile(community, nodes)

largestSubGroup = findMostFriendlyGroup(matrix)

