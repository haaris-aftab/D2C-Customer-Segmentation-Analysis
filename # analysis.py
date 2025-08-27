# analysis.py

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Data Loading & Cleaning ---
# Load the dataset from the same folder
try:
    df = pd.read_csv('online_retail_II.csv')
except FileNotFoundError:
    print("Error: 'online_retail_II.csv' not found. Make sure the dataset is in the same folder as this script.")
    exit()

# Clean the data
df.dropna(subset=['Customer ID'], inplace=True)
df = df[~df['Invoice'].str.contains('C', na=False)]
df['Customer ID'] = df['Customer ID'].astype(int)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalPrice'] = df['Price'] * df['Quantity']

print("Data loaded and cleaned successfully.")

# --- 2. Calculate RFM Metrics ---
# Set a snapshot date for analysis
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Group by customer and calculate RFM
rfm_df = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda date: (snapshot_date - date.max()).days, # Recency
    'Invoice': 'nunique', # Frequency
    'TotalPrice': 'sum' # Monetary
})

# Rename columns
rfm_df.rename(columns={'InvoiceDate': 'Recency',
                       'Invoice': 'Frequency',
                       'TotalPrice': 'MonetaryValue'}, inplace=True)

print("RFM metrics calculated.")

# --- 3. Create RFM Scores and Segments ---
r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], q=4, labels=r_labels)
rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), q=4, labels=f_labels)
rfm_df['M_Score'] = pd.qcut(rfm_df['MonetaryValue'], q=4, labels=m_labels)

rfm_df['RFM_Score'] = rfm_df['R_Score'].astype(str) + rfm_df['F_Score'].astype(str) + rfm_df['M_Score'].astype(str)

# Define segments
segment_map = {
    r'[3-4][3-4][3-4]': 'Champions',
    r'[2-4][1-3][1-3]': 'Loyal Customers',
    r'[3-4][1-2][3-4]': 'Potential Loyalists',
    r'1[3-4][3-4]': 'Recent Customers',
    r'111': 'Lost',
    r'[1-2][1-2][1-2]': 'Hibernating'
}

rfm_df['Segment'] = rfm_df['RFM_Score'].replace(segment_map, regex=True)
rfm_df['Segment'] = rfm_df['Segment'].fillna('Others')

print("Customer segments created.")

# --- 4. Visualize the Segments ---
segment_counts = rfm_df['Segment'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=segment_counts.index, y=segment_counts.values, palette='viridis')
plt.title('Customer Segmentation Distribution')
plt.xlabel('Customer Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)

# Save the plot to a file
plt.savefig('segment_distribution.png', bbox_inches='tight')

print("Visualization saved as 'segment_distribution.png'.")