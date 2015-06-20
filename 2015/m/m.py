import sys

res = {}
res[0] = "+[]"
res[1] = "+!![]"
res[2] = "!![]+!![]"
res[3] = "!![]+!![]+!![]"
res[4] = "!![]+!![]+!![]+!![]"
res[5] = "!![]+!![]+!![]+!![]+!![]"
res[6] = "[!![]+!![]]*[!![]+!![]+!![]]"
res[7] = "[!![]+!![]]*[!![]+!![]+!![]]+!![]"
res[8] = "[!![]+!![]]*[!![]+!![]]*[!![]+!![]]"
res[9] = "[!![]+!![]+!![]]*[!![]+!![]+!![]]"

# for i in range(2, 10):
  # res[i] = res[i - 1] + res[1]

def smaller(x):
  if x.endswith('-[]'):
    res = x[:-len('-[]')]
    # print 'returning', x, res
    return res
  return x

for n in range(10, 1001):
  s = str(n)
  res[n] = ""
  for d in s:
    if res[n]:
      res[n] += "+"
    res[n] += "[" + res[int(d)] + "]"
  res[n] += "-[]"
  for i in range(2, n/2 + 1):
    if n % i == 0:
      test = "[%s]*[%s]" % (smaller(res[i]), smaller(res[n / i]))
      if len(test) < len(res[n]):
        # print "found", i, test
        res[n] = test
  for i in range(1, n - 0):
    if not res[n - i].endswith('-[]'):
      right = res[n - i]
      if right.startswith('+'):
        right = right[1:]
      test = "%s+%s" % (((res[i])), (right))
      if len(test) < len(res[n]):
        # print "found", i, test
        res[n] = test

for n in range(10, 1001):
  for i in range(n + 1, 1001):
    if not res[i - n].endswith('-[]'):
      right = res[i - n]
      # if right.startswith('+'):
        # right = right[1:]
      test = "%s-[%s]" % (((res[i])), (right))
      if len(test) < len(res[n]):
        # print "found", i, test
        res[n] = test

for i, s in res.iteritems():
  if len(s) > 75:
    sys.stderr.write("%s, %s\n" % (i, s))
    # print i, s  # 264, 235, 45, 44, 8
  # assert len(s) <= 75
  # print s
  print "console.log(%s);" % s
