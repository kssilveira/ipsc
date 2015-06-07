import sys

result = {}
index = -1

def solve(s):
  global result

  # print 'in', s in result
  if s in result:
    return result[s]

  # the_len = len(result)
  # if the_len % 100000 == 0:
    # print index, the_len

  found_one = False
  leading_zeroes = 0
  total_ones = 0
  for i in range(len(s)):
    if s[i] == '1':
      if not found_one:
        leading_zeroes = i
        found_one = True
      total_ones += 1

  # print '0, 1:', leading_zeroes, total_ones

  if leading_zeroes + 1 >= total_ones:
    res = bool(total_ones % 2)
    result[s] = res
    return res

  if total_ones == 0:
    res = False
    result[s] = res
    return res

  for i in range(len(s)):
    if s[i] == '1':
      if i == 0:
        t = s[1:]
      else:
        t = s[1:i] + '0' + s[(i + 1):]
      if not solve(t):
        res = True
        result[s] = res
        return res

  res = False
  result[s] = res
  return res

if False:
  for n in range(5):
    for i in range(2 ** n):
      binary = bin(i)[2:]
      s = '0' * (n - len(binary)) + binary
      # print 'solving', s
      res = solve(s)
      print s, 'a' if res else 'b'

t = int(raw_input())

for index in range(t):
  new_line = raw_input()
  n = int(raw_input())
  s = raw_input()
  assert n == len(s)
  # sys.stderr.write('%s/%s\n' % (index, t))
  # sys.stderr.flush()
  res = solve(s)
  print 'Adam' if res else 'Betka'
