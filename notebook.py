import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Claims Data Explorer
    """)
    return


@app.cell
def _():
    import sqlite3
    conn = sqlite3.connect("data.sqlite3")
    return (conn,)


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
def _(conn, medical_claim, mo, patient):
    _df = mo.sql(
        f"""
        SELECT * FROM medical_claim LEFT JOIN patient on medical_claim.patient_id = patient.patient_id
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
