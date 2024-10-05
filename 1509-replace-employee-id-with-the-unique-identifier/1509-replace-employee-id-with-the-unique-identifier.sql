# Write your MySQL query statement below
select unique_id,name from employees as e left join employeeuni as uni on e.id=uni.id
