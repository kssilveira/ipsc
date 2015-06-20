import os
import time

n_max = 0
n_max_seed = 0

for seed in range(0, 10000):
  os.system('python sol_d.py %s > %s.in' % (seed, seed))
  os.system('timeout 60 python d.py < %s.in > %s.out' % (seed, seed))
  with open('%s.out' % seed, 'r') as f:
    n = int(f.read())
    if n > n_max:
      n_max = n
      n_max_seed = seed
    print seed, n, 'max', n_max_seed, n_max
    if n >= 10000:
      import pdb; pdb.set_trace()
  time.sleep(0.01)
