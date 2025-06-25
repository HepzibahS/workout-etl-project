-- LEVEL 1: Basic Selects & Filters
-- 1.	Fetch all rows from the workout_tracker table.
select * from workout_tracker

-- 2.	Display only the Date and Calories columns from workout_tracker.
select date,calories
from workout_tracker

-- 3.	Find all workouts that lasted more than 60 minutes.
select * from workout_tracker
where duration>=60
-- 4.	Show all records where Pulse is greater than 120.
select *
from workout_tracker
where pulse>120
-- 5.	List distinct values of Sleep_Quality from sleep_tracker.
select distinct sleep_quality
from sleep_tracker