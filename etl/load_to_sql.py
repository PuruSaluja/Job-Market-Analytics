import pandas as pd
import sqlite3
import os

# Configuration
INPUT_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\data\processed\cleaned_job_postings.csv"
DB_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\jobs.db"
SCHEMA_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\sql\schema.sql"

def main():
    print("Loading data to SQL...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file {INPUT_FILE} not found.")
        return

    # Connect to DB
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Execute Schema
    with open(SCHEMA_FILE, 'r') as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
    
    # Load Data
    df = pd.read_csv(INPUT_FILE)
    
    # Rename columns to match SQL schema
    df.rename(columns={
        'Job Title': 'job_title',
        'Company Name': 'company_name',
        'Location': 'location',
        'Salary Estimate': 'salary_estimate',
        'Job Description': 'job_description',
        'Rating': 'rating',
        'Date Posted': 'date_posted',
        'Min Salary': 'min_salary',
        'Max Salary': 'max_salary',
        'Avg Salary': 'avg_salary',
        'Job Title Clean': 'job_title_clean'
    }, inplace=True)

    # Insert into jobs_clean
    print("Inserting into jobs_clean...")
    df.to_sql('jobs_clean', conn, if_exists='append', index=False)
    
    # Populate companies table (simple aggregation)
    print("Populating companies table...")
    companies = df.groupby('company_name')['rating'].mean().reset_index()
    companies.columns = ['company_name', 'avg_rating']
    companies.to_sql('companies', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    print(f"Successfully loaded data into {DB_FILE}")

if __name__ == "__main__":
    main()
