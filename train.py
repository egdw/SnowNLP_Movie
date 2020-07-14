#使用SnowNLP进行训练
# 通过阅读snownlp的源码可以知道需要输入两个参数
# neg.txt 和 pos.txt
# 进行训练的结果会生成sentiment.marshal
from snownlp import sentiment
print("starting training")
sentiment.train('./data/neg.txt', './data/pos.txt')
print("saving model")
sentiment.save('sentiment.marshal')
print("end training")
