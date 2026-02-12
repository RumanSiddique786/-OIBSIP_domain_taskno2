# Download dataset
import kagglehub

path = kagglehub.dataset_download("gokulrajkmv/unemployment-in-india")
print("Path to dataset files:", path)

# Import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = os.path.join(path, "Unemployment_Rate_upto_11_2020.csv")
data = pd.read_csv(file_path)

# Basic checks
print(data.head())
print(data.info())

# Clean column names
data.columns = data.columns.str.strip()

# Drop duplicate Region column
if 'Region.1' in data.columns:
    data.drop(columns=['Region.1'], inplace=True)

# 🔥 IMPORTANT FIX: remove spaces + convert date
data['Date'] = data['Date'].str.strip()
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Summary stats
print(data.describe())

# Split Covid and Pre-Covid data
covid_data = data[data['Date'] >= '2020-03-01']
pre_covid_data = data[data['Date'] < '2020-03-01']

# ---------------- Plot 1: Covid Impact ----------------
plt.figure(figsize=(10,5))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=covid_data,
    color='red'
)
plt.title("Covid-19 Impact on Unemployment Rate in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ---------------- Plot 2: Overall Trend ----------------
plt.figure(figsize=(10,5))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=data
)
plt.title("Unemployment Rate in India Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# ---------------- Plot 3: Pre vs During Covid ----------------
plt.figure(figsize=(10,5))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=pre_covid_data,
    label="Pre-Covid"
)
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=covid_data,
    label="Covid Period"
)
plt.title("Impact of Covid-19 on Unemployment Rate")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend()
plt.show()

# ---------------- Plot 4: Region-wise Analysis ----------------
plt.figure(figsize=(12,6))
sns.barplot(
    x='Region',
    y='Estimated Unemployment Rate (%)',
    data=data
)
plt.xticks(rotation=90)
plt.title("Region-wise Average Unemployment Rate in India")
plt.show()
