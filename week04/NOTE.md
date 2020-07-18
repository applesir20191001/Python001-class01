学习笔记

1、numpy.random.randint用法
 函数的作用是，返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)。
 如果没有写参数high的值，则返回[0,low)的值。
 size 个数

2、COUNT(DISTINCT order_id)
python 实现起来倒是也挺简洁的

3、INNER JOIN  等连接
对应python中的
pd.merge(data, data1, on= 'group', how='inner')

4、UNION
对应python中的
pd.concat([data, data1])

5、sql 中的delete和drop 列
对应python中的
df.drop
axis 控制行和列

凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。如果手动设定为True（默认为False），那么原数组直接就被替换。也就是说，采用inplace=True之后，原数组名对应的内存值直接改变；而采用inplace=False之后，原数组名对应的内存值并不改变，需要将新的结果赋给一个新的数组或者覆盖原数组的内存位置


