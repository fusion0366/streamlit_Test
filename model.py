# model.py
# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import joblib # 모델 저장 또는 불러올 때

data = pd.read_csv("data/iris.csv")
le = LabelEncoder()
print(le.fit(data['Species']))
data['Species'] = le.fit_transform(data['Species'])
print(le.classes_) # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

X = data.drop(columns = ['Id', 'Species'])
y = data['Species']
print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# 모델 만들고 배포 (Export)
model_file = open("models/logistic_regression_model_iris_230425.pkl","wb")
joblib.dump(model, model_file)
model_file.close()