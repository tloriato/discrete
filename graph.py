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
  
# Finds the biggest group of friends
# given an Adjacency Matrix implemented in
# an array with bitmap
def findFriends(matrix):
  size = len(matrix)
  friends = []
  for i in range(size, 0, -1):
    temp = findFriendsOfN(matrix, i)
    if len(temp) > len(friends):
      friends = temp.copy()
  return friends

def findFriendsOfN(matrix, i):
  friends = []
  # do something #
  return friends


community = open("comunidade.txt", 'r')

nodes = int(community.readline())
matrix = populateFromFile(community, nodes)

largestSubGroup = findFriends(matrix)
