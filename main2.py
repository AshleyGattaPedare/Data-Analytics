import pandas as pd
import matplotlib.pyplot as plt

# Read the original CSV file into a DataFrame
travel_data = pd.read_csv('Reasons_For_Travel.csv')

# Strip any leading or trailing whitespace from column names
travel_data.columns = travel_data.columns.str.strip()

# Print the column names to check if they match what you expect
print("Columns in the dataset:", travel_data.columns)

# Convert columns to string type and remove commas, then convert to numeric
columns_to_convert = [
    'Trips Ending March 2019', 
    'Trips Ending March 2024', 
    'Spend Ending March 2019', 
    'Spend Ending March 2024'
]

for column in columns_to_convert:
    if column in travel_data.columns:
        # Convert to string, replace commas, then convert to numeric
        travel_data[column] = travel_data[column].astype(str).str.replace(',', '', regex=False)
        travel_data[column] = pd.to_numeric(travel_data[column], errors='coerce')

# Handle NaN values (optional)
travel_data.fillna(0, inplace=True)  # Replaces NaNs with 0s

# Save the cleaned DataFrame to a new CSV file
travel_data.to_csv('Reasons_For_Travel_cleaned.csv', index=False)

# Read the cleaned CSV file into a new DataFrame
cleaned_travel_data = pd.read_csv('Reasons_For_Travel_cleaned.csv')

# Print the cleaned data to the console
print(cleaned_travel_data)
