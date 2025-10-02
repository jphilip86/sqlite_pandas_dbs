import pandas as pd
from sqlalchemy import create_engine

# Paths to files
# SQLAlchemy connection string for SQLite
DB_PATH = 'sqlite:///clinic_simple.db'  
CSV_PATH = "./data/patients.csv"



# Create SQLAlchemy engine
engine = create_engine(DB_PATH)

# Load the CSV data into a DataFrame
df = pd.read_csv(CSV_PATH)

# Append the DataFrame rows into the 'patients' table
df.to_sql('patients', con=engine, if_exists='append', index=False)


print(f"Appended {len(df)} rows from {CSV_PATH} into the 'patients' table.")

