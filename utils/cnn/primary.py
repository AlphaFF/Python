#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: AlphaFF
# @Date:   2018-08-12 19:09:45
# @Email: liushahedi@gmail.com
# @Last Modified by:   AlphaFF
# @Last Modified time: 2018-08-12 20:08:05


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MINIST_data/', one_hot=True)

x = tf.placeholder('float', [None, 784])
W = tf.Variable(tf.zeros([784, 10]))1
b = tf.Variable(tf.zeros([10]))

# 模型
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 输入正确值
y_ = tf.placeholder('float', [None, 10])

# 计算交叉熵
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# 使用选择的优化算法(梯度下降算法)不断修改变量以降低成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_tables()

sess = tf.Session()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)    # 随机抓取训练数据中的100个批处理数据点
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))
