# Querying the SQLite Database

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
