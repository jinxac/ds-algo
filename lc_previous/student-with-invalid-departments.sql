# Write your MySQL query statement below
/*
    Solution:-
    
    1. Check if id is not in department list
    2. Compare using join (TODO: Explore later)
*/
select id, name from Students
where department_id not in(
    select id from Departments
)
