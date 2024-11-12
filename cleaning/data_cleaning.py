import pandas as pd

# Load the dataset with specified encoding to handle non-UTF-8 characters
df = pd.read_csv(r'C:\Users\marie\Desktop\data\Data_science_Crime_Project\data\cybercrimedata.csv', encoding='ISO-8859-1')

# Ensure column names are standardized (strip any whitespace and convert to lowercase)
df.columns = df.columns.str.strip().str.lower()

# Remove rows where 'organization_type' is 'others' (if the column exists)
if 'method' in df.columns:
    df = df[df['method'] != 'others']
else:
    print("Warning: 'organization_type' column not found in the dataset.")

# Define a dictionary for 'method' replacements
type_replacements = {
    "tech": "tech",
    "medical": "medical/healthcare",
    "healthcare": "medical/healthcare",
    "information technology": "tech",
    "teching": "tech",
    "hospitality": "retail/hospitality",
    "retail": "retail/hospitality",
    "mobile carrier": "telecommunications",
    "techmunications": "telecommunications",
    "telecoms": "telecommunications",
    "government": "government/military",
    "military": "government/military",
    "education": "education/academic",
    "academic": "education/academic",
    "financial": "finance/consulting",
    "consulting, accounting": "finance/consulting",
    "automobile": "automotive/transportation",
    "airline": "automotive/transportation",
    "advertising": "retail/hospitality"
}

# Apply the replacement mappings to the 'method' column if it exists
df['organization_type'] = df['organization_type'].str.strip().str.lower()  # Standardize values to match dictionary keys
df['organization_type'] = df['organization_type'].replace(type_replacements)

method_replacements = {
    "third-party": "third-party",
    "misconfiguration": "misconfiguration",
    "hacked": "hacking",
    "insider job": "inside_job",
    "oops": "other",
    "inside job": "inside_job",
    "poor security": "poor_security",
    "theft": "lost/stolen",
    "loss": "lost/stolen",
    "accidentally published": "accidental",
    "lost / stolen media": "lost/stolen",
    "lost / stolen computer": "lost/stolen",
    "hacking/it incident": "hacking",
    "unknown": "other",
    "accidentally exposed": "accidental",
    "poor security/inside job": "inside_job",
    "inside job, hacked": "inside_job",
    "lost": "lost/stolen",
    "unauthorized access": "hacking",
    "it incident": "hacking",
    "data breach": "other",
    "unsecured s3 bucket": "unprotected",
    "misconfiguration/poor security": "misconfiguration",
    "unprotected api": "unprotected",
    "data exposed by misconfiguration": "misconfiguration",
    "accidentally uploaded": "accidental",
    "poor security / hacked": "hacking",
    "social engineering": "other"
}
# Assuming 'method' is the column you want to modify
df['method'] = df['method'].str.strip().str.lower()
df['method'] = df['method'].replace(method_replacements)


# Save the modified DataFrame to a new file
output_path = r'C:\Users\marie\Desktop\data\Data_science_Crime_Project\data\processed_data.csv'
df.to_csv(output_path, index=False)

print(f"Data transformation completed and saved to '{output_path}'")
