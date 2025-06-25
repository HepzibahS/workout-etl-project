import pandas as pd
from Workout_ETL_Project.Utils.db_connection import get_engine

# Extract
df = pd.read_csv("../data/sleep_data.csv")
print("Original Data:\n", df)

# Transform
df_cleaned = df.copy()

# Convert 'Date' safely (handles any format, backward-compatible)
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], errors='coerce')

# Assign Sleep_Quality based on Sleep_Hours
for i in df_cleaned.index:
    if pd.notnull(df_cleaned.loc[i, "Sleep_Hours"]):  # safety check
        hours = df_cleaned.loc[i, "Sleep_Hours"]
        if hours <= 5:
            df_cleaned.loc[i, "Sleep_Quality"] = "Poor"
        elif 5 < hours <= 7:
            df_cleaned.loc[i, "Sleep_Quality"] = "Average"
        elif 7 < hours <= 9.5:
            df_cleaned.loc[i, "Sleep_Quality"] = "Good"
        else:
            df_cleaned.loc[i, "Sleep_Quality"] = "OverSlept"

# update Null calories with mean value
avg_Heart_Rate_Variability=df_cleaned['Heart_Rate_Variability'].mean()
df_cleaned.fillna({'Heart_Rate_Variability':avg_Heart_Rate_Variability}, inplace=True)

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
df_cleaned.to_sql("sleep_tracker",engine,if_exists='replace',index=False)

print("\nData loaded successfully to PostgreSQL!")