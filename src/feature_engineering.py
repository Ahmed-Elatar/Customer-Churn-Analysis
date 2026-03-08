# src/feature_engineering.py
import pandas as pd
import numpy as np

def add_features(df):
    # Age groups
    df['Age_Group'] = pd.cut(df['Age'], bins=[0,18,25,35,45,55,65,120],
                             labels=['<18','18-25','26-35','36-45','46-55','56-65','65+'])

    # Customer value bucket by Total Spend
    df['Customer_Value'] = pd.qcut(df['Total_Spend'].rank(method='first'), q=3, labels=['Low','Medium','High'])

    # Recency risk flag
    df['At_Risk'] = df['Days_Since_Last_Purchase'] > 30  # boolean flag; tune threshold as needed

    # High rating flag
    df['High_Rating'] = df['Average_Rating'] >= 4.0

    return df