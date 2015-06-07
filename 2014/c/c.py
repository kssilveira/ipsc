t = int(raw_input())

for _ in range(t):
  new_line = raw_input()
  n = int(raw_input())
  s = raw_input()
  seen = set()
  answer = []
  for x in s.split():
    v = int(x)
    if v not in seen:
      seen.add(v)
      answer.append(x)
  print ' '.join(answer)
