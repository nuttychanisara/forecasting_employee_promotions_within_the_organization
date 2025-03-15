# -*- coding: utf-8 -*-
"""model Decision Tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n6-b_9jY-iyDKaf95sim9SSixDum2k2R

Decision Tree : การทำนายผลการเลื่อนตำแหน่งขึ้นอยู่กับความสัมพันธ์ระหว่างตัวแปรต่าง ๆ.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv('Employee_Clean.csv')

data.head()

feature_cols = ["department", "education", "gender", "age",
            "previous_year_rating", "length_of_service", "KPIs_met >80%", "avg_training_score"]
#แยกคอลัมน์ feature และ target
X = data[feature_cols]
y = data.is_promoted

#แบ่งข้อมูลเป็น train, test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#แปลง ข้อความ เป้น ตัวเลข
X_train = pd.get_dummies(X_train, columns=['department', 'education', 'gender'], drop_first=True)
X_test = pd.get_dummies(X_test, columns=['department', 'education', 'gender'], drop_first=True)

clf = DecisionTreeClassifier() #สร้าง Decision Tree Classifier
clf = clf.fit(X_train, y_train) #วิเคราะห์ด้วย training data
y_pred = clf.predict(X_test) #พยากรณ์ด้วย test data

# ประเมินผลโมเดล
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))