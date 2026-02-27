# This repo contains notional claims data that we can use to both tech screen deployment strategists and to practice data pipelining for FDEs / Devs

## What is it

A bunch of csv files that can be joined together. 

#### Available Tables

- `patient`
- `provider`
- `diagnosis`
- `procedure`
- `medical_claim`
- `pharmacy_claim`

### Excel workflow

Open the first CSV in excel or gsheets. Open another CSV in the same excel in a new sheet. Use vlookups to connect the datasets together. 

### SQL workflow

Clone the repo or download from github. Assuming you have python installed, you can write the CSVs into a sqlite db like so:

```bash
python3 import_csvs.py
```

This script will:
- Create `data.sqlite3` database (removes existing one if present)
- Import all CSV files as tables: `patient`, `provider`, `diagnosis`, `procedure`, `medical_claim`, `pharmacy_claim`

Now you can query this data in sql. 

```bash
% sqlite3 data.sqlite3
sqlite> SELECT * FROM patient LIMIT 10;
```

### Python workflow

Clone the repo and install dependencies using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
python3 import_csvs.py

```

That's it — `uv` will create a virtual environment and install all dependencies automatically.

### Interactive Notebook (Marimo)

To explore the data interactively, launch the included Marimo notebook:

```bash
uv run marimo edit notebook.py
```

### Querying the Data with Python (Polars)

Once dependencies are installed, you can load and query the CSV files directly using `polars`. Here's an example of how to get started in a Python script or the Marimo notebook:

```python
import polars as pl

# Load the CSV files into DataFrames
df_patient = pl.read_csv("patient.csv")
df_provider = pl.read_csv("provider.csv")
df_diagnosis = pl.read_csv("diagnosis.csv")
df_procedure = pl.read_csv("procedure.csv")
df_medical_claim = pl.read_csv("medical_claim.csv")
df_pharmacy_claim = pl.read_csv("pharmacy_claim.csv")

# Example: Join patient with medical_claim on a key (e.g., patient_id)
df = df_patient.join(df_medical_claim, on="patient_id", how="inner")

# Show the first five rows
print(df.head())
```

