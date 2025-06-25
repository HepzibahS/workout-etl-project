-- LEVEL 2: Aggregations & Sorting
-- 1.	Count the total number of rows in sleep_tracker.
select count(*)
from sleep_tracker

-- 2.	Find the average Calories burned in workouts.
select round((avg(calories)::numeric),2) as AVG_calories
from workout_tracker

-- 3.	Get the minimum and maximum Sleep_Hours recorded.
select min(sleep_hours) as Min_Sleep_hours,max(sleep_hours) as Max_Sleep_hours
from sleep_tracker

-- 4.	Show the top 5 entries with highest Total_Calories from calories_intake.
select * from diet_tracker
select calories_consumed as Total_calories
from diet_tracker
order by calories_consumed desc
limit 5

-- 5.	Find how many entries in monthly_summary had Weight(kg) over 60.
select count(*)
from monthly_summary
where "weight(kg)">60
