# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:04:49 2018

@author: shui
"""

import numpy as np
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pylab as pl
import random
from matplotlib import cm
from sklearn.model_selection import train_test_split

# 求平均值
def mean(numbers):
    return sum(numbers)/float(len(numbers))

# 求平均差
def stdev(numbers):
  avg = mean(numbers)
  variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
  return math.sqrt(variance)

# 求各列的平均值和方差
def summarize(dataset):
    parameter = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del parameter[-1]
    return parameter

# 进行分类
def separatedByClass(dataset):
    separated = {}
    #创建字典
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            #根据最后一个元素，随后一个元素为1,2,3,4，代表着水果的种类，作为键值key
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

# 类别属性提取特征,即每一类四种特征总的均值和方差
def summarizeByClass(dataset):
    separated = separatedByClass(dataset)
    summaries = { }
    #创建字典
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries


# 求出高斯概率密度函数
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

#所属类的概率
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    #字典
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities

# 对数据单一预测
# 每组测试数据最有可能的情况
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:

            bestProb = probability
            bestLabel = classValue
    return bestLabel

#进行多重预测
def getPredictions(summaries, testSet):
    predictions = []        #来存储结果
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions     # 最终返回输出结果

#输出结果计算准确率
def getAccuracy(testSet, predictions):
    correct = 0
    print("结果：")
    for x in range(len(testSet)):
        print("预测的结果：", predictions[x], "----", "正确的结果:",testSet[x][-1])
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

def main():

    fruits = pd.read_table('./fruit.txt') 
    feature_names = ['fruit_label', 'mass', 'width', 'height', 'color_score']
    X = fruits[['mass', 'width', 'height', 'color_score', 'fruit_label']]
    Y = fruits['fruit_label']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)  #通过pandas取出数据，再随机生成X_train和X_test 训练和测试数据
    Traindataset = X_train.values
    Testdataset = X_test.values

    summaries = summarizeByClass(Traindataset)            #根据测试数据进行提取数据特征， 分类，求方差，均值，然后对每类进行特征值提取
    print("特征的提取：",summaries)                      #输出贝叶斯整理的结果
    predictions = getPredictions(summaries, Testdataset)  #输入测试数据
    accuracy = getAccuracy(Testdataset, predictions)
    print("准确率：",accuracy,'%')

if __name__ == "__main__":
    main()
