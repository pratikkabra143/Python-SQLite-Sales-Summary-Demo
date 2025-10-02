# Python-SQLite-Sales-Summary-Demo

---

## 🎯 Objective: Generate a basic sales summary from a tiny SQLite database using Python, displaying total quantity sold and revenue per product using basic print statement and a simple bar chart.

### ⚙️ Tools Used: Python (`sqlite3`, `pandas`, `matplotlib`), SQLite

---

## 🛢️ Dataset
A small SQLite database `sales_data.db` located in the `data/` folder.  

- Database created using the included script `create_sales_db.py` (also in `data/`)  
- Table: `sales`  
- Relevant Columns:
  - `id` → unique row identifier
  - `product` → product name
  - `quantity` → quantity sold
  - `price` → price per unit

- Sample products included: Laptop, Mouse, Keyboard, Monitor, Headphones, Charger, Webcam, Tablet, Speaker, Smartwatch  

> The database and `create_sales_db.py` are present in the `data/` folder for reproducibility.

---

## 🛠 Deliverables
The following steps were performed for demonstration purposes on the database:

1. **Database Setup**
   - `data/sales_data.db` created using `data/create_sales_db.py`.
   - Sample rows inserted for demonstration.

2. **Python Script (`sales_summary.py`)**
   - Connects to `data/sales_data.db`.
   - Runs a SQL query to calculate:
     - Total quantity sold per product
     - Total revenue per product
   - Prints the results in the console.
   - Plots a simple bar chart of revenue per product.
   - Saves the chart to `outputs/sales_chart.png`.

3. **Outputs**
   - Bar chart saved in `outputs/` folder.
   - Printed summary shown in console after running the script.

---

## 📂 Project Structure

```
Python-SQLite-Sales-Summary-Demo/
├── data/
│    ├── create_sales_db.py  # Script to create the database locally
│    └── sales_data.db       # SQLite database created using create_sales_db.py
├── outputs/
│    └── sales_chart.png     # Bar chart showing Revenue per Product
├── README.md                # Project explanation
├── requirements.txt         # Requirements file for python dependencies
└── sales_summary.py         # Main script performing analysis
```

---

## 🚀 How to Reproduce

1. **Setup Environment:**
   - python -m venv .sqlite_summary
   - .\\.sqlite_summary\Scripts\Activate.ps1 (for Windows, find accordingly for other OSes)
   - python -m pip install -r requirements.txt
2. Create dummy database using `data/create_sales_db.py` or use existing if you have or `data/sales_data.db`. For creation:
   - python data/create_sales_db.py
3. Run the main script as-
   - python sales_summary.py
   - The console will display the sales summary table.
   - The chart will be automatically saved as the `sales_chart.png` in `outputs/` folder.

---
