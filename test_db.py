"""
Week 0 sanity check: confirm Python can connect to MySQL and read the data.
Run with:  ./venv/bin/python test_db.py
"""
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # reads .env

conn = mysql.connector.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
)
cur = conn.cursor()

for table in ("rets_property", "california_sold", "rets_openhouse"):
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"{table:18} {cur.fetchone()[0]:>10,} rows")

# A real sample query, like Week 2 will use
cur.execute(
    "SELECT L_Address, L_City, L_SystemPrice "
    "FROM rets_property WHERE L_City = 'Irvine' AND L_Status = 'Active' "
    "LIMIT 3"
)
print("\nSample active Irvine listings:")
for addr, city, price in cur.fetchall():
    print(f"  {addr}, {city} — ${price:,}")

cur.close()
conn.close()
print("\n✅ Python ↔ MySQL connection works.")
