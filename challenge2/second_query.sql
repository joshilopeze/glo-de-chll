--List of ids, name and number of employees hired of each department that hired more
--employees than the mean of employees hired in 2021 for all the departments, ordered
--by the number of employees hired (descending).

WITH AvgHired AS (
    SELECT AVG(hired_count) AS avg_hired
    FROM (
        SELECT COUNT(*) AS hired_count
        FROM employees
        WHERE strftime('%Y', datetime) = '2021'
        GROUP BY department_id
    ) sub
),
HiredPerDept AS (
    SELECT 
        d.id,
        d.department,
        COUNT(*) AS hired
    FROM departments d
    JOIN employees e ON d.id = e.department_id
    WHERE strftime('%Y', datetime) = '2021'
    GROUP BY d.id, d.department
)
SELECT 
    id,
    department,
    hired
FROM HiredPerDept
WHERE hired > (SELECT avg_hired FROM AvgHired)
ORDER BY hired DESC;