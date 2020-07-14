from snownlp import SnowNLP

s = SnowNLP(u'甩迪斯尼好几条街！技术已经达到顶级水平！故事改编得有趣有人情味！可惜“哪吒”好丑！为中国国产动画的进步感到骄傲！致敬每一个为中国动画努力拼搏的人！')
print(s.sentiments)

s = SnowNLP(u'现在看来，中国会讲故事的导演和编剧一只手都能数的过来，中国电影行业现在就是一具大型的行尸走肉，一只没有灵魂的资产怪兽。')
print(s.sentiments)