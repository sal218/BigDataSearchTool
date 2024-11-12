import pandas as pd
import sqlite3

# load the CSV file
data = pd.read_csv("realtor-data.zip.csv")

# filter only properties with status 'for_sale'
data = data[data['status'] == 'for_sale']

# drop unnecessary columns from dataset 
data = data.drop(columns=["acre_lot", "brokered_by", "prev_sold_date"])

# drop rows with null values
data = data.dropna()

# Clean up the 'street' column to remove trailing '.0' if it exists
data['street'] = data['street'].apply(lambda x: str(int(x)) if isinstance(x, float) else x.rstrip('.0') if isinstance(x, str) and x.endswith('.0') else x)

# Ensure 'zip_code' is treated as a string
# Clean up the 'street' column to remove trailing '.0' if it exists
data['zip_code'] = data['zip_code'].apply(lambda x: str(int(x)) if isinstance(x, float) else x.rstrip('.0') if isinstance(x, str) and x.endswith('.0') else x)


# check if we have at least 500,000 rows after filtering (I reduced original dataset from 2.5 million to 500k but we can always keep full dataset)
if len(data) >= 500000:
    sampled_data = data.sample(n=500000, random_state=42)
else:
    sampled_data = data  # Use the entire filtered dataset if less than 500,000 rows

# Connect to a new SQLite database
conn = sqlite3.connect("real_estate_new.db")

# Save the sampled data to a table in the database
sampled_data.to_sql("properties", conn, if_exists="replace", index=False)

# Close the connection
conn.close()
