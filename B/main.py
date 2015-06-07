
r, s, m = 43, 22, 2 ** 32

class random(object):
    def __init__(self, seed):
        self.x = seed
        self.c_store = {}

    def c(self, i):
        if i not in self.c_store:
            if i >= 43 and self.x[i-s] - self.x[i-r] - self.c(i-1) < 0:
                self.c_store[i] = 1
            else:
                self.c_store[i] = 0
        return self.c_store[i]

    def rand(self, i):
        if i > len(self.x):
            self.rand(i-1)
        elif i < len(self.x) - 1:
            return self.x[i]
        else:
            self.x.append((self.x[i - s] - self.x[i - r] - self.c(i-1)) % m)
            return self.x[-1]


class testcase(object):
    def __init__(self, lines):
        self.len = int(lines[0])
        self.nmoves = int(lines[-2])
        self.moves = lines[-1]
        self.line = map(int, lines[1].split())
        self.random_obj = random(map(int, lines[2].split()))
        self.random_index = 43


    def random(self):
        res = self.random_obj.rand(self.random_index)
        self.random_index += 1
        return res

    def newtile(self):
        zeros = self.line.count(0)
        if not zeros:
            return False
        pos = self.random() % zeros
        if (self.random() % 10) == 0:
            new_value = 4
        else:
            new_value = 2
        cnt = 0
        for x in range(0,len(self.line)):
            if self.line[x] == 0:
                if cnt == pos:
                    self.line[x] = new_value
                cnt += 1
        return True


    def solve(self):
        for c in self.moves:
            effect = False
            if c == 'r':
                self.line = self.line[::-1]
            for pos in range(len(self.line)):
                if self.line[pos] != 0:
                    newpos = pos
                    while newpos > 0:
                        newpos -= 1
                        if self.line[newpos] != 0:
                            if self.line[newpos] == self.line[pos]:
                                self.line[newpos] = - 2 * self.line[pos]
                                self.line[pos] = 0
                                effect = True
                                break
                            else:
                                self.line[newpos + 1], self.line[pos] = self.line[pos], self.line[newpos + 1]
                                if newpos + 1 != pos:
                                    effect = True
                                    break
                        else:
                            if newpos == 0:
                                self.line[newpos], self.line[pos] = self.line[pos], self.line[newpos]
                                effect = True
                                break

            if c == 'r':
                self.line = self.line[::-1]


            for x in range(len(self.line)):
                self.line[x] = abs(self.line[x])
            if effect:
                if not self.newtile():
                    break
        return ' '.join(map(str, self.line))





with open('b1.in') as f:
    lines = f.read().splitlines()

tests = int(lines[0])
lines = lines[2:]
lines.append('')

testcases = []
cur_lines = []
for line in lines:
    if not line:
        testcases.append(testcase(cur_lines))
        cur_lines = []
    else:
        cur_lines.append(line)


with open('b.out', 'w') as f:
    for case in testcases:
        sol = case.solve()
        print sol
        f.write(sol)