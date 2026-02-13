# Querying the SQLite Database

## Setup

Import CSV files into the SQLite database:

```bash
python3 import_csvs.py
```

This script will:
- Create `data.sqlite3` database (removes existing one if present)
- Import all CSV files: `patient.csv`, `provider.csv`, `diagnosis.csv`, `procedure.csv`, `medical_claim.csv`, `pharmacy_claim.csv`

**Note:** No external Python packages are required - the script uses only Python standard library.

## Quick Start

Query the database using the `sqlite3` command-line tool:

```bash
sqlite3 data.sqlite3 "SELECT * FROM patient LIMIT 10;"
```

## Available Tables

- `patient`
- `provider`
- `diagnosis`
- `procedure`
- `medical_claim`
- `pharmacy_claim`

## Example Query

View all columns from the patient table:

```bash
sqlite3 data.sqlite3 "SELECT * FROM patient LIMIT 10;"
```

For better formatting with headers:

```bash
sqlite3 data.sqlite3 -header -column "SELECT * FROM patient LIMIT 10;"
```
