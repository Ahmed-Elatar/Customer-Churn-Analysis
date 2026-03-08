# src/data_cleaning.py
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    # Ensure numeric types
    df['Total_Spend'] = pd.to_numeric(df['Total_Spend'], errors='coerce')
    df['Average_Rating'] = pd.to_numeric(df['Average_Rating'], errors='coerce')
    df['Items_Purchased'] = pd.to_numeric(df['Items_Purchased'], errors='coerce')
    df['Days_Since_Last_Purchase'] = pd.to_numeric(df['Days_Since_Last_Purchase'], errors='coerce')

    # Normalize boolean Discount Applied
    df['Discount_Applied'] = df['Discount_Applied'].astype(str).str.lower().map({'true': True, 'false': False, '1': True, '0': False})
    df['Discount_Applied'] = df['Discount_Applied'].fillna(False)

    # Handle missing numeric values (median imputation)
    num_cols = ['Total_Spend','Average_Rating','Items_Purchased','Days_Since_Last_Purchase']
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill categorical missing with 'Unknown'
    cat_cols = ['Gender','City','Membership_Type','Satisfaction_Level']
    for col in cat_cols:
        df[col] = df[col].fillna('Unknown')

    return df