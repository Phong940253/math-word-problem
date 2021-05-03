from pyvi import ViTokenizer, ViPosTagger

text = u"Một cửa hàng ngày thứ nhất bán được 28 lít dầu. Số dầu ngày thứ hai bán được bằng 1/7 số dầu bán được của ngày thứ nhất. Hỏi cả hai ngày cửa hàng bán được bao nhiêu lít dầu?"
posts = ViPosTagger.postagging(ViTokenizer.tokenize(text))
print(posts)
