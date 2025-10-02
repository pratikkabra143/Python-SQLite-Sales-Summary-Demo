# sales_summary.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Connect to the SQLite database
conn = sqlite3.connect("data/sales_data.db")

# Step 2: Run SQL query to get total quantity sold and revenue per product
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Print the results
print("Sales Summary:")
print(df)

# Step 4: Create outputs folder if it doesn't exist
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# Step 5: Plot a simple bar chart of revenue per product
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/sales_chart.png") # save chart
plt.show()

# Step 6: Close the database connection
conn.close()