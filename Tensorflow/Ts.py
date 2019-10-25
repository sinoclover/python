# # 基本操作
# import tensorflow as tf  # 引入tensorflow模块并简写为tf
#
# a = tf.constant([1.0, 2.0])  # 定义一个一维数组常量
# b = tf.constant([3.0, 4.0])
#
# result = a + b  # 进行矩阵加法运算过程
# print(result)

# # 神经元基本模型
# import tensorflow as tf
#
# x = tf.constant([[1.0, 2.0]])
# w = tf.constant([[3.0], [4.0]])  # 定义一个二维数组
#
# y = tf.matmul(x, w)  # 进行矩阵乘法运算过程
# print(y)
#
# print(tf.Session().run(y))
# with tf.Session() as sess:  # 使用with结构输出运算过程的值
#     print(sess.run(y))

# # NN的前向传播(两层简单全连接NN)
# import tensorflow as tf
#
# # 定义输入和参数
# # x = tf.constant([[0.7, 0.5]])
# # 用placeholder实现输入定义
# # x = tf.placeholder(tf.float32, shape = (1, 2))
# x = tf.placeholder(tf.float32, shape = (None, 2))
# w1 = tf.Variable(tf.random_normal([2, 3], stddev = 1, seed = 1))
# w2 = tf.Variable(tf.random_normal([3, 1], stddev = 1, seed = 1))
#
# # 定义前向传播过程
# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)
#
# # 用会话计算结果
# with tf.Session() as sess:
#     init_op = tf.global_variables_initializer()  # 变量初始化
#     sess.run(init_op)
#     # print('y is: ', sess.run(y))
#     # print('y is: ', sess.run(y, feed_dict = {x: [[0.7, 0.5]]}))  # 喂入一组数据
#     print('y is: ', sess.run(y, feed_dict = {x: [[0.7, 0.5], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5]]}))
#     print('w1:\n', sess.run(w1))
#     print('w2:\n', sess.run(w2))

# NN搭建框架
# 导入模块，生成模拟数据集
import tensorflow as tf
import numpy
BATCH_SIZE = 8
seed = 23455

# 基于seed产生随机数
rng = numpy.random.RandomState(seed)
# 随机数返回32行2列的矩阵，表示32组特征值作为输入
X = rng.rand(32, 2)
# 从X这个矩阵中取出一行，判断如果和小于1则给Y赋值1，反之赋值0
# 作为输入数据集的标签（正确答案）
# for (x0, x1) in X:
#     if (x0 + x1) < 1:
#         Y = [1]
#     else:
#         Y = [0]
Y = [[int((x0 + x1) < 1)] for x0, x1 in X]
print('X:\n', X)
print('Y:\n', Y)

# 1定义神经网络的输入、参数和输出，定义前向传播的过程
x = tf.placeholder(tf.float32, shape = (None, 2))
y_ = tf.placeholder(tf.float32, shape = (None, 1))

w1 = tf.Variable(tf.random_normal([2, 3], stddev = 1, seed = 1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev = 1, seed = 1))

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 2定义损失函数以及反向传播的过程
loss = tf.reduce_mean(tf.square(y - y_))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# train_step = tf.train.MomentumOptimizer(0.001, 0.9).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 3生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    # 输出未经训练的参数取值
    print('w1:\n', sess.run(w1))
    print('w2:\n', sess.run(w2))
    print('\n')

    # 训练模型
    STEPS = 3000
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict = {x: X[start:end], y_: Y[start:end]})
        if i % 500 == 0:
            total_loss = sess.run(loss, feed_dict = {x: X, y_: Y})
            print('After %d training step(s), loss on all data is %g' %(i, total_loss))

    print('\n')
    print('w1:\n', sess.run(w1))
    print('w2:\n', sess.run(w2))



