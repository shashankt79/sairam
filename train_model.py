"""
FAST ML MODEL TRAINER FOR FREIGHT FORECASTING
Trains XGBoost model on downloaded data in 2 minutes!

Run: python train_model.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import os

print("="*60)
print("🚀 TRAINING FREIGHT FORECASTING MODEL")
print("="*60)

# Check if data exists
if not os.path.exists('training_data.csv'):
    print("❌ training_data.csv not found!")
    print("💡 Please run: python download_data.py first")
    exit(1)

# 1. Load Data
print("\n📂 [1/4] Loading training data...")
df = pd.read_csv('training_data.csv')
print(f"   ✓ Loaded {len(df)} rows")
print(f"   ✓ Columns: {list(df.columns)}")

# 2. Preprocess & Feature Engineering
print("\n🔧 [2/4] Engineering features...")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Create lag features (previous days' rates)
df['Rate_Lag1'] = df['Freight_Rate'].shift(1)
df['Rate_Lag7'] = df['Freight_Rate'].shift(7)
df['Rate_MA7'] = df['Freight_Rate'].rolling(window=7).mean()
df['Rate_MA30'] = df['Freight_Rate'].rolling(window=30).mean()

# Price ratios
df['Coal_Freight_Ratio'] = df['Coal_Price'] / (df['Freight_Rate'] + 1)
df['Oil_Freight_Ratio'] = df['Oil_Price'] / (df['Freight_Rate'] + 1)

# Drop NaN values from lag features
df.dropna(inplace=True)

print(f"   ✓ Rows after feature engineering: {len(df)}")

# Define features and target
feature_cols = [
    'Coal_Price', 'Oil_Price', 'USD_INR', 'Rainfall_mm', 'Temperature_C',
    'Month', 'Quarter', 'Is_Monsoon',
    'Rate_Lag1', 'Rate_Lag7', 'Rate_MA7', 'Rate_MA30',
    'Coal_Freight_Ratio', 'Oil_Freight_Ratio'
]

# Keep only existing columns
feature_cols = [col for col in feature_cols if col in df.columns]

X = df[feature_cols]
y = df['Freight_Rate']

print(f"   ✓ Using {len(feature_cols)} features: {feature_cols}")

# 3. Train-Test Split (80/20 time-based split, no shuffle)
print("\n✂️  [3/4] Splitting data (80% train, 20% test)...")
split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

print(f"   ✓ Train set: {len(X_train)} rows")
print(f"   ✓ Test set:  {len(X_test)} rows")

# 4. Train Model
print("\n🤖 [4/4] Training XGBoost Regressor...")
model = XGBRegressor(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
accuracy = max(0, (1 - (mae / y_test.mean()))) * 100

print("\n" + "="*60)
print("📊 MODEL PERFORMANCE RESULTS")
print("="*60)
print(f"   🎯 Accuracy:  {accuracy:.1f}%")
print(f"   📉 MAE:       ${mae:.2f}")
print(f"   📉 RMSE:      ${rmse:.2f}")
print(f"   📈 R² Score:  {r2:.3f}")
print("="*60)

# Feature Importance
print("\n🏆 Top 5 Most Important Features:")
importance = pd.DataFrame({
    'Feature': feature_cols,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

for idx, row in importance.head(5).iterrows():
    print(f"   {row['Feature']:<20} {row['Importance']*100:.1f}%")

# Save model & feature list
with open('xgboost_model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'features': feature_cols}, f)

print(f"\n💾 Model saved to: xgboost_model.pkl")

# Quick test prediction
print("\n🔮 Sample Prediction:")
sample = X_test.iloc[-1:]
actual = y_test.iloc[-1]
predicted = model.predict(sample)[0]
print(f"   Actual Rate:    ${actual:.2f}")
print(f"   Predicted Rate: ${predicted:.2f}")
print(f"   Error:          ${abs(actual - predicted):.2f} ({(abs(actual-predicted)/actual)*100:.1f}%)")

print("\n✅ Training complete! Next step: run python app.py")
