import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("data/sales_data.db")

query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

print(df)

df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

plt.savefig("outputs/sales_chart.png")

conn.close()