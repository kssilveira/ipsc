t = int(raw_input())

# print 't', t

for _ in range(t):
  line = raw_input()
  p = raw_input()
  q = raw_input()
  # print 'p', p, 'q', q
  answer = ''
  for i in range(min(len(p), len(q))):
    if p[i] != q[i]:
      answer = '<' * (len(q) - i)
      answer += p[i:]
      break
  else:
    if len(q) > len(p):
      answer = '<' * (len(q) - len(p))
    else:
      answer = p[len(q):]
  answer += '*'
  other = '*' + p + '*'
  # print 'answer', answer, 'other', other
  if len(answer) < len(other):
    print answer
  else:
    print other
