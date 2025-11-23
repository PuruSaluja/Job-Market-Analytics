import pandas as pd
import os
import re

# Configuration
INPUT_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\data\raw\synthetic_job_postings.csv"
OUTPUT_DIR = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\data\processed"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cleaned_job_postings.csv")

def clean_salary(salary_str):
    if pd.isna(salary_str):
        return None, None, None
    
    # Remove '$' and 'K' and other chars
    clean_str = salary_str.replace('$', '').replace('K', '').replace(',', '')
    
    # Extract numbers
    matches = re.findall(r'\d+', clean_str)
    if len(matches) >= 2:
        min_sal = float(matches[0]) * 1000
        max_sal = float(matches[1]) * 1000
        avg_sal = (min_sal + max_sal) / 2
        return min_sal, max_sal, avg_sal
    elif len(matches) == 1:
        val = float(matches[0]) * 1000
        return val, val, val
    else:
        return None, None, None

def main():
    print("Starting data cleaning...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file {INPUT_FILE} not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    
    # 1. Clean Salary
    print("Cleaning salaries...")
    salary_data = df['Salary Estimate'].apply(clean_salary)
    df['Min Salary'] = [x[0] for x in salary_data]
    df['Max Salary'] = [x[1] for x in salary_data]
    df['Avg Salary'] = [x[2] for x in salary_data]
    
    # 2. Parse Dates
    print("Parsing dates...")
    df['Date Posted'] = pd.to_datetime(df['Date Posted'])
    
    # 3. Standardize Job Titles (Simple Lowercase and Strip)
    print("Standardizing job titles...")
    df['Job Title Clean'] = df['Job Title'].str.lower().str.strip()
    
    # 4. Remove Duplicates
    print("Removing duplicates...")
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    final_count = len(df)
    print(f"Removed {initial_count - final_count} duplicates.")
    
    # Ensure directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Successfully saved cleaned data to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
