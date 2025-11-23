-- Schema for Job Market Analytics

DROP TABLE IF EXISTS jobs_clean;
DROP TABLE IF EXISTS skills_lookup;
DROP TABLE IF EXISTS job_skills;
DROP TABLE IF EXISTS companies;

CREATE TABLE jobs_clean (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company_name TEXT,
    location TEXT,
    salary_estimate TEXT,
    job_description TEXT,
    rating REAL,
    date_posted DATE,
    min_salary REAL,
    max_salary REAL,
    avg_salary REAL,
    job_title_clean TEXT
);

CREATE TABLE skills_lookup (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT UNIQUE
);

CREATE TABLE job_skills (
    job_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES jobs_clean(id),
    FOREIGN KEY (skill_id) REFERENCES skills_lookup(skill_id)
);

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT UNIQUE,
    avg_rating REAL
);
