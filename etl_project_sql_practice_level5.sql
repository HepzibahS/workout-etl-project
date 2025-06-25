-- LEVEL 5: Joins & Insights
-- 1.	Join sleep_tracker and calories_intake on Date and show Sleep_Hours with Total_Calories.
select sleep_hours,calories_consumed
from sleep_tracker 
Inner join diet_tracker
on sleep_tracker.date=diet_tracker.date

-- 2.	From the above join, filter only where sleep was less than 6 hours.
select sleep_hours,calories_consumed
from sleep_tracker 
Inner join diet_tracker
on sleep_tracker.date=diet_tracker.date
where sleep_hours<6

-- 3.	Identify if days with high Calories burned also had high Sleep_Hours.
SELECT 
    d.date,
    d.calories_consumed,
    s.sleep_hours
FROM 
    diet_tracker d
JOIN 
    sleep_tracker s
    ON d.date = s.date
WHERE  (calories_consumed >
	(select avg(calories_consumed) from diet_tracker))
	and
	(sleep_hours >
	(select avg(sleep_hours)from sleep_tracker))
	
-- 4.	Create a derived column using CASE that flags Workout_Intensity as 'High' if Calories > 450.

select *,
case
	when calories >450 then 'High'
	else 'Normal'
end as Workout_Intensity
from workout_tracker





