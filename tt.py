from pyvi import ViTokenizer, ViPosTagger

text = u" Có 8 bao gạo đựng tất cả 448 kg gạo. Hỏi có 5 bao gạo như thế nặng bao nhiêu kg?"
posts = ViPosTagger.postagging(ViTokenizer.tokenize(text))
print(posts)
