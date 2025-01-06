from google.cloud import bigquery
import pandas as pd
from google.colab import auth  # Import auth for authentication

# Authenticate user
auth.authenticate_user()

# Define your project ID
project_id = 'binance-bot-442813'

# Create a BigQuery client
client = bigquery.Client(project=project_id)

# Define your SQL query
query = """
SELECT *
FROM `binance-bot-442813.BIG_FIVE.UNION_ALL`

"""

# Execute the query and convert the result to a Pandas DataFrame
query_job = client.query(query)
df = query_job.to_dataframe()

# Assign the retrieved DataFrame to combined_data
combined_data = df

# Display the first few rows of combined_data
print(combined_data.head())

# Verify the actual column names in the DataFrame
print("Columns in combined_data:")
print(combined_data.columns)

# Corrected column names for analysis
columns_to_analyze = [
    'Open', 'Close', 'High', 'Low',
    'Cumulative_Return', 'Daily_Return', 'Daily_Volatility'
]

# Calculate mean and standard deviation for the entire dataset
overall_mean = combined_data[columns_to_analyze].mean()
overall_std = combined_data[columns_to_analyze].std()

print("\nOverall Mean:")
print(overall_mean)
print("\nOverall Standard Deviation:")
print(overall_std)

# Step 3: Calculate statistics per coin (optional)
if 'ticker' in combined_data.columns:
    grouped_stats = combined_data.groupby('ticker')[columns_to_analyze].agg(['mean', 'std'])
    print("\nPer-Coin Statistics:")
    print(grouped_stats)