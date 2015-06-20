import random
import sys

seed = sys.argv[1]
random.seed(seed)
n = 60
m = 0

edge_prob = 10
negative_prob = 10

edges = {}

for i in range(n):
  edges[i] = {}
  for j in range(i + 1, n):
    if random.randint(0, edge_prob):
      edges[i][j] = random.randint(1, 2**30)
      if random.randint(0, negative_prob):
        edges[i][j] = -edges[i][j]
      m += 1

print n
print m
for i in range(n):
  for j, v, in edges[i].iteritems():
    print i, j, v
