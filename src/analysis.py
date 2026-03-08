import pandas as pd

def spending_by_city(df):

    city_spend = df.groupby("City")["Total Spend"].mean()

    return city_spend.sort_values(ascending=False)