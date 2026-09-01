"""
FREIGHT FORECASTING - FREE DATA DOWNLOADER
Downloads all required training data from FREE sources
No paid APIs required!

Run: python download_data.py
Time: 5-10 minutes
Cost: FREE
"""

import pandas as pd
import yfinance as yf
import requests
from datetime import datetime

print("🚀 Starting FREE data download...")
print("="*60)

# Configuration
START_DATE = '2020-01-01'
END_DATE = '2026-08-30'

# =============================================================================
# 1. FREIGHT RATES (Baltic Dry Index via Yahoo Finance)
# =============================================================================
print("\n📊 [1/5] Downloading Freight Rates (Baltic Dry Index)...")
try:
    # Alternative: Use BDI from Yahoo Finance (no FRED key needed)
    # BDI is tracked as ^BDI ticker
    freight = yf.download('^BDI', start=START_DATE, end=END_DATE, progress=False)
    if not freight.empty:
        freight = freight[['Close']].rename(columns={'Close': 'Freight_Rate'})
        freight.to_csv('freight_rates.csv')
        print(f"   ✅ Downloaded {len(freight)} rows → freight_rates.csv")
    else:
        print("   ⚠️  BDI not available, using proxy...")
        # Fallback: Use oil tanker rates or container shipping index
        freight = yf.download('EURN', start=START_DATE, end=END_DATE, progress=False)
        freight = freight[['Close']].rename(columns={'Close': 'Freight_Rate'})
        freight.to_csv('freight_rates.csv')
        print(f"   ✅ Downloaded {len(freight)} rows (proxy) → freight_rates.csv")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   💡 Tip: Install yfinance: pip install yfinance")

# =============================================================================
# 2. COAL PRICES
# =============================================================================
print("\n⛏️  [2/5] Downloading Coal Prices...")
try:
    coal = yf.download('MTF=F', start=START_DATE, end=END_DATE, progress=False)
    if not coal.empty:
        coal = coal[['Close']].rename(columns={'Close': 'Coal_Price'})
        coal.to_csv('coal_prices.csv')
        print(f"   ✅ Downloaded {len(coal)} rows → coal_prices.csv")
    else:
        # Fallback: Use energy sector proxy
        coal = yf.download('XLE', start=START_DATE, end=END_DATE, progress=False)
        coal = coal[['Close']].rename(columns={'Close': 'Coal_Price'})
        coal.to_csv('coal_prices.csv')
        print(f"   ✅ Downloaded {len(coal)} rows (energy proxy) → coal_prices.csv")
except Exception as e:
    print(f"   ❌ Error: {e}")

# =============================================================================
# 3. OIL PRICES (WTI Crude)
# =============================================================================
print("\n🛢️  [3/5] Downloading Oil Prices...")
try:
    oil = yf.download('CL=F', start=START_DATE, end=END_DATE, progress=False)
    oil = oil[['Close']].rename(columns={'Close': 'Oil_Price'})
    oil.to_csv('oil_prices.csv')
    print(f"   ✅ Downloaded {len(oil)} rows → oil_prices.csv")
except Exception as e:
    print(f"   ❌ Error: {e}")

# =============================================================================
# 4. USD/INR EXCHANGE RATE
# =============================================================================
print("\n💱 [4/5] Downloading USD/INR Exchange Rate...")
try:
    usd_inr = yf.download('INR=X', start=START_DATE, end=END_DATE, progress=False)
    usd_inr = usd_inr[['Close']].rename(columns={'Close': 'USD_INR'})
    usd_inr.to_csv('usd_inr.csv')
    print(f"   ✅ Downloaded {len(usd_inr)} rows → usd_inr.csv")
except Exception as e:
    print(f"   ❌ Error: {e}")

# =============================================================================
# 5. WEATHER DATA (Open-Meteo - FREE, no API key!)
# =============================================================================
print("\n🌧️  [5/5] Downloading Weather Data (Vizag Port)...")
try:
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 17.68,      # Vizag port coordinates
        "longitude": 83.21,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "daily": "precipitation_sum,temperature_2m_mean",
        "timezone": "Asia/Kolkata"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        weather_data = response.json()['daily']
        weather = pd.DataFrame(weather_data)
        weather.columns = ['Date', 'Rainfall_mm', 'Temperature_C']
        weather.to_csv('weather_data.csv', index=False)
        print(f"   ✅ Downloaded {len(weather)} rows → weather_data.csv")
    else:
        print(f"   ❌ HTTP Error: {response.status_code}")
except Exception as e:
    print(f"   ❌ Error: {e}")

# =============================================================================
# 6. MERGE ALL DATA
# =============================================================================
print("\n🔗 Merging all datasets...")
try:
    # Load all CSVs
    freight = pd.read_csv('freight_rates.csv', index_col=0, parse_dates=True)
    coal = pd.read_csv('coal_prices.csv', index_col=0, parse_dates=True)
    oil = pd.read_csv('oil_prices.csv', index_col=0, parse_dates=True)
    usd_inr = pd.read_csv('usd_inr.csv', index_col=0, parse_dates=True)
    weather = pd.read_csv('weather_data.csv', parse_dates=['Date'])
    weather.set_index('Date', inplace=True)

    # Merge on date (inner join to keep only matching dates)
    merged = freight.join([coal, oil, usd_inr, weather], how='inner')

    # Add time-based features
    merged['Month'] = merged.index.month
    merged['Quarter'] = merged.index.quarter
    merged['DayOfYear'] = merged.index.dayofyear
    merged['Is_Monsoon'] = merged['Month'].isin([6, 7, 8, 9]).astype(int)

    # Reset index to have Date as column
    merged.reset_index(inplace=True)
    merged.rename(columns={'index': 'Date'}, inplace=True)

    # Save final training dataset
    merged.to_csv('training_data.csv', index=False)

    print(f"\n✅ SUCCESS! Final training dataset created:")
    print(f"   📄 File: training_data.csv")
    print(f"   📊 Rows: {len(merged)}")
    print(f"   📋 Columns: {len(merged.columns)}")
    print(f"\n   Column names:")
    for col in merged.columns:
        print(f"      - {col}")

    # Show sample data
    print(f"\n   Sample data (first 3 rows):")
    print(merged.head(3).to_string(index=False))

    # Data quality check
    print(f"\n📈 Data Quality Report:")
    print(f"   - Total rows: {len(merged)}")
    print(f"   - Date range: {merged['Date'].min()} to {merged['Date'].max()}")
    print(f"   - Missing values: {merged.isnull().sum().sum()}")
    print(f"   - Ready for ML training: {'YES ✅' if merged.isnull().sum().sum() == 0 else 'NO ❌'}")

except Exception as e:
    print(f"❌ Merge failed: {e}")
    print("💡 Make sure all individual CSV files were downloaded successfully")

print("\n" + "="*60)
print("🎉 DOWNLOAD COMPLETE!")
print("="*60)
print("\n📝 Next steps:")
print("   1. Check training_data.csv has data")
print("   2. Run: python train_model.py")
print("   3. Start building your ML models!")
print("\n💡 All data is FREE and ready to use for your hackathon!\n")
