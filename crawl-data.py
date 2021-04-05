import sys
from bs4 import BeautifulSoup
import requests
import pickle


def check(x):
    return x or x.isspace()


indexBegin = sys.argv[1] or 0
indexEnd = sys.argv[2] or 100
# print(indexBegin, indexEnd)

for i in range(int(indexBegin), int(indexEnd)):
    begin = i * 500
    step = "500"
    response = requests.get(
        "https://olm.vn/?g=question.loadMore&start=" + str(begin) + "&step=" + step + "&tag=3&feature=0&newfeed=0&newq=0&id_subject=0")
    print("complete download page ", i)
    soup = BeautifulSoup(response.content, "html.parser")

    check = soup.find("div", class_="new")

    questions = check.find_all("a", class_="block-link text-overflow")
    # questions += check.find_all("p")

    # for question in questions:
    #     print(question.text)
    print("Start write file")
    pkl_file = open('Pre data/data' + str(i) + '.pkl', 'wb')
    ques = [question.text for question in questions]
    pickle.dump(ques, pkl_file)
    print("write file success!")
