import pandas as pd

# Example: Assuming 'df' has the columns 'ticker', 'Date', 'Open', 'Close', 'High', 'Low', etc.
# Ensure the 'Date' column is in datetime format and sorted by 'ticker' and 'Date'
combined_data['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['ticker', 'Date'])

# Define the window size for the moving average (e.g., 7-day moving average)
window_size = 7

# Columns to calculate the moving average for
columns_to_average = ['Open', 'Close', 'High', 'Low', 'Cumulative_Return', 'Daily_Return', 'Daily_Volatility']

# Calculate the moving average for each specified column for each coin (ticker)
for column in columns_to_average:
    df[f'{column}_moving_average'] = df.groupby('ticker')[column].rolling(window=window_size, min_periods=1).mean().reset_index(level=0, drop=True)

# Show the result
print(df.head())