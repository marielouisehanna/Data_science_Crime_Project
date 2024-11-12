import pandas as pd

# Load the dataset from the CSV file
data = pd.read_csv(r"C:\Users\marie\Desktop\data\Data_science_Crime_Project\data\processed_data.csv")

# Convert the 'records' column to numeric, removing commas
data['records'] = pd.to_numeric(data['records'].str.replace(',', ''), errors='coerce')

# Calculating descriptive statistics for the 'records' column
mean_records = data['records'].mean()
median_records = data['records'].median()
std_records = data['records'].std()
min_records = data['records'].min()
max_records = data['records'].max()

# Storing the results in a dictionary
summary_statistics = {
    'Mean': mean_records,
    'Median': median_records,
    'Standard Deviation': std_records,
    'Minimum': min_records,
    'Maximum': max_records
}

# Printing the summary statistics
print(summary_statistics)
