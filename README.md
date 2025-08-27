# README.md

# D2C Customer Segmentation Analysis

##  Project Objective

This project analyzes a transactional dataset from a UK-based online retailer to segment customers into distinct groups based on their purchasing behavior. The primary goal is to identify key customer segments to enable targeted and personalized marketing strategies, ultimately driving retention and sales.

##  Dataset

The analysis uses the "Online Retail II UCI" dataset, which contains transactional data from 2009 to 2011.

- **Source:** [Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)

##  Tools & Libraries

- **Python:** For data manipulation and analysis.
- **Pandas:** For data cleaning and processing.
- **Matplotlib & Seaborn:** For data visualization.

##  Analysis & Findings

The project uses the **RFM (Recency, Frequency, Monetary)** model to score customers:
1.  **Recency:** How recently a customer made a purchase.
2.  **Frequency:** How often they make purchases.
3.  **Monetary:** The total value of their purchases.

Based on these scores, customers were grouped into segments like **Champions, Loyal Customers, Potential Loyalists, and At-Risk**.


### Key Strategic Recommendations
- **Champions:** Nurture these high-value customers with loyalty programs and exclusive offers to maintain their engagement.
- **At-Risk / Hibernating:** Launch targeted win-back campaigns with personalized discounts to re-engage them.
- **Potential Loyalists:** Encourage repeat purchases through personalized product recommendations and follow-up marketing.

##  How to Run

1.  Ensure you have Python and the required libraries (`pandas`, `matplotlib`, `seaborn`) installed.
2.  Place the `online_retail_II.csv` dataset in the same directory.
3.  Run the script: `python analysis.py`
4.  The output plot will be saved as `segment_distribution.png`.
