import pandas as pd
import matplotlib.pyplot as plt

# Read the original CSV file into a DataFrame
df = pd.read_csv('Tourism.csv')

# Convert columns to numeric types
df['Trips Ending March 2019'] = pd.to_numeric(df['Trips Ending March 2019'], errors='coerce')
df['Trips Ending March 2024'] = pd.to_numeric(df['Trips Ending March 2024'], errors='coerce')
df['Spend Ending March 2019'] = pd.to_numeric(df['Spend Ending March 2019'], errors='coerce')
df['Spend Ending March 2024'] = pd.to_numeric(df['Spend Ending March 2024'], errors='coerce')

# Handle NaN values (optional)
df.fillna(0, inplace=True)  # Replaces NaNs with 0s

# Save the cleaned DataFrame to a new CSV file
df.to_csv('Tourism_cleaned.csv', index=False)

# Read the cleaned CSV file into a new DataFrame
new_df = pd.read_csv('Tourism_cleaned.csv')

# Print the cleaned data to the console
#print(new_df)

# Calculate the total number of people that traveled in 2019
total_2019 = new_df['Trips Ending March 2019'].sum()

# Calculate the total number of people that traveled in 2024
total_2024 = new_df['Trips Ending March 2024'].sum()

# Print the totals
print(f'Total number of travelers in 2019: {total_2019}') 
print(f'Total number of travelers in 2024: {total_2024}')

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(['2019', '2024'], [total_2019, total_2024], color=['blue', 'orange'])
plt.xlabel('Year')
plt.ylabel('Total Number of Travelers')
plt.title('Total Number of Travelers in 2019 vs. 2024')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a PNG file
plt.savefig('Travelers_Comparison.png')

# Show the plot
plt.show()



#Find the top five countries 

top_countries = new_df.groupby('Country')

top_countries = top_countries.sum()

top_countries = top_countries.sort_values(['Trips Ending March 2024'], ascending=False)

top_countries.head(5)

top_5_countries = top_countries.head(5)

print(top_5_countries)



#Find the top 5 spending countries

spending_countries = new_df.groupby('Country')

spending_countries = spending_countries.sum()

spending_countries = spending_countries.sort_values(['Spend Ending March 2024'], ascending=False)

top_5_spending_countries = spending_countries.head(5)

print("Top 5 countries by spending in 2024:")
print(top_5_spending_countries)


#Make the menu line system 
print('Hello and welcome to ....')
option = input('Select what you would like to know: 1 - top 5 spending countries, 2 - show a graph comparing travellers in 2019 and 2024')

if option == '1':
   print(top_5_spending_countries)

elif option == '2':
   plt.savefig('Travelers_Comparison.png')
else:
   print('Unknown value. Please select 1, 2 or 3.')