from snownlp import SnowNLP
from snownlp import sentiment

s = SnowNLP(u'这个东西真心很赞')
print(s.sentiments)