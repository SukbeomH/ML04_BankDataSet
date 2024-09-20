
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score


# Let's load the uploaded CSV file and inspect the first few rows to understand its structure.
file_path = r'C:\Users\audwn\ITstudy\hana_data\ML04_BankDataSet\bank.csv'
data = pd.read_csv(file_path)
# Step 1: Preprocessing
# Encode the categorical variables
label_encoders = {}
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'deposit']
#age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,
#campaign,pdays,previous,poutcome,deposit 중에서
# job, marital, education, default, housing, loan, contact,  month, poutcome 을빼고
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Separate features (X) and target (y)
X = data.drop(columns=['deposit'])  # All features except the target
y = data['deposit']  # Target variable (whether deposit was made or not)

# Step 2: Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 3: Scale the numerical features
scaler = StandardScaler()
numerical_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
# age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,deposit
# job, marital, education, default, housing, loan, contact,  month, poutcome
X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])



# 최적 파라미터
best_params = {
    'n_estimators': 243,
    'max_depth': 18,
    'min_samples_split': 9,
    'min_samples_leaf': 1
}

# 데이터셋을 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델 생성 (최적화된 파라미터 사용)
model = RandomForestClassifier(**best_params, random_state=42)

# 모델 학습
model.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# AUC 및 다른 성능 평가 지표 출력
auc = roc_auc_score(y_test, y_prob)
print(f"Test AUC: {auc}")

# 분류 보고서 출력 (정확도, 재현율, F1-점수 등 포함)
print(classification_report(y_test, y_pred))
