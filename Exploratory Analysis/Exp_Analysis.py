# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting styles
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load the dataset
data = pd.read_csv("Data_science_Crime_Project\data\processed_data.csv")  # Replace "file_path.csv" with your file path

# Step 1: Data Loading and Initial Inspection
print("Data Info:")
data.info()
print("\nFirst 5 Rows of Data:")
print(data.head())

# Step 2: Data Cleaning and Handling Missing Values
print("\nMissing Values Count:")
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
# Describe numerical columns
print("\nStatistical Summary for Numerical Columns:")
print(data.describe())

# Display value counts for categorical columns
print("\nValue Counts for Categorical Columns:")
for col in data.select_dtypes(include="object").columns:
    print(f"\n{col} Value Counts:")
    print(data[col].value_counts())

# Plot histograms for numerical columns
data.select_dtypes(include=np.number).hist(bins=15, figsize=(15, 10), edgecolor='black')
plt.suptitle("Histograms of Numerical Columns")
plt.show()

# Plot bar plots for categorical columns
for col in data.select_dtypes(include="object").columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(y=col, data=data, palette="viridis")
    plt.title(f"Count Plot of {col}")
    plt.show()

# Step 4: Bivariate Analysis
# Scatter plots for pairs of numerical columns
numerical_cols = data.select_dtypes(include=np.number).columns
for i in range(len(numerical_cols)):
    for j in range(i + 1, len(numerical_cols)):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data[numerical_cols[i]], y=data[numerical_cols[j]])
        plt.title(f"{numerical_cols[i]} vs {numerical_cols[j]}")
        plt.show()

# Box plots for categorical vs numerical relationships
for cat_col in data.select_dtypes(include="object").columns:
    for num_col in data.select_dtypes(include=np.number).columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=cat_col, y=num_col, data=data, palette="coolwarm")
        plt.title(f"{num_col} by {cat_col}")
        plt.xticks(rotation=45)
        plt.show()

# Step 5: Correlation Analysis
# Calculate and plot the correlation matrix for numerical columns
corr_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()

# Step 6: Summary and Key Insights
# Print summary statistics for further insights
print("\nSummary of Key Insights:")
print("Highest Correlations:")
print(corr_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(10))

print("Potential areas of further exploration include strong correlations, unique distributions, or outliers identified above.")
