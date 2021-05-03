def selectf(F, f):
    for ind, val in enumerate(f):
        if not val:
            return F[ind]
    return False


def chonDuoc(fs):
    pass


def checkDoiXung(fs):
    pass


def Bien_Quan_He(M, f):
    pass


def dim(fs):
    pass


def checkCon(S1, S2):
    pass


def solve(M, F, A, B):
    Sol = {}
    if B in A:
        return True
    else:
        sol_found = False

    f = [False for x in range(F)]
    while True:
        A_old = A

        fs = selectf(F, f)
        while not sol_found and chonDuoc(fs):
            if (checkDoiXung(fs) and 0 < len(Bien_Quan_He(M, fs) - A) and len(Bien_Quan_He(M, fs) - A) <= dim(fs)) or (not checkDoiXung(fs) and Bien_Quan_He(M, fs) - A != 0):
                A = A.union(Bien_Quan_He(M, fs))
                Sol = Sol.union(fs)
            if (checkCon(B, A)):
                sol_found = True
            fs = selectf(F, f)
        if sol_found or A == A_old:
            break

    return sol_found


class Obuject:
    value = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __init__(self, name) -> None:
        self.name = name

    def checkNone(self):
        return self.value == None

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __div___(self, other):
        return self.value / other.value

    def __str__(self):
        return str(self.value)


a = Obuject("a")
b = Obuject("b")
c = Obuject("c")
d = Obuject("d")
e = Obuject("e")
f = Obuject("f")

F = [
    {'e', 'a', 'b'},
    {'f', 'b', 'a'},
    {'c', 'a', 'b'},
    {'d', 'a', 'b'}
]

M = [a, b, c, d, e, f]


def f1(e, a, b):
    if e.checkNone():
        e.value = a / b
    if a.checkNone():
        a.value = e * b
    if b.checkNone():
        b.value = a / e
    return [e, a, b]


def f2(f, b, a):
    return f1(f, b, a)


def f3(c, a, b):
    if c.checkNone():
        c.value = a + b
    if a.checkNone():
        a.value = c - b
    if b.checkNone():
        b.value = c - a
    return [c, a, b]


def f4(d, a, b):
    if d.checkNone():
        d.value = a - b
    if a.checkNone():
        a.value = d + b
    if b.checkNone():
        b.value = a - d
    return [d, a, b]


a.value = 1
b.value = 2

A = [a, b]
B = [c]
