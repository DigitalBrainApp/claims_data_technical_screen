#!/usr/bin/env python3
"""
Script to import CSV files into SQLite database.
"""

import sqlite3
import csv
import os

# Database file
DB_FILE = 'data.sqlite3'

# CSV files to import
CSV_FILES = [
    'patient.csv',
    'provider.csv',
    'diagnosis.csv',
    'procedure.csv',
    'medical_claim.csv',
    'pharmacy_claim.csv'
]

def get_column_type(value):
    """Infer SQLite column type from a sample value."""
    if value == '':
        return 'TEXT'
    try:
        int(value)
        return 'INTEGER'
    except ValueError:
        try:
            float(value)
            return 'REAL'
        except ValueError:
            return 'TEXT'

def create_table_from_csv(cursor, csv_file, table_name):
    """Create a table from CSV file structure."""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        # Read first data row to infer types
        try:
            first_row = next(reader)
        except StopIteration:
            first_row = []
        
        # Build column definitions
        columns = []
        for i, header in enumerate(headers):
            col_name = header.lower().replace(' ', '_')
            if i < len(first_row):
                col_type = get_column_type(first_row[i])
            else:
                col_type = 'TEXT'
            columns.append(f"{col_name} {col_type}")
        
        # Create table
        create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        cursor.execute(create_sql)
        
        # Reset file pointer
        f.seek(0)
        reader = csv.reader(f)
        next(reader)  # Skip header
        
        # Insert data
        placeholders = ','.join(['?' for _ in headers])
        insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        
        rows = []
        for row in reader:
            # Pad row if necessary
            while len(row) < len(headers):
                row.append('')
            rows.append(row)
            # Insert in batches for better performance
            if len(rows) >= 1000:
                cursor.executemany(insert_sql, rows)
                rows = []
        
        # Insert remaining rows
        if rows:
            cursor.executemany(insert_sql, rows)

def main():
    """Main function to import all CSV files."""
    # Remove existing database if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Removed existing {DB_FILE}")
    
    # Connect to database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        for csv_file in CSV_FILES:
            if not os.path.exists(csv_file):
                print(f"Warning: {csv_file} not found, skipping...")
                continue
            
            table_name = os.path.splitext(csv_file)[0]
            print(f"Importing {csv_file} into table {table_name}...")
            
            create_table_from_csv(cursor, csv_file, table_name)
            conn.commit()
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"  Imported {count} rows into {table_name}")
        
        print("\nAll CSV files imported successfully!")
        
        # Show table summary
        print("\nDatabase summary:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        for (table_name,) in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"  {table_name}: {count} rows")
    
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        raise
    
    finally:
        conn.close()

if __name__ == '__main__':
    main()
