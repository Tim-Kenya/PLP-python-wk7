# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Data Loading and Exploration ---
print("--- 1. Data Loading and Exploration ---")

# Assume the dataset is a CSV file named 'data.csv' in the same directory.
# You can replace 'data.csv' with the actual path to your dataset.
try:
    df = pd.read_csv('data.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: 'data.csv' not found. Please make sure the file is in the correct directory or provide the correct path.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the data: {e}")
    exit()

# Display the first few rows of the dataframe
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Get basic information about the dataset
print("\nDataset information:")
df.info()

# Get descriptive statistics of numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# --- 2. Basic Data Analysis Results ---
print("\n--- 2. Basic Data Analysis Results ---")

# Example analysis: Let's say we have a column named 'Category' and a numerical column named 'Value'

# Count the occurrences of each category
if 'Category' in df.columns:
    category_counts = df['Category'].value_counts()
    print("\nCounts of each category:")
    print(category_counts)
else:
    print("\n'Category' column not found. Skipping category analysis.")

# Calculate the average of the 'Value' column
if 'Value' in df.columns and pd.api.types.is_numeric_dtype(df['Value']):
    average_value = df['Value'].mean()
    print(f"\nAverage value: {average_value:.2f}")
else:
    print("\n'Value' column not found or is not numeric. Skipping value analysis.")

# --- 3. Visualizations ---
print("\n--- 3. Visualizations ---")

# Example visualization 1: Bar chart of category counts
if 'Category' in df.columns:
    plt.figure(figsize=(10, 6))
    category_counts.plot(kind='bar')
    plt.title('Distribution of Categories')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("\nCannot create category bar chart as 'Category' column is missing.")

# Example visualization 2: Histogram of the 'Value' column
if 'Value' in df.columns and pd.api.types.is_numeric_dtype(df['Value']):
    plt.figure(figsize=(8, 6))
    plt.hist(df['Value'], bins=10, edgecolor='black')
    plt.title('Distribution of Value')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
else:
    print("\nCannot create value histogram as 'Value' column is missing or not numeric.")

# --- 4. Findings or Observations ---
print("\n--- 4. Findings or Observations ---")

print("Based on the initial exploration:")
print("- The dataset has {} rows and {} columns.".format(df.shape[0], df.shape[1]))
print("- The column names are: {}.".format(df.columns.tolist()))
print("- Summary statistics provide insights into the central tendency and spread of numerical data.")
print("- The number of missing values in each column can be observed.")

# Add more specific observations based on the example analysis and visualizations
if 'Category' in df.columns:
    print("\nCategory Analysis:")
    print(f"- There are {len(category_counts)} unique categories.")
    print(f"- The most frequent category is '{category_counts.index[0]}' with {category_counts.iloc[0]} occurrences.")

if 'Value' in df.columns and pd.api.types.is_numeric_dtype(df['Value']):
    print("\nValue Analysis:")
    print(f"- The average value is approximately {average_value:.2f}.")
    print("- The histogram shows the distribution of the 'Value' column.")

print("\nFurther analysis and more complex visualizations can be performed depending on the specific nature of the dataset and the questions you want to answer.")
