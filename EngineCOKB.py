def giaiToan(O, F, G):
    Sol = []
    KnowFact = F
    flag = True

    currO = O

    if KiemTraTapSuKienTrongTapSuKien(G, O) or KiemTraSuKienTrongTapSuKien(G, F):
        return "Ket qua da co san trong gia thiet"

    for i in nops(G):
        if LoaiSuKien(op(i, G)) == 7:
            KnowFact = KnowFact.union({op(i, G)})
        elif LoaiSuKien(op(i, G)) == 10:
            KnowFact = KnowFact.union({lhs(op(i, G)), rhs(op(i, G))})
        elif LoaiSuKien(op(i, G)) == 12:
            for j in nops(op(i, G))[2:]:
                if LoaiSuKien(op(j, op(i, G))) == 7:
                    KnowFact = KnowFact.union({op(j, op(i, G))})

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
    return
