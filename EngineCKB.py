from copy import deepcopy


def selectf(F, f):
    for ind, val in enumerate(f):
        if not val:
            return F[ind]
    return False


def checkIn(B, A):
    for i in B:
        for j in A:
            if i == j:
                return True
    return False


def solve(M, F, A, B):
    Sol = []
    if checkIn(B, A):
        sol_found = True
    else:
        sol_found = False

    fs = [False for x in range(len(F))]
    while not sol_found:
        check = False
        for i, f in enumerate(F):
            if not fs[i] and f.checkFull(A):
                Sol.append(f)
                A = f.getListOutput(A)
                check = True
                break
        if checkIn(B, A):
            sol_found = True
        elif not check:
            sol_found = False
            break
    return (sol_found, Sol, A)


def checkCon(B, A):
    dem = 0
    for i in B:
        for j in A:
            if i == j:
                dem += 1
    return dem >= len(B)

    # print(OptSol)


class Object:
    value = None

    def __init__(self, name):
        self.name = name

    def checkNone(self):
        return self.value == None

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return str(self.value)


exp = []


def cong(a, b, c):
    global exp
    if a.checkNone():
        a.value = b + c
        exp.append(str(b.value) + " + " + str(c.value) + " = " + str(a.value))
    return [a, b, c]


def tru(a, b, c):
    global exp
    if a.checkNone():
        a.value = b - c
        exp.append(str(b.value) + " - " + str(c.value) + " = " + str(a.value))
    return [a, b, c]


def nhan(a, b, c):
    global exp
    if a.checkNone():
        a.value = b * c
        exp.append(str(b.value) + " * " + str(c.value) + " = " + str(a.value))
    return [a, b, c]


def chia(a, b, c):
    global exp
    if a.checkNone():
        a.value = b / c
        exp.append(str(b.value) + " / " + str(c.value) + " = " + str(a.value))
    return [a, b, c]


def re1(a, b, e):
    e, a, b = chia(e, a, b)
    a, e, b = nhan(a, e, b)
    b, a, e = chia(b, a, e)
    return (a, b, e)


def re2(a, b, f):
    return re1(b, a, f)


def re3(a, b, c):
    c, a, b = cong(c, a, b)
    a, c, b = tru(a, c, b)
    b, c, a = tru(b, c, a)
    return [c, a, b]


def re4(a, b, d):
    d, a, b = tru(d, a, b)
    a, d, b = cong(a, d, b)
    b, a, d = tru(b, a, d)
    return [d, a, b]


def re5(a, b, g):
    g, a, b = nhan(g, a, b)
    a, g, b = chia(a, g, b)
    b, g, a = chia(b, g, a)
    return [a, b, g]


class Function:
    name = None

    def __init__(self, u, name, func=None):
        self.func = func
        u.sort(key=lambda x: x.name)
        self.u = u
        self.name = name

    def getValue(self, v):
        v.sort(key=lambda x: x.name)
        param = []
        for i in v:
            for j in self.u:
                if i == j:
                    param.append(i)
                    break
        res = self.func(param[0], param[1], param[2])
        for i in res:
            for j in v:
                if i == j:
                    j.value = i.value
                    break
        return v

    def getListOutput(self, v):
        v.sort(key=lambda x: x.name)
        res = list(set(self.u).union(set(v)))
        res.sort(key=lambda x: x.name)
        return res

    def checkFull(self, v):
        v.sort(key=lambda x: x.name)
        dem = 0
        for i in v:
            for j in self.u:
                if i == j:
                    dem += 1
        return len(self.u) == dem + 1

    def __str__(self):
        return self.name


a = Object("a")
b = Object("b")
c = Object("c")
d = Object("d")
e = Object("e")
f = Object("f")
g = Object("g")

f1 = Function([a, b, e], "f1", re1)
f2 = Function([a, b, f], "f2", re2)
f3 = Function([a, b, c], "f3", re3)
f4 = Function([a, b, d], "f4", re4)
f5 = Function([a, b, g], "f5", re5)


F = [f1, f2, f3, f4, f5]

M = [a, b, c, d, e, f, g]


# for i in f3.getListOutput(A):
#     print(i.name)
# solve(M, F, A, B)
# res = solve(M, F, A, B)
# res = find_good_soltion(M, F, A, B, res[1])


# caculate(OptSol, M, exp)


class Engine:
    minDeep = 100000
    OptSol = []
    F = [f1, f2, f3, f4, f5]
    M = [a, b, c, d, e, f, g]
    IsSol = False

    def __init__(self, A, B):
        self.A = A
        self.B = B
        global exp
        self.exp = exp
        self.exp.clear()
        fs = [False for x in range(len(self.F))]
        self.find_good_soltion(self.B, fs, [], 0)
        self.OptSol.reverse()
        self.IsSol = len(self.OptSol) > 0
        self.caculate(A)

    def find_good_soltion(self, B, check, Sol, deep):

        if B == []:
            self.OptSol = Sol
            self.minDeep = deep
        if (checkCon(B, A)):
            if deep < self.minDeep:
                self.OptSol = Sol
                self.minDeep = deep

        for b in B:
            for i, f in enumerate(self.F):
                if not check[i] and checkIn([b], f.u):
                    bf = list(set(f.u) - (set([b])))
                    checkc = deepcopy(check)
                    checkc[i] = True
                    Solc = deepcopy(Sol)
                    Solc.append(f)
                    self.find_good_soltion(bf, checkc, Solc, deep + 1)

    def caculate(self, A):
        MM = deepcopy(M)
        for i in MM:
            for j in A:
                if i == j:
                    i.value = j.value
                    break
        for i in self.OptSol:
            MM = i.getValue(MM)


aa = Object('a')
bb = Object('c')
dd = Object('d')
aa.value = 1
bb.value = 6
A = [aa, bb]
B = [dd]
engine = Engine(A, B)
print(engine.exp)
