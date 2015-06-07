f = open('/home/kaue/Desktop/l1.pcm', 'rb')
s = f.read()
print 'len', len(s)

for start in range(1000):
  for n in range(4000, 10000):
    middle = start + n
    end = middle + n
    if s[start:middle] == s[middle:end]:
      print start, n
