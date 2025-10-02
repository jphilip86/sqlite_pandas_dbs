# sqlite_pandas_dbs
507 Assignment 2  Single-Table Patient Roster in SQLite
Two-step workflow: (1) create DB with Python, (2) load CSV with Pandas/SQLAlchemy; then run simple queries.

# Learning goals
Create a stand-alone .sql schema for a single table.
Use Python (sqlite3) to create an SQLite database from a schema file.Load a CSV into SQLite with Pandas + SQLAlchemy.Write and run single-table SELECT queries in DB Browser for SQLite.

# Steps (how to recreate the database)

1. I made a repo in Github under the name "sqlite_pandas_dbs" with Readme file.
2. I cloned the repo in vscode and arranged the folder structure as given.
3. I moved the patients.csv file into the data folder
4. I created the create_db python file under folder src.
5. After trial and error I was able to create clinic_simple.db file based on the previous class ( creation of sql database).
6. I used the given script as it was simpler and added executescript as an option to run multiple SQL queries.
7. I made the schema.sql with the given structure.
8. After many errors I was able to reproduce and understand each line as to why I need to apply the schema to the clinic_simple.db
9. I then created the import_csv python file and used the sql engine to connect the python code to the sqlite database in effect creating an "engine" object – the pipe to the SQLite database.
10. Then I read the csv file to pandas dataframe.
11. The df.to_sql code sent all the rows in the dataframe to the sqlite database.
12. Finally it printed a summary of how many rows were added.
13. Then I opened DB browser and ran the given queries which are noted below. 


# Query results section: 
For each query (A-E) in analysis.sql, include:
1.The query description
2.A screenshot or text output of the results from DB Browser
3.1-2 sentence explanation of what the results show


# A. Row count
![Screenshot](data/sql%20screenshots/Screenshot%202025-10-02%20162947.png)

The patients table contains exactly 500 records, as shown by the query result. This confirms the database import was successful and matches the expected dataset size.

# B. Top primary diagnoses by count
![Screenshot](data/sql%20screenshots/Screenshot%202025-10-02%20163152.png)

I10 is the most frequent primary diagnosis with 81 cases, followed by E11.9 and E78.5, indicating common conditions among this clinic's patient population. The result ranks all ICD-10 codes by the number of patients assigned each code.



# C. Office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992)
![Screenshot](data/sql%20screenshots/Screenshot%202025-10-02%20163451.png)

There are 94 office visits matching CPT codes starting with '992' and dated on or after January 1, 2025. The query returns recent patient visits, sorted from most to least recent.



# D. Age (approx) at last visit for the 5 oldest patients
![Screenshot](data/sql%20screenshots/Screenshot%202025-10-02%20163801.png)

The five oldest patients in the system are each 85 years old, with birth dates in 1940. The query shows their most recent visit dates, indicating these older patients remain actively followed.

# E. Quick data quality check: any blank codes?
![Screenshot](data/sql%20screenshots/Screenshot%202025-10-02%20163908.png)

No records were found with a blank primary_icd10 or last_cpt code. This means the dataset’s diagnostic and CPT code columns are fully populated, with no missing values.
