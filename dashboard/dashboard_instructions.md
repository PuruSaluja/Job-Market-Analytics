# Dashboard Instructions (Power BI)

## 1. Data Import
1. Open Power BI Desktop.
2. Click **Get Data** -> **More...** -> **SQLite**.
3. Enter the database path: `C:\Users\psaluja1\.gemini\antigravity\scratch\job_market_analytics\jobs.db`.
4. Select the following tables:
   - `jobs_clean`
   - `skills_lookup`
   - `job_skills`
   - `companies`
5. Click **Load**.

## 2. Data Modeling
1. Go to **Model View**.
2. Ensure the following relationships exist:
   - `jobs_clean[id]` -> `job_skills[job_id]` (One-to-Many)
   - `skills_lookup[skill_id]` -> `job_skills[skill_id]` (One-to-Many)
   - `companies[company_name]` -> `jobs_clean[company_name]` (One-to-Many)

## 3. DAX Measures
Create a new table called `_Measures` to store these.

**Total Jobs**
```dax
Total Jobs = COUNTROWS(jobs_clean)
```

**Avg Salary**
```dax
Avg Salary = AVERAGE(jobs_clean[avg_salary])
```

**Remote %**
```dax
Remote % = 
DIVIDE(
    CALCULATE(COUNTROWS(jobs_clean), CONTAINSSTRING(jobs_clean[location], "Remote")),
    [Total Jobs],
    0
)
```

**Top Skill Count**
```dax
Skill Count = COUNTROWS(job_skills)
```

## 4. Dashboard Pages

### Page 1: Overview / KPI
- **Cards**: Total Jobs, Avg Salary, Remote %, Total Companies.
- **Bar Chart**: Top 10 Job Titles (Axis: `job_title_clean`, Values: `Total Jobs`).
- **Map**: Job Distribution by Location (Location: `location`, Bubble Size: `Total Jobs`).
- **Donut Chart**: Remote vs Onsite (Legend: Calculated Column `Work Type`, Values: `Total Jobs`).

### Page 2: Skill Analysis
- **Bar Chart**: Top 20 Skills (Axis: `skill_name`, Values: `Skill Count`).
- **Tree Map**: Skill Categories (if available) or just Skills.
- **Table**: Skill Name, Job Count, Avg Salary (for jobs with that skill).

### Page 3: Salary Insights
- **Histogram (Column Chart)**: Salary Distribution (Bin `avg_salary`).
- **Scatter Plot**: Rating vs Salary (X: `rating`, Y: `avg_salary`).
- **Bar Chart**: Avg Salary by Job Title.

## 5. Formatting
- Use a dark theme (e.g., "Innovate" or custom dark blue/black background).
- Use consistent fonts (Segoe UI).
- Add a title "Job Market Insights 2024-2025" at the top.
