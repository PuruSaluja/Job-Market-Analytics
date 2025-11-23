-- 1. Top 20 Most Demanded Skills
SELECT s.skill_name, COUNT(js.job_id) as demand_count
FROM skills_lookup s
JOIN job_skills js ON s.skill_id = js.skill_id
GROUP BY s.skill_name
ORDER BY demand_count DESC
LIMIT 20;

-- 2. Average Salary by Job Title
SELECT job_title_clean, AVG(avg_salary) as average_salary, COUNT(*) as job_count
FROM jobs_clean
WHERE avg_salary IS NOT NULL
GROUP BY job_title_clean
ORDER BY average_salary DESC;

-- 3. Top Paying Skills (Avg Salary for jobs requiring the skill)
SELECT s.skill_name, AVG(j.avg_salary) as avg_skill_salary, COUNT(j.id) as job_count
FROM skills_lookup s
JOIN job_skills js ON s.skill_id = js.skill_id
JOIN jobs_clean j ON js.job_id = j.id
WHERE j.avg_salary IS NOT NULL
GROUP BY s.skill_name
HAVING job_count > 10
ORDER BY avg_skill_salary DESC
LIMIT 20;

-- 4. Remote vs Onsite Trends (Approximation based on location)
SELECT 
    CASE 
        WHEN location LIKE '%Remote%' THEN 'Remote'
        ELSE 'Onsite/Hybrid' 
    END as work_type,
    COUNT(*) as count,
    AVG(avg_salary) as avg_salary
FROM jobs_clean
GROUP BY work_type;

-- 5. Job Distribution by City (Top 10)
SELECT location, COUNT(*) as job_count
FROM jobs_clean
GROUP BY location
ORDER BY job_count DESC
LIMIT 10;

-- 6. Company Rating vs Salary
SELECT company_name, avg_rating, AVG(avg_salary) as avg_salary
FROM jobs_clean
WHERE avg_rating IS NOT NULL AND avg_salary IS NOT NULL
GROUP BY company_name, avg_rating
ORDER BY avg_salary DESC;
