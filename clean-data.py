# -*- coding: utf-8 -*-
import collections
import pickle

write = open('clean\clean.txt', 'w', encoding='utf-16')
for i in range(76):

    listMath = {"+", "-", "*", "=", "<", ">"}
    listSpecial = {".", ",", ":", ";", "]"}

    with (open("Pre data\data" + str(i) + ".pkl", "rb")) as openfile:
        while True:
            try:
                read = pickle.load(openfile)
            except EOFError:
                break

    def filter(x):
        countNum = 0
        for i in x:
            if i >= "0" and i <= "9":
                countNum += 1
        return len(x) >= 70 and countNum <= len(x) / 4 and (u"hỏi" in x.lower() or u"tính" in x.lower()) and "a)" not in x and "a," not in x

    def Clean(x):
        for c in listMath:
            x = x.replace(c, " " + c + " ")
        for c in listSpecial:
            x = x.replace(" " + c, c)
        for c in listSpecial:
            x = x.replace(c + " ", c)
        for c in listSpecial:
            x = x.replace(c, c + " ")
        return " ".join(x.split())

    for x in read:
        sentence = x.strip()
        ques = " ".join(sentence.split())
        if filter(ques):
            if (collections.Counter(ques).most_common(1)[0][1] < len(ques) / 3):
                ques = Clean(ques)
                write.writelines(ques + "\n")

    # res = re.findall(
    #     r'[a-z0-9áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ+\-\*\/,. %?:=\[\]\"\'(){}<>;\\]+', txt, flags=re.IGNORECASE + re.MULTILINE)

write.close()
