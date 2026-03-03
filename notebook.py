import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""
    # Claims Data Explorer
    """)
    return


@app.cell
def _():
    import marimo as mo
    import sqlite3
    conn = sqlite3.connect("data.sqlite3")
    return conn, mo


@app.cell
def _(conn, mo, patient):
    patients = mo.sql(
        f"""
        SELECT * FROM patient LIMIT 10
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo, patient):
    patients = mo.sql("SELECT * FROM patient", engine=conn)
    patients.head(10)
    return


if __name__ == "__main__":
    app.run()
