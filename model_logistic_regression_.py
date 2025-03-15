# -*- coding: utf-8 -*-
"""model Logistic Regression .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BQRY2bFjmv1fpcU-njuFLLEA_HpF_49G
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# โหลดข้อมูล
data = pd.read_csv('Employee_Clean.csv')
#แปลงข้อมูลและแบ่งชุดข้อมูล
X = data.drop(columns=['is_promoted'])
y = data['is_promoted']

X = pd.get_dummies(X, columns=['department', 'education', 'gender'])

 # แบ่งชุดข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# มาตรฐานข้อมูล
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# สร้างโมเดล Logistic Regression
model = LogisticRegression()

# ฝึกโมเดล
model.fit(X_train, y_train)

# ทดสอบโมเดล
y_pred = model.predict(X_test)

# ประเมินผลโมเดล
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))