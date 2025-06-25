-- LEVEL 3: Group By & Date Logic
-- 1.	Get the total number of workouts per unique Pulse value.
select pulse,count(*)
from workout_tracker
group by pulse

-- 2.	Find the average Sleep_Hours grouped by Sleep_Quality.
select sleep_quality,round(avg(sleep_hours)::numeric,2)||' hours'
from sleep_tracker
group by sleep_quality

-- 3.	Count how many days of data exist per month in the workout_tracker.
SELECT DATE_TRUNC('month', date) AS month,
COUNT(DISTINCT date) AS days_with_data
FROM workout_tracker
GROUP BY month
ORDER BY month;
	
-- 4.	Retrieve all entries from sleep_tracker that happened in December 2020.
select * from sleep_tracker
where date>='2020-01-12' and date<='2021-01-01'

-- 5.	Find which month had the highest average number of Total_Workouts.
select month
from monthly_summary
order by total_workouts desc
limit 1

