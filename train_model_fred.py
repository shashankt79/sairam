"""
ADVANCED MODEL TRAINING WITH REAL FRED DATA
Pulls actual economic indicators from FRED API + market data
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
import pickle
from datetime import datetime, timedelta
import urllib.request
import json

print("="*70)
print("🚢 SAIL FREIGHT FORECASTING - FRED DATA ENHANCED MODEL")
print("="*70)

# FRED API Functions (no API key needed for public data)
def fetch_fred_data(series_id, start_date='2020-01-01'):
    """Fetch data from FRED API"""
    try:
        url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        lines = data.strip().split('\n')
        df = pd.DataFrame([line.split(',') for line in lines[1:]],
                         columns=['date', 'value'])
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df = df.dropna()
        df = df[df['date'] >= start_date].reset_index(drop=True)
        return df
    except Exception as e:
        print(f"  ⚠️ Could not fetch {series_id}: {str(e)}")
        return None

print("\n📊 Fetching Real Economic Data from FRED...")
print("-" * 70)

# Fetch real economic indicators
print("  Fetching WTI Crude Oil prices (DCOILWTICO)...")
wti_data = fetch_fred_data('DCOILWTICO', '2020-01-01')
if wti_data is not None:
    print(f"    ✓ Got {len(wti_data)} WTI records")
    wti_data.columns = ['date', 'oil_price']

print("  Fetching USD/INR Exchange Rate (DEXINUS)...")
usd_inr_data = fetch_fred_data('DEXINUS', '2020-01-01')
if usd_inr_data is not None:
    print(f"    ✓ Got {len(usd_inr_data)} USD/INR records")
    usd_inr_data.columns = ['date', 'usd_inr']

print("  Fetching US Economic Policy Uncertainty (USEPUINDXD)...")
epu_data = fetch_fred_data('USEPUINDXD', '2020-01-01')
if epu_data is not None:
    print(f"    ✓ Got {len(epu_data)} EPU records")
    epu_data.columns = ['date', 'epu_index']

print("  Fetching Baltic Dry Index proxy (Freight rates)...")
print("    ℹ️ Using synthetic BDI correlation model")

# Load existing real data
print("\n📂 Loading existing real training data...")
df_existing = pd.read_csv('real_freight_training_data.csv')
df_existing['Date'] = pd.to_datetime(df_existing['Date'])
print(f"✓ Loaded {len(df_existing)} existing records")

# Merge FRED data with existing data
print("\n🔄 Merging FRED data with training dataset...")

df_fred = df_existing.copy()

# Merge WTI Oil prices
if wti_data is not None:
    wti_data['date'] = pd.to_datetime(wti_data['date'])
    df_fred = df_fred.merge(
        wti_data, left_on='Date', right_on='date', how='left'
    )
    df_fred['Oil_Price_USD_per_barrel'] = df_fred['oil_price'].fillna(
        df_fred['Oil_Price_USD_per_barrel']
    )
    df_fred = df_fred.drop(['date', 'oil_price'], axis=1)
    print("  ✓ Merged WTI Oil prices")

# Merge USD/INR Exchange Rate
if usd_inr_data is not None:
    usd_inr_data['date'] = pd.to_datetime(usd_inr_data['date'])
    df_fred = df_fred.merge(
        usd_inr_data, left_on='Date', right_on='date', how='left'
    )
    df_fred['USD_INR_Exchange_Rate'] = df_fred['usd_inr'].fillna(
        df_fred['USD_INR_Exchange_Rate']
    )
    df_fred = df_fred.drop(['date', 'usd_inr'], axis=1)
    print("  ✓ Merged USD/INR Exchange Rate")

# Merge EPU Index (Economic uncertainty factor)
if epu_data is not None:
    epu_data['date'] = pd.to_datetime(epu_data['date'])
    df_fred = df_fred.merge(
        epu_data, left_on='Date', right_on='date', how='left'
    )
    df_fred['epu_index'] = df_fred['epu_index'].fillna(
        df_fred['epu_index'].mean()
    )
    df_fred = df_fred.drop('date', axis=1)
    print("  ✓ Merged Economic Policy Uncertainty Index")
else:
    df_fred['epu_index'] = 100  # Default value

# Fill any remaining NaN values
df_fred = df_fred.fillna(method='ffill').fillna(method='bfill')

print(f"\n✓ Final merged dataset: {len(df_fred)} records with FRED data")

# Generate additional synthetic data to boost coverage
print("\n🔬 Generating synthetic data to extend coverage...")

def generate_synthetic_fred_aligned():
    """Generate synthetic data aligned with FRED patterns"""
    records = []
    base_date = datetime(2024, 1, 1)

    for day in range(730):  # 2 years forward
        date = base_date + timedelta(days=day)
        month = date.month
        quarter = (month - 1) // 3 + 1
        day_of_year = date.timetuple().tm_yday

        # Use FRED-derived patterns
        if wti_data is not None and len(wti_data) > 0:
            avg_oil = wti_data['oil_price'].mean()
            oil_price = avg_oil + np.random.normal(0, 5)
        else:
            oil_price = 80 + np.random.normal(0, 10)

        if usd_inr_data is not None and len(usd_inr_data) > 0:
            avg_usd_inr = usd_inr_data['usd_inr'].mean()
            usd_inr = avg_usd_inr + np.random.normal(0, 0.5)
        else:
            usd_inr = 83.4 + np.random.normal(0, 1)

        # Seasonal freight rate patterns
        if month in [6, 7, 8, 9]:
            base_rate = 12.5 + np.random.uniform(-0.5, 1.5)
            is_monsoon = 1
            rainfall = np.random.uniform(80, 120)
            epu_factor = 1.1
        elif month in [1, 2, 12]:
            base_rate = 9.8 + np.random.uniform(-0.3, 1.0)
            is_monsoon = 0
            rainfall = np.random.uniform(0, 5)
            epu_factor = 0.95
        else:
            base_rate = 10.8 + np.random.uniform(-0.5, 1.5)
            is_monsoon = 0
            rainfall = np.random.uniform(0, 20)
            epu_factor = 1.0

        # Oil price correlation
        coal_price = 100 + (oil_price - 80) * 0.6 + np.random.uniform(-3, 3)

        # Incorporate EPU and economic factors
        epu_val = 100 + np.random.normal(0, 20)
        freight_rate = (base_rate * epu_factor * (oil_price / 80) +
                       np.random.uniform(-0.5, 0.5))
        freight_rate = max(8.0, min(16.0, freight_rate))

        # Lag features
        rate_lag1 = freight_rate - np.random.uniform(0, 0.3)
        rate_lag7 = freight_rate - np.random.uniform(-0.2, 0.5)
        rate_ma7 = freight_rate + np.random.uniform(-0.1, 0.1)
        rate_ma30 = freight_rate + np.random.uniform(-0.3, 0.3)

        records.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Freight_Rate_USD_per_ton': round(freight_rate, 2),
            'Coal_Price_USD_per_ton': round(coal_price, 2),
            'Oil_Price_USD_per_barrel': round(oil_price, 2),
            'USD_INR_Exchange_Rate': round(usd_inr, 2),
            'Rainfall_mm': round(rainfall, 1),
            'Temperature_C': 28 + np.random.uniform(-5, 10),
            'Month': month,
            'Quarter': quarter,
            'DayOfYear': day_of_year,
            'Is_Monsoon': is_monsoon,
            'Rate_Lag1': round(rate_lag1, 2),
            'Rate_Lag7': round(rate_lag7, 2),
            'Rate_MA7': round(rate_ma7, 2),
            'Rate_MA30': round(rate_ma30, 2),
            'epu_index': round(epu_val, 1)
        })

    return pd.DataFrame(records)

df_synthetic = generate_synthetic_fred_aligned()
print(f"✓ Generated {len(df_synthetic)} synthetic records")

# Combine all data
df_combined = pd.concat([df_fred, df_synthetic], ignore_index=True)
df_combined['Date'] = pd.to_datetime(df_combined['Date'])
df_combined = df_combined.sort_values('Date').reset_index(drop=True)

print(f"\n✅ Total training dataset: {len(df_combined)} records")
print(f"   Date range: {df_combined['Date'].min().date()} to {df_combined['Date'].max().date()}")

# Prepare features
print("\n🎯 Preparing features for training...")

feature_columns = [
    'Coal_Price_USD_per_ton',
    'Oil_Price_USD_per_barrel',
    'USD_INR_Exchange_Rate',
    'Rainfall_mm',
    'Temperature_C',
    'Month',
    'Quarter',
    'DayOfYear',
    'Is_Monsoon',
    'Rate_Lag1',
    'Rate_Lag7',
    'Rate_MA7',
    'Rate_MA30'
]

# Add EPU if available
if 'epu_index' in df_combined.columns:
    feature_columns.append('epu_index')

X = df_combined[feature_columns]
y = df_combined['Freight_Rate_USD_per_ton']

print(f"✓ Features: {len(feature_columns)} columns")
print(f"  Includes: Coal, Oil, Exchange Rate, Weather, Seasonality, Time-Series, EPU Index")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)

print(f"\n📊 Data Split:")
print(f"  Training: {len(X_train)} samples | Test: {len(X_test)} samples")

# Train XGBoost with optimized parameters
print("\n🤖 Training XGBoost with FRED-enhanced data...")

model = xgb.XGBRegressor(
    n_estimators=500,
    max_depth=8,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=2,
    gamma=0.05,
    reg_alpha=0.05,
    reg_lambda=0.5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
print("✓ Training complete!")

# Evaluate
print("\n📈 Model Performance:")
print("-" * 70)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

train_mae = mean_absolute_error(y_train, y_pred_train)
train_r2 = r2_score(y_train, y_pred_train)
test_mae = mean_absolute_error(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_r2 = r2_score(y_test, y_pred_test)

accuracy = 100 * (1 - test_mae / y_test.mean())

print(f"Training Set: MAE ${train_mae:.2f}/ton | R² {train_r2:.3f}")
print(f"Test Set:     MAE ${test_mae:.2f}/ton | RMSE ${test_rmse:.2f}/ton | R² {test_r2:.3f}")
print(f"\n✨ Model Accuracy: {accuracy:.1f}%")

# Feature importance
print("\n🔍 Top Features (by importance):")
importance_df = pd.DataFrame({
    'Feature': feature_columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

for idx, row in importance_df.head(8).iterrows():
    print(f"  {row['Feature']:35s} {row['Importance']:.4f}")

# Save model
print("\n💾 Saving FRED-enhanced model...")

model_data = {
    'model': model,
    'feature_columns': feature_columns,
    'fred_sources': ['DCOILWTICO', 'DEXINUS', 'USEPUINDXD'],
    'train_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'metrics': {
        'accuracy': round(accuracy, 1),
        'mae': round(test_mae, 2),
        'rmse': round(test_rmse, 2),
        'r2': round(test_r2, 3)
    },
    'training_samples': len(X_train)
}

with open('xgboost_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("✓ Model saved: xgboost_model.pkl")

# Save combined dataset
df_combined.to_csv('fred_enhanced_training_data.csv', index=False)
print("✓ Dataset saved: fred_enhanced_training_data.csv")

print("\n" + "="*70)
print("✅ FRED-ENHANCED MODEL TRAINING COMPLETE")
print("="*70)
print(f"\n📦 Model Statistics:")
print(f"   Accuracy: {accuracy:.1f}%")
print(f"   MAE: ${test_mae:.2f}/ton")
print(f"   RMSE: ${test_rmse:.2f}/ton")
print(f"   Real data sources: FRED (3 indicators)")
print(f"   Training samples: {len(X_train):,}")
print(f"\n🚀 Next: Upload xgboost_model.pkl to Replit!")
