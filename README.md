# SnowNLP_Movie
基于SnowNLP的三百万电影数据的影评情感预测

# 项目详情
使用了约三百万包含正负的影评数据,如果有需要的话可以再进行增加,增加数据量理论上能更好的提高精度.

# 使用方法

> 我直接使用的是SnowNLP复制下来的代码,然后在它的基础上重新训练了关于电影影评相关的样本。

1. 测试test是否能够运行，如果能够运行代表项目已经跑通了
2. 测试SentimentTest是否能够运行，代表我训练的模型已经可以跑通了.
3. 直接调用函数即可.

```
from snownlp import SnowNLP

s = SnowNLP(u'甩迪斯尼好几条街！技术已经达到顶级水平！故事改编得有趣有人情味！可惜“哪吒”好丑！为中国国产动画的进步感到骄傲！致敬每一个为中国动画努力拼搏的人！')
print(s.sentiments)

s = SnowNLP(u'现在看来，中国会讲故事的导演和编剧一只手都能数的过来，中国电影行业现在就是一具大型的行尸走肉，一只没有灵魂的资产怪兽。')
print(s.sentiments)

```

# 训练方法

1. 打开train.py

2. 修改data中的两个txt的内容即可,然后运行train.py

```
from snownlp import sentiment
print("starting training")
sentiment.train('./data/neg.txt', './data/pos.txt')
print("saving model")
sentiment.save('sentiment.marshal')
print("end training")
```
3. 会在根目录生成sentiment.marshal.3把它复制到snownlp下的sentiment中.

4. 运行SentimentTest.py调用生成完成的模型


# 已训练完成的模型

我放在model下
我现在一共分享了两种,一种是50万的训练量,另外一种是三百万的训练量.
把需要替换的模型放到snownlp下的sentiment进行替换即可.