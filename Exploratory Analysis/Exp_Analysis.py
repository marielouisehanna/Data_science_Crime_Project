# Import necessary libraries
import pandas as pd
import numpy as np
# Load the dataset
data = pd.read_csv("Data_science_Crime_Project\data\processed_data.csv")  # Replace "file_path.csv" with your file path

# Step 1: Data Loading and Initial Inspection
print("Step 1: Data Loading and Initial Inspection")
print("Data Info:")
data.info()
print("\nFirst 5 Rows of Data:")
print(data.head())

# Step 2: Data Cleaning and Handling Missing Values
print("\nStep 2: Data Cleaning and Handling Missing Values")
print("Missing Values Count:")
print(data.isnull().sum())

# Optionally, drop or fill missing values
# Drop rows or columns with too many missing values (e.g., columns with over 50% missing)
threshold = 0.5
data = data.dropna(thresh=int(threshold * len(data)), axis=1)

# For remaining missing values, you can use mean/mode imputation
# Example for filling numerical columns with mean
for col in data.select_dtypes(include=np.number).columns:
    data[col].fillna(data[col].mean(), inplace=True)

# Example for filling categorical columns with mode
for col in data.select_dtypes(include="object").columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

# Step 3: Univariate Analysis
print("\nStep 3: Univariate Analysis")
# Describe numerical columns
print("Statistical Summary for Numerical Columns:")
print(data.describe())

# Display value counts for categorical columns
print("\nValue Counts for Categorical Columns:")
for col in data.select_dtypes(include="object").columns:
    print(f"\n{col} Value Counts:")
    print(data[col].value_counts())

# Step 4: Bivariate Analysis
print("\nStep 4: Bivariate Analysis")
# Display correlation matrix for numerical columns
print("Correlation Matrix for Numerical Columns:")
corr_matrix = data.corr()
print(corr_matrix)

# Step 5: Summary and Key Insights
print("\nStep 5: Summary and Key Insights")
# Print summary statistics for further insights
print("Highest Correlations:")
print(corr_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(10))

print("Potential areas of further exploration include strong correlations, unique distributions, or outliers identified above.")
