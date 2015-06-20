s = "7ialnjpbjd..RED"
d = "Pythagoras"

res = ""

for i in range(10):
  res += chr(((ord(d[i]) - ord(s[i])) + 256) % 256)
  assert chr(((ord(d[i]) - ord(res[i])) + 256) % 256) == s[i]

print res
print [x.encode('hex') for x in res]
