import os
import subprocess
import sqlite3

# Database and table information
database_name = "data_challenge.db"
table_name = "player_pos"

# Directory containing CSV files and its subdirectories
csv_directory = "/Users/gaberiedel/Downloads/smt_data_challenge_2023/player_pos"

# Function to import CSV files into the table
def import_csv_files(cursor, csv_directory, table_name):
    for root, dirs, files in os.walk(csv_directory):
        for csv_file in files:
            if csv_file.endswith(".csv"):
                csv_path = os.path.join(root, csv_file)
                subprocess.run(["sqlite3", database_name, f".mode csv", f".import {csv_path} {table_name}"])
                print(f"Imported {csv_file} into {table_name}")

# Connect to the SQLite database
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Import CSV files from all subdirectories into the table
import_csv_files(cursor, csv_directory, table_name)

# Commit changes and close connection
conn.commit()
conn.close()

print("All CSV files imported successfully.")
