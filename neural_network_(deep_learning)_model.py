# -*- coding: utf-8 -*-
"""Neural Network (Deep Learning) model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zuTp2f5bLLzri3VLcxvYn2FhIyli9-zl
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.metrics import classification_report, accuracy_score

# โหลดข้อมูล
data = pd.read_csv('Employee_Clean.csv')

data.head()

# แปลงข้อมูลและแบ่งชุดข้อมูล
X = data.drop(columns=['is_promoted'])  # ลบคอลัมน์ 'is_promoted' จากตัวแปรอิสระ
y = data['is_promoted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

X_train = pd.get_dummies(X_train, columns=['department', 'education', 'gender'])
X_test = pd.get_dummies(X_test, columns=['department', 'education', 'gender'])

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# สร้างโมเดล Neural Network
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# ฝึกโมเดล
model.fit(X_train, y_train, epochs=10, batch_size=64)

# ทดสอบโมเดล
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)  # ตัดสินใจค่าส่งเสริมหรือไม่ด้วยค่าความน่าจะเป็น

# ประเมินผลโมเดล
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))