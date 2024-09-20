import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler, RobustScaler
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, roc_auc_score
# 필요한 라이브러리 임포트
from sklearn.ensemble import StackingClassifier, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
# Let's load the uploaded CSV file and inspect the first few rows to understand its structure.
file_path = r'C:\Users\audwn\ITstudy\hana_data\ML04_BankDataSet\bank.csv'
data = pd.read_csv(file_path)
# Step 1: Preprocessing
# Encode the categorical variables

label_encoders = {}
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'deposit']

for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

numerical_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
numerical_columns_log = ['balance', 'duration', 'campaign', 'pdays', 'previous']
# Apply log transformation
# Add a small constant to avoid log(0) issues if necessary
for col in numerical_columns_log:
    # Check for negative values and replace them with a small positive value before log transformation
    data[col] = data[col].apply(lambda x: np.log1p(x) if x >= 0 else np.nan)  # log1p is equivalent to log(1 + x)

def remove_outliers_iqr(df, column):
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    # Calculate IQR
    IQR = Q3 - Q1
    # Define the bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Remove outliers
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Apply the outlier removal for each numerical column
for col in numerical_columns:
    data = remove_outliers_iqr(data, col)

# Separate features (X) and target (y)
X = data.drop(columns=['deposit'])  # All features except the target
X = X.drop(columns=['duration'])  # All features except the target

y = data['deposit']  # Target variable (whether deposit was made or not)

# 데이터셋을 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 베이스 모델들 생성
base_learners = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42)),
    ('svm', SVC(probability=True, random_state=42)),
    ('xgb', XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric='logloss', random_state=42))
]

# 메타 모델 생성 (스태킹의 최종 단계에서 사용할 모델)
meta_learner = LogisticRegression()

# 스태킹 앙상블 생성
stacking_clf = StackingClassifier(
    estimators=base_learners,
    final_estimator=meta_learner,
    cv=5
)

# 스태킹 모델 학습
stacking_clf.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = stacking_clf.predict(X_test)
y_prob = stacking_clf.predict_proba(X_test)[:, 1]

# AUC 및 다른 성능 평가 지표 출력
auc = roc_auc_score(y_test, y_prob)
print(f"Test AUC: {auc}")

# 분류 보고서 출력
print(classification_report(y_test, y_pred))

# Test AUC: 0.8324769380158601
#               precision    recall  f1-score   support

#            0       0.73      0.59      0.65       148
#            1       0.83      0.90      0.87       334

#     accuracy                           0.81       482
#    macro avg       0.78      0.75      0.76       482
# weighted avg       0.80      0.81      0.80       482