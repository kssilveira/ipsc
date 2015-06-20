
res = {}
res[0] = "+![]"
res[1] = "+!![]"
res[2] = "!![]+!![]"

for i in range(2, 10):
  res[i] = res[i - 1] + res[1]

for n in range(10, 1001):
  s = str(n)
  res[n] = ""
  for d in s:
    if res[n]:
      res[n] += "+"
    res[n] += "[" + res[int(d)] + "]"
  res[n] += "-[]"

for i, s in res.iteritems():
  if len(s) > 75:
    print i, s
  # assert len(s) <= 75
  # print s
  # print "console.log(%s);" % s
