import pandas as pd
from Workout_ETL_Project.Utils.db_connection import get_engine

# Extract
df = pd.read_csv("../data/monthly_summary.csv")
print("Original Data:\n", df)

# Transform
df_cleaned = df.copy()

# add values at Nulls
mode_total_workouts=df_cleaned['Total_Workouts'].mode()[0]
df_cleaned.fillna({'Total_Workouts':mode_total_workouts}, inplace=True)

for i in df_cleaned.index:
    if pd.isnull(df_cleaned.loc[i,'Weight(kg)']):
        df_cleaned.loc[i,'Weight(kg)']=df_cleaned.loc[i-1,'Weight(kg)']

# Drop duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Reset index
df_cleaned = df_cleaned.reset_index(drop=True)

# Add 'id' as primary key column
df_cleaned.insert(0, 'id', range(1, 1 + len(df_cleaned)))

df_cleaned.columns = df_cleaned.columns.str.lower()


print("Cleaned Data:\n", df_cleaned)

engine=get_engine()
df_cleaned.to_sql("monthly_summary",engine,if_exists='replace',index=False)

print("\nData loaded successfully to PostgreSQL!")