
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
      test = "[%s]*[%s]" % (res[i], res[n / i])
      if len(test) < len(res[n]):
        # print "found", i, test
        res[n] = test

for i, s in res.iteritems():
  if len(s) > 75:
    print i, s  # 264
  # assert len(s) <= 75
  # print s
  # print "console.log(%s);" % s


