import pandas as pd
import random
import datetime
import os

# Configuration
OUTPUT_DIR = r"C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\data\raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "synthetic_job_postings.csv")
NUM_RECORDS = 1000

# Sample Data for Generation
JOB_TITLES = [
    "Data Analyst", "Senior Data Analyst", "Junior Data Analyst", "Business Intelligence Analyst",
    "Data Scientist", "Data Engineer", "Analytics Consultant", "Marketing Analyst",
    "Financial Analyst", "Product Analyst", "Machine Learning Engineer", "BI Developer"
]

COMPANIES = [
    "TechCorp", "DataWiz", "Innovate Solutions", "FinancePlus", "HealthCare Inc.",
    "RetailGiants", "EduTech", "GreenEnergy", "CyberSecure", "CloudSystems",
    "Alpha Analytics", "Beta Data", "Gamma Group", "Delta Dynamics"
]

LOCATIONS = [
    "New York, NY", "San Francisco, CA", "Austin, TX", "Chicago, IL", "Seattle, WA",
    "Boston, MA", "Los Angeles, CA", "Denver, CO", "Atlanta, GA", "Remote",
    "London, UK", "Toronto, ON", "Berlin, DE", "Bangalore, IN"
]

SKILLS = [
    "SQL", "Python", "Excel", "Tableau", "Power BI", "R", "AWS", "Azure", "Google Cloud",
    "Machine Learning", "Statistics", "Spark", "Hadoop", "Snowflake", "Looker", "Jira",
    "Git", "Docker", "Kubernetes", "Airflow"
]

DESCRIPTIONS_TEMPLATES = [
    "We are looking for a {title} to join our team. You will be working with {skills}.",
    "Exciting opportunity for a {title} at {company}. Must have experience in {skills}.",
    "Join {company} as a {title}. Key skills required: {skills}.",
    "Seeking a talented {title}. Proficiency in {skills} is a must.",
    "{company} is hiring a {title}. You should know {skills}."
]

def generate_salary():
    min_sal = random.randint(50, 120) * 1000
    max_sal = min_sal + random.randint(10, 50) * 1000
    return f"${min_sal//1000}K-${max_sal//1000}K"

def generate_description(title, company):
    num_skills = random.randint(3, 8)
    selected_skills = random.sample(SKILLS, num_skills)
    skills_str = ", ".join(selected_skills)
    template = random.choice(DESCRIPTIONS_TEMPLATES)
    return template.format(title=title, company=company, skills=skills_str)

def generate_date():
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2025, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def main():
    print("Generating synthetic data...")
    data = []
    
    for _ in range(NUM_RECORDS):
        title = random.choice(JOB_TITLES)
        company = random.choice(COMPANIES)
        location = random.choice(LOCATIONS)
        salary = generate_salary()
        description = generate_description(title, company)
        date_posted = generate_date()
        rating = round(random.uniform(3.0, 5.0), 1)
        
        data.append({
            "Job Title": title,
            "Company Name": company,
            "Location": location,
            "Salary Estimate": salary,
            "Job Description": description,
            "Rating": rating,
            "Date Posted": date_posted
        })
        
    df = pd.DataFrame(data)
    
    # Ensure directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Successfully generated {NUM_RECORDS} records to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
