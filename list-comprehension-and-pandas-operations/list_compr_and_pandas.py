# ===================================================
# PYTHON DATA ANALYSIS - LIST COMPREHENSION & PANDAS
# ===================================================

import seaborn as sns
import pandas as pd

pd.set_option("display.width", 500)
pd.set_option('display.max_columns', None)


# ===================================================
# PART 1: LIST COMPREHENSION
# ===================================================

df = sns.load_dataset("car_crashes")

# ---------------------------------------------------
# Task 1: Convert numeric column names to uppercase and add "NUM_" prefix
# If the column type is not object → add "NUM_" prefix and uppercase
# If the column type is object → only uppercase
# ---------------------------------------------------

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# ---------------------------------------------------
# Task 2: Add "FLAG" suffix to columns that do not contain "no" in their name
# All column names must be uppercase
# ---------------------------------------------------

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


# ---------------------------------------------------
# Task 3: Select columns that are NOT in the given list and create a new dataframe
# ---------------------------------------------------

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


# ===================================================
# PART 2: PANDAS - TITANIC DATASET
# ===================================================

df = sns.load_dataset("titanic")

# ---------------------------------------------------
# Task 1: Load the Titanic dataset and explore basic info
# ---------------------------------------------------

df.head()
df.shape  # number of observations and variables

# ---------------------------------------------------
# Task 2: Find the number of male and female passengers
# ---------------------------------------------------

df["sex"].value_counts()

# ---------------------------------------------------
# Task 3: Find the number of unique values for each column
# ---------------------------------------------------

df.nunique()

# ---------------------------------------------------
# Task 4: Find the number of unique values in the pclass column
# ---------------------------------------------------

df["pclass"].nunique()

# ---------------------------------------------------
# Task 5: Find the number of unique values in pclass and parch columns
# ---------------------------------------------------

df[["pclass", "parch"]].nunique()

# ---------------------------------------------------
# Task 6: Check the type of embarked column, convert to category and verify
# ---------------------------------------------------

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

# ---------------------------------------------------
# Task 7: Show all information of passengers whose embarked value is "C"
# ---------------------------------------------------

df[df["embarked"] == "C"].head()

# ---------------------------------------------------
# Task 8: Show all information of passengers whose embarked value is NOT "S"
# ---------------------------------------------------

df[df["embarked"] != "S"].head()

# ---------------------------------------------------
# Task 9: Show all information of female passengers under the age of 30
# ---------------------------------------------------

df[(df["age"] < 30) & (df["sex"] == "female")].head()

# ---------------------------------------------------
# Task 10: Show passengers with fare over 500 or age over 70
# ---------------------------------------------------

df[(df["fare"] > 500) | (df["age"] > 70)].head()

# ---------------------------------------------------
# Task 11: Find the total number of missing values in each column
# ---------------------------------------------------

df.isnull().sum()

# ---------------------------------------------------
# Task 12: Drop the "who" column from the dataframe
# ---------------------------------------------------

df.drop("who", axis=1, inplace=True)

# ---------------------------------------------------
# Task 13: Fill missing values in "deck" column with the mode
# ---------------------------------------------------

df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df.isnull().sum()

# ---------------------------------------------------
# Task 14: Fill missing values in "age" column with the median
# ---------------------------------------------------

df["age"].fillna(df["age"].median(), inplace=True)
df.isnull().sum()

# ---------------------------------------------------
# Task 15: Find sum, count and mean of "survived" grouped by pclass and sex
# ---------------------------------------------------

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

# ---------------------------------------------------
# Task 16: Create "age_flag" column — 1 if age < 30, else 0
# ---------------------------------------------------

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x: age_30(x))
df.head()


# ===================================================
# PART 3: PANDAS - TIPS DATASET
# ===================================================

df = sns.load_dataset("tips")
df.head()

# ---------------------------------------------------
# Task 17: Find sum, min, max and mean of total_bill grouped by time
# ---------------------------------------------------

df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

# ---------------------------------------------------
# Task 18: Find sum, min, max and mean of total_bill grouped by day and time
# ---------------------------------------------------

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# ---------------------------------------------------
# Task 19: Find sum, min, max and mean of total_bill and tip
# for female customers at Lunch time, grouped by day
# ---------------------------------------------------

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]
})

# ---------------------------------------------------
# Task 20: Find the mean total_bill for orders where size < 3 and total_bill > 10
# ---------------------------------------------------

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# ---------------------------------------------------
# Task 21: Create a new column "total_bill_tip_sum" = total_bill + tip
# ---------------------------------------------------

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# ---------------------------------------------------
# Task 22: Sort by total_bill_tip_sum descending and assign top 30 to a new dataframe
# ---------------------------------------------------

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape