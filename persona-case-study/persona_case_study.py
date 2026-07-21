# ===================================================
# RULE-BASED CLASSIFICATION - PERSONA CASE STUDY
# ===================================================
# Business Problem:
# Creating level-based customer personas using country, source, sex and age breakdown
# and estimating the average revenue potential of new customers based on these segments.
# Example: How much revenue can a 33-year-old Turkish female Android user generate?
# ===================================================

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)


# ---------------------------------------------------
# Task 1: Load the dataset and explore general information
# ---------------------------------------------------

df = pd.read_csv('datasets/persona.csv')
df.head()
df.dtypes


# ---------------------------------------------------
# Task 2: Find average price by country, source, sex and age breakdown
# ---------------------------------------------------

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})


# ---------------------------------------------------
# Task 3: Sort by price in descending order and save as agg_df
# ---------------------------------------------------

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()


# ---------------------------------------------------
# Task 4: Convert index names to column variables using reset_index()
# ---------------------------------------------------

agg_df.reset_index(inplace=True)
agg_df.head()


# ---------------------------------------------------
# Task 5: Create age categories and add as a new variable
# ---------------------------------------------------

bins = [0, 18, 23, 30, 40, df["AGE"].max()]
labels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=labels)
agg_df.head()


# ---------------------------------------------------
# Task 6: Create level-based customer definitions
# Format: COUNTRY-SOURCE-SEX-AGE_CAT
# ---------------------------------------------------

agg_df["customers_level_based"] = agg_df[["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].agg(
    lambda x: '-'.join(x).upper(), axis=1
)
agg_df.head()


# ---------------------------------------------------
# Task 7: Divide personas into segments (A, B, C, D) based on price
# ---------------------------------------------------

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head()

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})


# ---------------------------------------------------
# Task 8: Which segment does a 33-year-old Turkish female Android user belong to?
# What is the expected revenue?
# ---------------------------------------------------

agg_df.sort_values(by="PRICE")

new_user = "TUR-ANDROID-FEMALE-31_40"
agg_df[agg_df["customers_level_based"] == new_user]