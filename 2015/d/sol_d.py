import random
import sys

seed = sys.argv[1]
random.seed(seed)
n = 60
m = 0

edge_prob = random.randint(1, 1000000)

edges = {}

for i in range(n):
  edges[i] = {}
  for j in range(i + 1, n):
    if random.randint(0, edge_prob):
      edges[i][j] = random.randint(-(2**31), (2**31) - 1)
      m += 1

print n
print m
for i in range(n):
  for j, v, in edges[i].iteritems():
    print i, j, v
