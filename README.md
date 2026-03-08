# Customer Behavior & Satisfaction Analysis

## Project Overview

This project analyzes customer purchasing behavior, satisfaction levels,
and retention signals using an e-commerce customer dataset. The goal is
to identify valuable customer segments, understand spending patterns,
detect potential churn risks, and generate actionable business insights.

Companies rely on data-driven decision making to improve customer
retention, increase revenue, and optimize marketing strategies. This
project demonstrates a complete analytics workflow including data
cleaning, exploratory data analysis (EDA), visualization, segmentation,
and basic predictive modeling.

------------------------------------------------------------------------

## Business Objectives

The analysis aims to answer the following business questions:

-   Which customer segments generate the most revenue?
-   Which membership types spend the most?
-   Do discounts increase spending or only purchase frequency?
-   Which cities have the most valuable customers?
-   Which customers are at risk of leaving (high inactivity period)?
-   How does satisfaction relate to customer behavior and ratings?

------------------------------------------------------------------------

## Dataset Description

The dataset contains information about customer demographics, purchasing
behavior, satisfaction levels, and engagement metrics.

### Columns

  Column                     Description
  -------------------------- --------------------------------------
  Customer ID                Unique customer identifier
  Gender                     Customer gender
  Age                        Customer age
  City                       Customer location
  Membership Type            Loyalty membership level
  Total Spend                Total money spent by the customer
  Items Purchased            Number of purchased items
  Average Rating             Average product/service rating
  Discount Applied           Whether a discount was applied
  Days Since Last Purchase   Recency metric indicating inactivity
  Satisfaction Level         Customer satisfaction category

------------------------------------------------------------------------

## Project Structure

    customer-behavior-analysis/
    │
    ├── data/
    │   └── e_commerce_customer_behavior.csv
    │
    ├── notebooks/
    │   └── customer_analysis.ipynb
    │
    ├── src/
    │   ├── data_cleaning.py
    │   ├── feature_engineering.py
    │   ├── visualization.py
    │   └── modeling.py
    │
    ├── images/
    │   ├── age_distribution.png
    │   ├── spending_by_membership.png
    │   ├── discount_vs_spend.png
    │   ├── satisfaction_distribution.png
    │   └── correlation_matrix.png
    │
    ├── requirements.txt
    │
    └── README.md

### Folder Explanation

  Folder             Purpose
  ------------------ -------------------------------------------------------
  data               Contains the raw dataset
  notebooks          Jupyter notebook for exploratory analysis
  src                Python scripts for reusable data processing functions
  images             Exported charts and visualizations
  README.md          Project documentation
  requirements.txt   Python dependencies

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn
-   Scikit‑learn
-   Jupyter Notebook

These tools are widely used in data science workflows for data
manipulation, visualization, and machine learning.

------------------------------------------------------------------------

## Installation

Clone the repository:

``` bash
git clone https://github.com/Ahmed-Elatar/Customer-Churn-Analysis.git
cd customer-behavior-analysis
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## How to Run the Project

1.  Place the dataset inside the **data/** folder.
2.  Install required packages.
3.  Open the notebook:

    notebooks/customer_analysis.ipynb

4.  Run all cells to reproduce the analysis and generate visualizations.

Charts will be exported to the **images/** directory.

------------------------------------------------------------------------

## Exploratory Data Analysis

The notebook explores several aspects of customer behavior:

### Customer Demographics

-   Age distribution
-   Gender distribution
-   Geographic distribution by city

### Customer Spending Behavior

-   Spending patterns across membership types
-   Relationship between items purchased and total spend
-   Impact of discounts on spending

### Customer Satisfaction

-   Satisfaction level distribution
-   Relationship between ratings and satisfaction
-   Identification of dissatisfied customers

### Customer Retention

-   Analysis of inactivity periods
-   Identification of potential churn risks

------------------------------------------------------------------------

## Key Insights

Example findings from the analysis:

1.  **VIP and Gold membership customers generate the highest revenue.**
2.  **Customers who purchase more items generally have higher total
    spending.**
3.  **Discounts increase purchase volume but may reduce profit
    margins.**
4.  **Customers with long inactivity periods are more likely to show low
    satisfaction.**
5.  **Certain cities contribute significantly more revenue than
    others.**

------------------------------------------------------------------------

## Business Recommendations

Based on the analysis:

-   Focus marketing campaigns on **high‑value customer segments**
-   Create **loyalty programs** for medium‑value customers
-   Implement **reactivation campaigns** for inactive customers
-   Improve product or service quality for segments with **low
    satisfaction levels**

These strategies can help improve retention, increase revenue, and
strengthen customer loyalty.

------------------------------------------------------------------------

## Author

Ahmed Mohamed Elatar


