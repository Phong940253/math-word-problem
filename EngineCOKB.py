def KiemTraSuKienTrongTapSuKien(fact, SetOfFacts):
    for i in range(len((SetOfFacts))):
        f = SetOfFacts[i]
        if HopNhatSuKien(f, fact):
            return True
    return False


def KiemTraTapSuKienTrongTapSuKien(fact1, fact2):
    count = 0
    for i in range(len(fact1)):
        f = fact1[i]
        if KiemTraSuKienTrongTapSuKien(f, fact2) == True:
            count += 1
    return count == len(fact1)


def giaiToan(O, F, G):
    Sol = []
    KnowFact = F
    flag = True

    currO = O

    if KiemTraTapSuKienTrongTapSuKien(G, O) or KiemTraSuKienTrongTapSuKien(G, F):
        return "Ket qua da co san trong gia thiet"

    for i in range(len(G)):
        if LoaiSuKien(G[i]) == 7:
            KnowFact = KnowFact.union({G[i]})
        elif LoaiSuKien(G[i]) == 10:
            KnowFact = KnowFact.union({lhs(G[i]), rhs(G[i])})
        elif LoaiSuKien(G[i]) == 12:
            for j in range(1, len(G[i])):
                if LoaiSuKien(G[i][j]) == 7:
                    KnowFact = KnowFact.union({G[i][j]})

    while flag == True:
        kfact == KnowFact
        temp == RCN1(KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        temp = RCN2(currO, KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        temp = RCN3(currO, KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        currO = op(3, temp)
        temp = RCN4(currO, KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        temp = RCN7(currO, KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        temp = RCN5(KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        temp = RCN6(currO, KnowFact)
        KnowFact = KnowFact.union(op(1, temp))
        Sol = [op(Sol), op(op(2, temp))]
        currO = op(4, temp)
        if KiemTraMucTieu(G, KnowFact) or kfact == KnowFact:
            flag = False
    if pr == True:
        print(KnowFact)
    if KiemTraMucTieu(G, KnowFact):
        return ThuGonLoiGiai(Sol, G)
