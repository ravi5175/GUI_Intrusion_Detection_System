import numpy as np
import pandas as pd


from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score)

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer



traindata = pd.read_csv('kddtrain.csv', header=None)
testdata = pd.read_csv('kddtest.csv', header=None)

X = traindata.iloc[:,1:42]
Y = traindata.iloc[:,0]
C = testdata.iloc[:,0]
T = testdata.iloc[:,1:42]

scaler = Normalizer().fit(X)
trainX = scaler.transform(X)

scaler = Normalizer().fit(T)
testT = scaler.transform(T)


traindata = np.array(trainX)
trainlabel = np.array(Y)

testdata = np.array(testT)
testlabel = np.array(C)









def LR():
    name='Logistic Regression'
    model = LogisticRegression()
    model.fit(traindata, trainlabel)
    
    # make predictions
    expected = testlabel
    np.savetxt('classical/expected.txt', expected, fmt='%01d')
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)
    
    np.savetxt('classical/predictedlabelLR.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaLR.txt', proba)
    
    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")
    
   
    
    return [accuracy, precision, recall,f1,name]







    
def NB():
    name='Gaussian Naive Bayes'
    model = GaussianNB()
    model.fit(traindata, trainlabel)
    print(model)
    # make predictions
    expected = testlabel
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)
    
    np.savetxt('classical/predictedlabelNB.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaNB.txt', proba)
    
    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")
    
    
    
    return [accuracy, precision, recall,f1,name]






def KNN():
    name='K-nearest Neighbour'
    model = KNeighborsClassifier(n_neighbors=2)
    model.fit(traindata, trainlabel)
    print(model)
    # make predictions
    expected = testlabel
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)
    
    
    np.savetxt('classical/predictedlabelKNN.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaKNN.txt', proba)
    
    # summarize the fit of the model
    
    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")
    
    
   
    
    return [accuracy, precision, recall,f1,name]




def DT():  
    name='Decision Tree'
    model = DecisionTreeClassifier()
    model.fit(traindata, trainlabel)
    print(model)
    # make predictions
    expected = testlabel
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)
    
    np.savetxt('classical/predictedlabelDT.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaDT.txt', proba)
    # summarize the fit of the model
    
    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")
    
    
    return [accuracy, precision, recall,f1,name]
    
    
    



def RF():
    name='Random Forest'
    model = RandomForestClassifier(n_estimators=100)
    model = model.fit(traindata, trainlabel)
    
    # make predictions
    expected = testlabel
    predicted = model.predict(testdata)
    proba = model.predict_proba(testdata)
    np.savetxt('classical/predictedlabelRF.txt', predicted, fmt='%01d')
    np.savetxt('classical/predictedprobaRF.txt', proba)
    
    # summarize the fit of the model
    
    
    
    y_train1 = expected
    y_pred = predicted
    accuracy = accuracy_score(y_train1, y_pred)
    recall = recall_score(y_train1, y_pred , average="binary")
    precision = precision_score(y_train1, y_pred , average="binary")
    f1 = f1_score(y_train1, y_pred, average="binary")
    
    
    
   
    return [accuracy, precision, recall,f1,name]
    


