--  LEVEL 4: Data Cleaning Checks
-- 1.	Identify and list duplicate records in the calories_intake table.
select date,calories_consumed,"protein(g)","carbs(g)","fats(g)",meal_type,count(*) as count
from diet_tracker
group by 1,2,3,4,5,6
having count(*) > 1

-- 2.	Find rows where Heart_Rate_Variability is NULL.
select * 
from sleep_tracker
where heart_rate_variability isNUll

-- 3.	Count how many rows have Total_Calories less than 1000.
select count(*) as Count_of_Calories_less_than_1000
from diet_tracker
where calories_consumed<1000

-- 4.	Check if any Date values are NULL in diet_tracker.
select count(*) as Count_of_Null_dates
from diet_tracker
where date isnull

-- 5.	Find out if there are any rows where Sleep_Hours is negative or zero.
select *
from sleep_tracker
where sleep_hours <=0
