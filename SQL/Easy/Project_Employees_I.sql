/**
 * 
 *  1075. Project Employees I
 * 
 */

# Write your MySQL query statement below

SELECT Project.project_id, ROUND(AVG(Employee.experience_years), 2) as average_years
FROM Project
JOIN Employee ON Employee.employee_id = Project.employee_id
GROUP BY Project.project_id;
