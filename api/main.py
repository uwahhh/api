import sqlite3

dbpath = r"C:\Users\coolz\Downloads\corpus.db"  # Adjust based on actual location
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in corpus.db:", tables)

# Check first few rows of a table
table_name = tables[0][0]  # Select first table
cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
rows = cursor.fetchall()
print("Sample rows:", rows)

conn.close()
