# ===================================================
# RULE-BASED CLASSIFICATION - GEZINOMI CASE STUDY
# ===================================================
# Business Problem:
# Gezinomi aims to create level-based sales definitions using existing sales data
# and estimate the average revenue potential of new customers based on these segments.
# Example: Estimating the average revenue from a customer who wants to stay at
# an all-inclusive hotel in Antalya during a busy season.
# ===================================================

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)


# ---------------------------------------------------
# Task 1: Load the dataset and explore general information
# ---------------------------------------------------

df = pd.read_excel('datasets/miuul_gezinomi.xlsx')
df.head()
df.dtypes

# Question 2: How many unique cities are there? What are their frequencies?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Question 3: How many unique concepts are there?
df["ConceptName"].nunique()

# Question 4: How many sales were made per concept?
df["ConceptName"].value_counts()

# Question 5: Total revenue earned by city
df.groupby("SaleCityName").agg({"Price": "sum"})

# Question 6: Total revenue earned by concept
df.groupby("ConceptName").agg({"Price": "sum"})

# Question 7: Average price by city
df.groupby("SaleCityName").agg({"Price": "mean"})

# Question 8: Average price by concept
df.groupby("ConceptName").agg({"Price": "mean"})

# Question 9: Average price by city and concept breakdown
df.groupby(by=["SaleCityName", "ConceptName"]).agg({"Price": "mean"})


# ---------------------------------------------------
# Task 2: Convert SaleCheckInDayDiff to a categorical variable called EB_Score
# ---------------------------------------------------

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head()


# ---------------------------------------------------
# Task 3: Examine average price and frequency by City-Concept-[EB_Score / Season / CInDay] breakdown
# ---------------------------------------------------

# City - Concept - EB Score breakdown
df.groupby(by=["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})

# City - Concept - Season breakdown
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

# City - Concept - CInDay breakdown
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})


# ---------------------------------------------------
# Task 4: Sort City-Concept-Season breakdown by Price in descending order
# Save the output as agg_df
# ---------------------------------------------------

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head(20)


# ---------------------------------------------------
# Task 5: Convert index names to column variables using reset_index()
# ---------------------------------------------------

agg_df.reset_index(inplace=True)
agg_df.head()


# ---------------------------------------------------
# Task 6: Define new level-based sales and add as a variable to the dataset
# Format: CITY_CONCEPT_SEASON
# ---------------------------------------------------

agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(
    lambda x: '_'.join(x).upper(), axis=1
)
agg_df.head()


# ---------------------------------------------------
# Task 7: Divide personas into segments based on Price
# Add segments to agg_df and describe them
# ---------------------------------------------------

agg_df['SEGMENT'] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head()
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})


# ---------------------------------------------------
# Task 8: Sort final dataframe by Price
# Which segment does "ANTALYA_HERŞEY DAHIL_HIGH" belong to?
# Expected revenue: ~64.92
# ---------------------------------------------------

agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]