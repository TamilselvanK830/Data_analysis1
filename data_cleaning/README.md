# Task 1 – Data Cleaning

## Project Overview
This project focuses on cleaning an employee dataset using Python and Pandas.

The objective is to handle missing values, correct data types, standardise text, remove duplicate records, detect outliers, and save a cleaned dataset.

## Dataset Columns
- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Salary

## Data Cleaning Steps

1. Loaded the original dataset using Pandas.
2. Checked missing values and duplicate records.
3. Standardised categorical text by removing extra spaces and correcting letter case.
4. Converted Age, Years of Experience, and Salary into numeric data types.
5. Filled missing numeric values using the median.
6. Filled missing categorical values using the mode.
7. Checked and removed duplicate records.
8. Detected outliers using the IQR method.
9. Created a before-and-after summary.
10. Saved the cleaned dataset as `clean_data.csv`.

## Missing Value Treatment

| Column | Method |
|---|---|
| Age | Median |
| Gender | No missing values |
| Education Level | Mode |
| Job Title | Mode |
| Years of Experience | Median |
| Salary | Median |

## Outlier Handling
Outliers were detected using the Interquartile Range (IQR) method. They were retained for further analysis because they may represent genuine employee records.

## Project Files
- `employees.csv` – Original dataset
- `data_cleaning.py` – Python cleaning program
- `clean_data.csv` – Cleaned dataset

## Technologies Used
- Python
- Pandas
- VS Code

## Conclusion
The dataset was cleaned by handling missing values, correcting data types, standardising text, checking duplicates, and detecting outliers. The final cleaned dataset was saved successfully as `clean_data.csv`.