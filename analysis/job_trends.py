import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

# Configuration
DB_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\jobs.db"
OUTPUT_DIR = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\analysis\plots"

def main():
    print("Generating trend charts...")
    if not os.path.exists(DB_FILE):
        print(f"Error: DB file {DB_FILE} not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    
    # Load Data
    df = pd.read_sql("SELECT * FROM jobs_clean", conn)
    skills_df = pd.read_sql("""
        SELECT s.skill_name, js.job_id 
        FROM skills_lookup s 
        JOIN job_skills js ON s.skill_id = js.skill_id
    """, conn)
    
    # 1. Salary Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['avg_salary'].dropna(), bins=20, edgecolor='black')
    plt.title('Salary Distribution')
    plt.xlabel('Average Salary')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(OUTPUT_DIR, "salary_distribution.png"))
    plt.close()
    
    # 2. Top 20 Skills
    top_skills = skills_df['skill_name'].value_counts().head(20)
    plt.figure(figsize=(12, 8))
    plt.barh(top_skills.index, top_skills.values)
    plt.title('Top 20 Most Demanded Skills')
    plt.xlabel('Count')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "top_skills.png"))
    plt.close()
    
    # 3. Job Titles
    top_titles = df['job_title_clean'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_titles.index, top_titles.values)
    plt.title('Top 10 Job Titles')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "top_job_titles.png"))
    plt.close()
    
    conn.close()
    print(f"Charts saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
