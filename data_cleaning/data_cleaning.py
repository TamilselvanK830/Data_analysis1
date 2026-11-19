
import pandas as pd

# =====================================
# STEP 1: LOAD ORIGINAL DATASET
# =====================================

df = pd.read_csv("employees.csv")

# Keep original data for comparison
original_df = df.copy()

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())


# =====================================
# STEP 2: CHECK UNIQUE VALUES
# =====================================

print("\nUnique Values:")

for column in df.columns:
    print(f"\n{column}:")
    print(df[column].unique())


# =====================================
# STEP 3: STANDARDISE TEXT COLUMNS
# =====================================

text_columns = ["Gender", "Education Level", "Job Title"]

for column in text_columns:
    df[column] = df[column].str.strip().str.title()

# Correct education labels
df["Education Level"] = df["Education Level"].replace({
    "Bachelor'S": "Bachelor's",
    "Associate'S": "Associate's",
    "Master'S": "Master's",
    "Phd": "PhD"
})

print("\nText Standardised Successfully!")


# =====================================
# STEP 4: CLEAN NUMERIC COLUMNS
# =====================================

# Clean Age
df["Age"] = df["Age"].str.replace(
    " years", "", regex=False
)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Clean Years of Experience
df["Years of Experience"] = (
    df["Years of Experience"]
    .str.replace(" yrs", "", regex=False)
)

df["Years of Experience"] = pd.to_numeric(
    df["Years of Experience"], errors="coerce"
)

# Clean Salary
df["Salary"] = df["Salary"].str.replace(
    "$", "", regex=False
)
df["Salary"] = df["Salary"].str.replace(
    ",", "", regex=False
)
df["Salary"] = pd.to_numeric(
    df["Salary"], errors="coerce"
)

print("\nData Types After Conversion:")
print(df.dtypes)


# =====================================
# STEP 5: HANDLE MISSING VALUES
# =====================================

# Fill numeric columns with median
numeric_columns = ["Age", "Years of Experience", "Salary"]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill categorical columns with mode
categorical_columns = ["Education Level", "Job Title"]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing Values After Filling:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# =====================================
# STEP 6: REMOVE DUPLICATES
# =====================================

print("\nDuplicate Rows Before Removal:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate Rows After Removal:")
print(df.duplicated().sum())

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)


# =====================================
# STEP 7: DETECT OUTLIERS USING IQR
# =====================================

numeric_columns = ["Age", "Years of Experience", "Salary"]

print("\nOutlier Detection:")

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"\n{column}:")
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))


# =====================================
# STEP 8: BEFORE AND AFTER SUMMARY
# =====================================

summary_df = pd.DataFrame({
    "Metric": [
        "Rows",
        "Missing Values",
        "Duplicate Rows"
    ],

    "Before Cleaning": [
        len(original_df),
        original_df.isnull().sum().sum(),
        original_df.duplicated().sum()
    ],

    "After Cleaning": [
        len(df),
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
})

print("\nBefore and After Cleaning Summary:")
print(summary_df)


# =====================================
# STEP 9: SAVE CLEANED DATASET
# =====================================

df.to_csv("clean_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

print("\nFinal Dataset Information:")
print(df.info())
