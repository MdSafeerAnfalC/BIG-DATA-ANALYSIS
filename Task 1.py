import dask.dataframe as dd
import pandas as pd
import os

# --- Configuration ---

dir= 'dask_analysis_results'
os.makedirs(dir, exist_ok=True)

print(f"Dask Analysis on Covid - 19...")

# --- 1. Load Data with Dask ---

try:
    ddf = dd.read_csv("E:/ALL Folder/Downloads/archive/Covid - 19.csv")
    print("\n--- Data Loaded with Dask ---")
    print(ddf.head())
    print(f"Number of partitions: {ddf.npartitions}")
    print(f"Dask DataFrame dtypes:\n{ddf.dtypes}")
except Exception as e:
    print(f"Error loading data with Dask: {e}")
    exit()

# --- 2. Data Cleaning and Preprocessing 

numeric_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths',
                'New recovered', 'Deaths / 100 Cases', 'Recovered / 100 Cases',
                'Deaths / 100 Recovered', 'Confirmed last week', '1 week change',
                '1 week % increase']

for col in numeric_cols:
    ddf[col] = dd.to_numeric(ddf[col], errors='coerce')

ddf = ddf.fillna(0)

print("\n--- Data Preprocessing  ---")

# --- 3. Analysis Tasks ---

# Task 1: Top 5 Countries by Confirmed Cases
print("\n--- Task 1: Top 5 Countries by Confirmed Cases ---")
top_confirmed = ddf[['Country', 'Confirmed']].nlargest(5, 'Confirmed').compute()
print(top_confirmed)
top_confirmed.to_csv(os.path.join(dir, 'top_5_confirmed_countries.csv'), index=False)

# Task 2: Top 5 Countries by Deaths
print("\n--- Task 2: Top 5 Countries by Deaths ---")
top_deaths = ddf[['Country', 'Deaths']].nlargest(5, 'Deaths').compute()
print(top_deaths)
top_deaths.to_csv(os.path.join(dir, 'top_5_deaths_countries.csv'), index=False)

# Task 3: Top 5 Countries by Recovered Cases
print("\n--- Task 3: Top 5 Countries by Recovered Cases ---")
top_recovered = ddf[['Country', 'Recovered']].nlargest(5, 'Recovered').compute()
print(top_recovered)
top_recovered.to_csv(os.path.join(dir, 'top_5_recovered_countries.csv'), index=False)

# Task 4: Average 'Deaths / 100 Cases' and 'Recovered / 100 Cases' 
print("\n--- Task 4: Average Metrics per WHO Region ---")
region_averages = ddf.groupby('WHO Region')[['Deaths / 100 Cases', 'Recovered / 100 Cases']].mean().compute()
print(region_averages)
region_averages.to_csv(os.path.join(dir,'region_averages.csv'))


print("\n--- Demonstrating the complex Dask operation  ---")
# Calculate a new column 'Active_Ratio' and then find the max per region
ddf['Active_Ratio'] = ddf['Active'] / ddf['Confirmed']
max_active_ratio_per_region = ddf.groupby('WHO Region')['Active_Ratio'].max().compute()
print("\nMax Active Ratio per WHO Region:")
print(max_active_ratio_per_region)
max_active_ratio_per_region.to_csv(os.path.join(dir, 'max_active_ratio_per_region.csv'))

print(f"\n Big Data Analysis Has Completed Using Dask. ")
