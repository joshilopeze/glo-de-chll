--Number of employees hired for each job and department in 2021 divided by quarter. The
--table must be ordered alphabetically by department and job.

SELECT
    d.department,
    j.job,
    COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM TO_TIMESTAMP(a.datetime, 'YYYY-MM-DD"T"HH24:MI:SS')) BETWEEN 1 AND 3 THEN 1 ELSE 0 END), 0) AS Q1,
    COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM TO_TIMESTAMP(a.datetime, 'YYYY-MM-DD"T"HH24:MI:SS')) BETWEEN 4 AND 6 THEN 1 ELSE 0 END), 0) AS Q2,
    COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM TO_TIMESTAMP(a.datetime, 'YYYY-MM-DD"T"HH24:MI:SS')) BETWEEN 7 AND 9 THEN 1 ELSE 0 END), 0) AS Q3,
    COALESCE(SUM(CASE WHEN EXTRACT(MONTH FROM TO_TIMESTAMP(a.datetime, 'YYYY-MM-DD"T"HH24:MI:SS')) BETWEEN 10 AND 12 THEN 1 ELSE 0 END), 0) AS Q4
FROM employees a
LEFT JOIN departments d ON d.id = a.department_id
LEFT JOIN jobs j ON j.id = a.job_id
WHERE EXTRACT(YEAR FROM TO_TIMESTAMP(a.datetime, 'YYYY-MM-DD"T"HH24:MI:SS')) = 2021
AND a.datetime <> 'nan'
GROUP BY d.department, j.job
ORDER BY d.department, j.job;
