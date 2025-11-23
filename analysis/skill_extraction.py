import pandas as pd
import sqlite3
import os
import re

# Configuration
DB_FILE = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\jobs.db"
OUTPUT_DIR = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\analysis"
SKILLS_EXTRACTED_FILE = os.path.join(OUTPUT_DIR, "skills_extracted.csv")
JOB_SKILL_MATRIX_FILE = os.path.join(OUTPUT_DIR, "job_skill_matrix.csv")

# Expanded Skill List
SKILLS_LIST = [
    "SQL", "Python", "Excel", "Tableau", "Power BI", "R", "AWS", "Azure", "Google Cloud",
    "Machine Learning", "Statistics", "Spark", "Hadoop", "Snowflake", "Looker", "Jira",
    "Git", "Docker", "Kubernetes", "Airflow", "Java", "C++", "Scala", "NoSQL", "MongoDB",
    "PostgreSQL", "Redshift", "BigQuery", "Databricks", "SAS", "SPSS", "Matlab", "TensorFlow",
    "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy", "Seaborn", "Matplotlib", "Plotly",
    "D3.js", "React", "Angular", "Vue", "Flask", "Django", "FastAPI", "HTML", "CSS", "JavaScript"
]

def extract_skills(description):
    if not isinstance(description, str):
        return []
    
    found_skills = []
    for skill in SKILLS_LIST:
        # Regex for word boundary to avoid partial matches (e.g., "R" in "Rest")
        # Escape special chars like C++
        escaped_skill = re.escape(skill)
        pattern = r'\b' + escaped_skill + r'\b'
        if skill == "C++": # Special case for C++
             pattern = r'C\+\+'
        
        if re.search(pattern, description, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

def main():
    print("Starting Skill Extraction...")
    if not os.path.exists(DB_FILE):
        print(f"Error: DB file {DB_FILE} not found.")
        return

    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT id, job_description FROM jobs_clean", conn)
    
    print(f"Processing {len(df)} job descriptions...")
    
    all_job_skills = []
    
    for index, row in df.iterrows():
        job_id = row['id']
        desc = row['job_description']
        skills = extract_skills(desc)
        
        for skill in skills:
            all_job_skills.append({'job_id': job_id, 'skill_name': skill})
            
    skills_df = pd.DataFrame(all_job_skills)
    
    if skills_df.empty:
        print("No skills extracted.")
        conn.close()
        return

    # Save to CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    skills_df.to_csv(SKILLS_EXTRACTED_FILE, index=False)
    print(f"Saved extracted skills to {SKILLS_EXTRACTED_FILE}")
    
    # Create Matrix
    matrix_df = pd.crosstab(skills_df['job_id'], skills_df['skill_name'])
    matrix_df.to_csv(JOB_SKILL_MATRIX_FILE)
    print(f"Saved job-skill matrix to {JOB_SKILL_MATRIX_FILE}")
    
    # Load to SQL
    print("Loading skills to SQL...")
    
    # 1. skills_lookup
    unique_skills = skills_df['skill_name'].unique()
    skills_lookup_df = pd.DataFrame(unique_skills, columns=['skill_name'])
    skills_lookup_df.to_sql('skills_lookup', conn, if_exists='append', index=False)
    
    # Get skill_ids back
    skills_lookup_db = pd.read_sql("SELECT * FROM skills_lookup", conn)
    skill_map = dict(zip(skills_lookup_db['skill_name'], skills_lookup_db['skill_id']))
    
    # 2. job_skills
    skills_df['skill_id'] = skills_df['skill_name'].map(skill_map)
    job_skills_final = skills_df[['job_id', 'skill_id']]
    job_skills_final.to_sql('job_skills', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    print("Successfully loaded skills into SQL.")

if __name__ == "__main__":
    main()
