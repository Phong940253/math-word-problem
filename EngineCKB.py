# -*- coding: utf-8 -*-
from copy import deepcopy
from pyvi import ViTokenizer, ViPosTagger
import string
import re


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
        if (checkCon(B, self.A)):
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


# aa = Object('a')
# bb = Object('c')
# dd = Object('d')
# aa.value = 1
# bb.value = 6
# A = [aa, bb]
# B = [dd]
# engine = Engine(A, B)
# print(engine.exp)
# text = u"Đàn gà có 15 gà trống, số gà mái gấp 4 lần số gà trống. Hỏi đàn gà có tất cả bao nhiêu con?"
# posts = ViPosTagger.postagging(ViTokenizer.tokenize(text))
# print(posts)

# NP = set()


def tach(text):
    res = []
    str = ""
    for i, v in enumerate(text):

        if v == "." or v == ",":
            res.append(str.strip())
            str = ""
        else:
            str += v
    if (str != ""):
        res.append(str.strip())
    return res


# new_text = tach(text)
# if "tất cả" in new_text[-1].lower() or "cả" in new_text[-1].lower():
#     cc = Object('c')
#     B = [cc]
# print(cc.name)

regex1 = r"(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)+\s*(\d+)\s*((?:\w|\s)+)"
regex2 = r"((?:số|Số)*(?:\w|\s)*)(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)*\s*(?:bằng|gấp)\s*((?:\d+/\d+)|\d+)\s*(?:lần)*\s*(?:số|Số)*((?:\w|\s)*)"
regext = [regex1, regex2]

test_str = ["Một cửa hàng buổi sáng bán được 13 kg đường. Buổi chiều bán được số đường gấp ba lần số đường bán được vào buổi sáng. Hỏi cả hai buổi cửa hàng bán được bao nhiêu ki-lô-gam đường?",
            "Băng giấy đỏ dài 25 cm, băng giấy xanh ngắn hơn băng giấy đỏ 14 cm. Hỏi cả hai băng giấy dài bao nhiêu xăng-ti-mét?"]

for index, i in enumerate(test_str):
    i = re.sub(r"một ", "1 ", i)
    i = re.sub(r"hai ", "2 ", i)
    i = re.sub(r"ba ", "3 ", i)
    i = re.sub(r"bốn ", "4 ", i)
    i = re.sub(r"năm ", "5 ", i)
    i = re.sub(r"sáu ", "6 ", i)
    i = re.sub(r"bảy ", "7 ", i)
    i = re.sub(r"tám ", "8 ", i)
    i = re.sub(r"chín ", "9 ", i)
    test_str[index] = i

print(test_str)

for test in test_str:
    for regex in regext:

        matches = re.finditer(regex, test, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            if regex == regex1:
                print(test[:match.start()] + ": ", end="")
            # print("Match {matchNum} was found at {start}-{end}: {match}".format(
                # matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

            # if regex == regex1:
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1

                print(match.group(groupNum), end=" ")
            # if regex == regex2:
            #     print(match.group(1))
            print()
# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

# i = 0
# while i < len(posts[1]):
#     if posts[1][i] == "Np":
#         NP.add(posts[0][i])
#     object = ""
#     while "N" in posts[1][i]:
#         object += posts[0][i] + " "
#         i += 1
#     if len(re.findall(r'\w+', object)) > 1:
#         tt = object.lower()
#         tt = string.capwords(tt[0]) + tt[1:]
#         NP.add(tt)
#     i += 1
# print(NP)
# NNA
# Np
# NN
