import pandas as pd
import matplotlib.pyplot as plt

# monthly spending
# monthly balance growth
# group spending categories
# create a budget for each spending categories to reach a goal

# Replace 'transactions.csv' with the path to your CSV file
csv_file = 'back_end/bank_transactions_test.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

df['WITHDRAWAL AMT'] = pd.to_numeric(df['WITHDRAWAL AMT'], errors='coerce')

# Perform data manipulation, e.g., getting summary statistics
total_amount = df['WITHDRAWAL AMT'].sum()
average_amount = df['WITHDRAWAL AMT'].mean()
months = df['DATE'].str.split('-').str.get(1)
monthly_spending = {
    "Jan": None,
    "Feb": None,
    "Mar": None,
    "Apr": None,
    "May": None,
    "Jun": None,
    "Jul": None,
    "Aug": None,
    "Sep": None,
    "Oct": None,
    "Nov": None,
    "Dec": None
}

for month, withdrawal_amount in zip(months, df['WITHDRAWAL AMT']):
    if monthly_spending[month] is None:
        monthly_spending[month] = withdrawal_amount
    else:
        monthly_spending[month] += withdrawal_amount


# Display the results
print('Total Amount:', total_amount)
print('Average Amount:', average_amount)
print('Months: ', monthly_spending)

keys = list(monthly_spending.keys())
values = list(monthly_spending.values())

# Create a line plot using plt.plot()
plt.plot(keys, values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Amount Spent')
plt.title('Monthly Spending')

# Display the plot
plt.show()
