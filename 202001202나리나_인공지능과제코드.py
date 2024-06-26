# -*- coding: utf-8 -*-
"""202001202나리나_인공지능과제코드

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZSoyq8hI7EynHTlH9sOEo5nJl3H1qaDy
"""

# 데이터 로드 및 확인
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
submission = pd.read_csv("sample_submission.csv")
international = pd.read_csv("international_trade.csv")

# 데이터 확인
print("Train 데이터셋의 처음 5행:")
print(train.head())

print("\nTest 데이터셋의 처음 5행:")
print(test.head())

print("\nInternational 데이터셋의 처음 5행:")
print(international.head())

# 결측치 확인
print("\nTrain 데이터셋의 결측치:")
print(train.isnull().sum())

print("\nTest 데이터셋의 결측치:")
print(test.isnull().sum())

print("\nInternational 데이터셋의 결측치:")
print(international.isnull().sum())

# 데이터 통계량 확인
print("\nTrain 데이터셋의 통계량:")
print(train.describe())

# 데이터 시각화
plt.figure(figsize=(10, 6))
sns.histplot(train['price(원/kg)'], bins=50, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price (KRW/kg)')
plt.ylabel('Frequency')
plt.show()

# 데이터 전처리
train['timestamp'] = pd.to_datetime(train['timestamp'])
train['is_weekend'] = (train['timestamp'].dt.dayofweek >= 5).astype(int)

# 카테고리형 변수 원-핫 인코딩
categorical_features = ['item', 'corporation', 'location']
encoder = OneHotEncoder(sparse=False)
encoded_features = encoder.fit_transform(train[categorical_features])

encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))
train = train.drop(columns=categorical_features).reset_index(drop=True)
train = pd.concat([train, encoded_df], axis=1)

# 데이터셋 준비
X = train.drop(columns=['ID', 'timestamp', 'price(원/kg)']).values
y = train['price(원/kg)'].values

# 데이터 스케일링
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# 학습 데이터와 검증 데이터 분리
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# PyTorch 데이터셋 정의
class TimeSeriesDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 데이터 로더 생성
train_dataset = TimeSeriesDataset(X_train, y_train)
val_dataset = TimeSeriesDataset(X_val, y_val)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 기존 모델 정의
class ExistingModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(ExistingModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# 모델 파라미터 설정 및 학습 루프
input_size = X.shape[1]  # 특성 수
hidden_size = 50
num_layers = 1
output_size = 1

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ExistingModel(input_size, hidden_size, num_layers, output_size).to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
epochs = 100
for epoch in range(epochs):
    model.train()
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs.unsqueeze(1))
        loss = criterion(outputs, targets.unsqueeze(1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("기존 모델 학습 완료")

# 모델 평가 함수 정의
def evaluate_model(model, data_loader):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in data_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs.unsqueeze(1))
            loss = criterion(outputs, targets.unsqueeze(1))
            total_loss += loss.item()
    return total_loss / len(data_loader)

# 기존 모델 평가
existing_model_loss = evaluate_model(model, val_loader)
print(f"기존 모델 MSE: {existing_model_loss:.4f}")

# 개선된 모델 정의
class ImprovedModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(ImprovedModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# 개선된 모델 학습
hidden_size = 100  # 은닉 상태 크기 증가
num_layers = 2  # LSTM 레이어 수 증가

model = ImprovedModel(input_size, hidden_size, num_layers, output_size).to(device)

# 학습 루프
epochs = 200  # 에포크 수 증가
for epoch in range(epochs):
    model.train()
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outputs = model(inputs.unsqueeze(1))
        loss = criterion(outputs, targets.unsqueeze(1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("개선된 모델 학습 완료")

# 개선된 모델 평가
improved_model_loss = evaluate_model(model, val_loader)
print(f"개선된 모델 MSE: {improved_model_loss:.4f}")