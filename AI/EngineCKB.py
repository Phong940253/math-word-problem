from fractions import Fraction
import re
import string
from copy import deepcopy
# -*- coding: utf-8 -*-


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
tinh = []


def In(i):
    if type(i) == type(1.2):
        return str(Fraction(i).limit_denominator(10))
    return str(i)


def cong(a, b, c):
    global exp
    if a.checkNone():
        tinh.append(a.name)
        a.value = b + c
        exp.append(In(b.value) + " + " + In(c.value) + " = " + In(a.value))
    return [a, b, c]


def tru(a, b, c):
    global exp
    if a.checkNone():
        tinh.append(a.name)
        a.value = b - c
        exp.append(In(b.value) + " - " + In(c.value) + " = " + In(a.value))
    return [a, b, c]


def nhan(a, b, c):
    global exp
    if a.checkNone():
        tinh.append(a.name)
        a.value = b * c
        exp.append(In(b.value) + " * " + In(c.value) + " = " + In(a.value))
    return [a, b, c]


def chia(a, b, c):
    global exp
    if a.checkNone():
        tinh.append(a.name)
        a.value = b / c
        exp.append(In(b.value) + " / " + In(c.value) + " = " + In(a.value))
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


def re6(a, b, h):
    a, b, h = tru(a, b, h)
    b, a, h = cong(b, h, a)
    h, b, a = tru(h, b, a)
    return [a, b, h]


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
h = Object("h")

f1 = Function([a, b, e], "f1", re1)
f2 = Function([a, b, f], "f2", re2)
f3 = Function([a, b, c], "f3", re3)
f4 = Function([a, b, d], "f4", re4)
f5 = Function([a, b, g], "f5", re5)
f6 = Function([a, b, h], "f6", re6)


F = [f1, f2, f3, f4, f5, f6]

M = [a, b, c, d, e, f, g, h]


# for i in f3.getListOutput(A):
#     print(i.name)
# solve(M, F, A, B)
# res = solve(M, F, A, B)
# res = find_good_soltion(M, F, A, B, res[1])


# caculate(OptSol, M, exp)

def convertFrac(str):
    x = str.split("/")
    if len(x) > 1:
        return int(x[0]) / int(x[1])
    return int(x[0])


class Engine:
    minDeep = 100000
    OptSol = []
    F = [f1, f2, f3, f4, f5, f6]
    M = [a, b, c, d, e, f, g, h]
    IsSol = False
    A = []
    B = []
    res = ""

    def __init__(self, text):
        try:
            global exp
            global tinh
            self.tinh = tinh
            self.tinh.clear()
            self.exp = exp
            self.exp.clear()
            self.A = []
            self.B = []
            self.res = ""
            regex1 = r"(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)+\s*(\d+)\s*((?:\w|\s)+)"
            regex2 = r"((?:số|Số)*(?:\w|\s)*)(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)*\s*(?:bằng|gấp)\s*((?:\d+/\d+)|\d+)\s*(?:lần)*\s*(?:số|Số)*((?:\w|\s)*)"
            regex3 = r"(?:Hỏi)*(?:\w|\s|-)*(?:cả)+(?:\w|\s|)*(?:bao nhiêu)\s*((?:\w|\s|-)+)"
            regex4 = r"((?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về))"
            regex5 = r"((?:số|Số)*(?:\w|\s)*)(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)*\s*((?:nhiều hơn|ít hơn|dài hơn|ngắn hơn)+)\s*(?:số|Số)*\s((?:\w|\s)*)\s((?:\d+/\d+)|\d+)\s*((?:\w|\s)*)"
            regext = [regex1, regex2, regex5]
            text = re.sub(r"một ", "1 ", text)
            text = re.sub(r"hai ", "2 ", text)
            text = re.sub(r"ba ", "3 ", text)
            text = re.sub(r"bốn ", "4 ", text)
            text = re.sub(r"năm ", "5 ", text)
            text = re.sub(r"sáu ", "6 ", text)
            text = re.sub(r"bảy ", "7 ", text)
            text = re.sub(r"tám ", "8 ", text)
            text = re.sub(r"chín ", "9 ", text)
            self.res = "TÓM TẮT:\n"
            matches = re.finditer(regex4, text, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                HanhDong = match.group(1).strip()
            for regex in regext:
                matches = re.finditer(regex, text, re.MULTILINE)

                for matchNum, match in enumerate(matches, start=1):
                    if regex == regex1:
                        ve1 = text[:match.start()].strip()
                        self.res += ve1 + ": "
                    # print("Match {matchNum} was found at {start}-{end}: {match}".format(
                        # matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

                    if regex == regex2:
                        if len(match.group()) > 2:
                            findOb1 = r"(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)+\s*\s*((?:\w|\s)+)"
                            matches1 = re.finditer(
                                findOb1, match.group(1), re.MULTILINE)
                            for matchNum1, match1 in enumerate(matches1, start=1):
                                Object1 = match.group()[:match1.start()]
                                Object1 = re.sub(r"Số ", "", Object1)
                                Object1 = re.sub(r"số", "", Object1)
                                Object1 = re.sub(DonVi, "", Object1)
                                test1 = DonVi.split(" ")
                                for i in test1:
                                    Object1 = re.sub(i, "", Object1)
                                Object1 = Object1.strip()
                                self.res += Object1 + " = "
                            self.res += match.group(2) + " lần "
                            findOb2 = r"(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)+\s*(?:vào)*\s*((?:\w|\s)*)"
                            matches1 = re.finditer(
                                findOb2, match.group(3), re.MULTILINE)
                            for matchNum1, match1 in enumerate(matches1, start=1):
                                Object2 = match1.group(1).strip()
                                if Object2 == "":
                                    Object2 = match.group(3)[:match1.start()]
                                test1 = DonVi.split(" ")
                                for i in test1:
                                    Object2 = re.sub(i, "", Object2)
                                if Object2 == "":
                                    Object2 = match.group(3)
                                Object2 = re.sub(r"của", "", Object2)
                                Object2 = Object2.strip()
                                self.res += Object2 + " "

                            if Object1.lower() in ve1.lower():
                                e = Object("e")
                            else:
                                e = Object("f")
                            e.value = convertFrac(match.group(2))
                            self.A.append(e)

                    if regex == regex1:
                        for groupNum in range(0, len(match.groups())):
                            groupNum = groupNum + 1
                            self.res += match.group(groupNum) + " "

                    if regex == regex1:
                        if len(match.group()) > 2:
                            a = Object("a")
                            a.value = int(match.group(1))
                            self.A.append(a)
                            DonVi = match.group(2)
                    # if regex == regex2:
                    #     print(match.group(1))
                    self.res += "\n"

                    if regex == regex5:
                        if len(match.group()) > 2:
                            self.res = self.res[:-1]
                            Object1 = match.group(1)
                            Object1 = re.sub(r"Số ", "", Object1)
                            Object1 = re.sub(r"số", "", Object1)
                            Object1 = re.sub(DonVi, "", Object1)
                            test1 = DonVi.split(" ")
                            for i in test1:
                                Object1 = re.sub(i, "", Object1)
                            test1 = HanhDong.split(" ")
                            for i in test1:
                                Object1 = re.sub(i, "", Object1)
                            Object1 = Object1.strip()
                            self.res += Object1 + " = "
                            print(match.group(3))
                            Object2 = match.group(3).strip()
                            # if Object2 == "":
                            #     Object2 = match.group(3)[:match1.start()]
                            test1 = DonVi.split(" ")
                            for i in test1:
                                Object2 = re.sub(i, "", Object2)
                            test1 = HanhDong.split(" ")
                            for i in test1:
                                Object2 = re.sub(i, "", Object2)
                            Object2 = re.sub(r"của", "", Object2)
                            Object2 = re.sub(r"là", "", Object2)
                            Object2 = re.sub(r"trong", "", Object2)
                            Object2 = Object2.strip()
                            self.res += Object2 + " "

                            if Object1.lower() in ve1.lower():
                                if "nhiều hơn" in match.group(2) or "dài hơn" in match.group(2):
                                    d = Object("d")
                                    self.res += " + " + \
                                        match.group(4) + " " + DonVi
                                    d.value = (int(match.group(4)))
                                else:
                                    self.res += " - " + \
                                        match.group(4) + " " + DonVi
                                    d = Object("h")
                                    d.value = int(match.group(4))
                            else:
                                if "nhiều hơn" in match.group(2) or "dài hơn" in match.group(2):
                                    d = Object("h")
                                    self.res += " + " + \
                                        match.group(4) + " " + DonVi
                                    d.value = int(match.group(4))
                                else:
                                    self.res += " - " + \
                                        match.group(4) + " " + DonVi
                                    d = Object("d")
                                    d.value = int(match.group(4))

                            self.res += "\n"
                            self.A.append(d)
            matches = re.finditer(regex3, text, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                c = Object("c")
                self.B.append(c)
                self.res += Object1 + " và " + Object2 + \
                    ": ? " + match.group(1) + "\n\nBÀI GIẢI:\n"

            fs = [False for x in range(len(self.F))]
            self.find_good_soltion(self.B, fs, [], 0)
            self.OptSol.reverse()
            self.IsSol = len(self.OptSol) > 0
            self.caculate(self.A)

            for ind, i in enumerate(self.tinh):
                if i == "a":
                    pass
                elif i == "b":
                    self.res += "Số " + DonVi + " " + Object2 + " " + HanhDong + " là:\n"
                    self.res += "    " + self.exp[ind] + "\n"
                elif i == "c":
                    self.res += "Số " + DonVi + " " + Object1 + \
                        " và " + Object2 + " " + HanhDong + " là:\n"
                    self.res += "    " + self.exp[ind] + "\n"
                    self.res += "        " + "Đáp số: " + \
                        self.exp[-1][self.exp[-1].rfind(" ") + 1:] + \
                        " " + DonVi
        except Exception:
            self.res = "Không thể giải"

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
