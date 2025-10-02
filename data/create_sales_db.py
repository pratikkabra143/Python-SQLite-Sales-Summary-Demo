import sqlite3

sample_data = [
    ("Laptop", 5, 70000.0),
    ("Laptop", 3, 70000.0),
    ("Mouse", 10, 500.0),
    ("Mouse", 15, 500.0),
    ("Keyboard", 8, 1500.0),
    ("Keyboard", 12, 1500.0),
    ("Monitor", 4, 12000.0),
    ("Monitor", 6, 12000.0),
    ("Headphones", 7, 3000.0),
    ("Headphones", 3, 3000.0),
    ("Charger", 25, 699.0),
    ("Webcam", 5, 2500.0),
    ("Webcam", 2, 2500.0),
    ("Tablet", 4, 25000.0),
    ("Speaker", 20, 1999.0),
    ("Smartwatch", 6, 8000.0)
]

def create_db(db_path='sales_data.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    );
    """)
    # Remove old demo rows (if any) then insert sample data
    cursor.execute("DELETE FROM sales;")
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?);", sample_data)
    conn.commit()
    conn.close()
    print(f"Created {db_path} with sample sales data.")


if __name__ == '__main__':
    create_db()
