from numpy import *
from csv import reader
from random import random
import operator
from collections import Counter
def getData(filename, train_percent):
    with open(filename,'r') as f:
        readlines=list(reader(f))
        train_dataset=list()
        test_dataset=list()
        dataset=[[0 for l in range(5)] for k in range(len(readlines))]
        
        for i in range(len(readlines)-1):# here -1 is done because there is an empty list added in the end by the reader
            for j in range(4):
                print(i,j, len(readlines), len(dataset))
                dataset[i][j]=float(readlines[i][j])
            dataset[i][4]=readlines[i][4]
            if random() < train_percent:
                train_dataset.append(dataset[i])
            else:
                test_dataset.append(dataset[i])
        return train_dataset,test_dataset
        
def distance_in_plot(instance_1, instance_2):
    distance=0
    for i in range(4):
        distance += (instance_1[i] - instance_2[i])**2
    return distance

def prediction(train_dataset,test_instance):
    result=[]
    for i in train_dataset:
        result.append([distance_in_plot(i, test_instance), i[4]]) 
    return result

def predict(result, k):
    d={}
    d['Iris-setosa']=0
    d['Iris-versicolor']=0
    d['Iris-virginica']=0
    for i in range(k):
        f=result[i][1]
        d[f] +=1
    print(d)
    temp=sorted(d.items(), key=operator.itemgetter(1))
    print(temp)
    return(temp[2][0])
    
if __name__ == '__main__':
    k=7
    count=0
    train_dataset,test_dataset = getData('iris.csv', 0.9)
    print()
    for i in test_dataset:
        result=prediction(train_dataset,i)
        result.sort(key=operator.itemgetter(0))
        p=predict(result, k)
        print(p, i[4])
        if p == i[4]:
            count +=1
    print("Accuracy:", count/len(test_dataset))



            


        
