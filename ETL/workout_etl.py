import pandas as pd
from Workout_ETL_Project.Utils.db_connection import get_engine

# Extract
df = pd.read_csv("../data/workout_data.csv")
print("Original Data:\n", df)

# Transform
df_cleaned = df.copy()

# Convert 'Date' safely (handles any format, backward-compatible)
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], errors='coerce')

# Clean Duration outliers using for loop
for i in df_cleaned.index:
    if pd.notnull(df_cleaned.loc[i, 'Duration']) and df_cleaned.loc[i, 'Duration'] > 180:
        df_cleaned.loc[i, 'Duration'] = 60

# update Null calories with mean value
mean_calories=df_cleaned['Calories'].mean()
df_cleaned.fillna({'Calories':mean_calories}, inplace=True)

#drop NaT/Null if any
df_cleaned.dropna(inplace=True)

# Drop duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Reset index
df_cleaned = df_cleaned.reset_index(drop=True)

# Add 'id' as primary key column
df_cleaned.insert(0, 'id', range(1, 1 + len(df_cleaned)))

df_cleaned.columns = df_cleaned.columns.str.lower()

print("Cleaned Data:\n", df_cleaned)

engine=get_engine()
df_cleaned.to_sql("workout_tracker",engine,if_exists='replace',index=False)

print("\nData loaded successfully to PostgreSQL!")