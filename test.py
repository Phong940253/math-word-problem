from pyvi import ViTokenizer, ViPosTagger
text = u"Hùng có 7 hộp bi như nhau đựng tổng cộng 112 viên. Hùng cho bạn 3 hộp. Hỏi Hùng còn lại bao nhiêu viên bi"
posts = ViPosTagger.postagging(ViTokenizer.tokenize(text))

print(posts)
exit(0)

Nu = set()
N = set()

for index, value in enumerate(posts[1]):
    if value == "Nu":
        Nu.add(posts[0][index])

for index, value in enumerate(posts[1]):
    if value == "N" and posts[0][index] not in Nu:
        N.add(posts[0][index])

all = []
for index, value in enumerate(posts[1]):
    if value == "M":
        begin = index
        end = begin + 1
        j = index + 1
        while posts[1][j] == "N" or posts[1][j] == "Nu" or posts[1][j] == "Nc":
            end += 1
            j += 1
        # if begin != end:
        all.append(posts[0][begin:end])

for index, value in enumerate(posts[1]):
    print(posts[0][index], value)

for i in all:
    print(i)
