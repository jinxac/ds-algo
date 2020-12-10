# Write your MySQL query statement below

# First sql query
/*
    Learnings:-
    
    1. Min
    2. Group BY
*/
select player_id, min(event_date) as first_login
from Activity
group by player_id
