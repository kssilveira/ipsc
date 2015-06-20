t = int(raw_input())

for _ in range(t):
  new_line = raw_input()
  s = raw_input()
  s = ''.join(sorted(s, reverse=True))
  # print s
  print long(s[:-1]) + long(s[-1])
