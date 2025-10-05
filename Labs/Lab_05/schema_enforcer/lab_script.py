import csv

# Define the data with intentional type inconsistencies
data = [
    # student_id (int), major (str), GPA (float/int), is_cs_major (bool but saved as string), credits_taken (float but saved as string)
    [101, "Computer Science", 3.8, "Yes", "15.0"],
    [102, "Mathematics", 3, "No", "12.5"],   # GPA as int
    [103, "Biology", 2.7, "No", "9.0"],
    [104, "Computer Science", 4, "Yes", "18.0"],  # GPA as int
    [105, "English", 3.25, "No", "10.5"],   # credits_taken as string
]

# Define the headers
headers = ["student_id", "major", "GPA", "is_cs_major", "credits_taken"]

# Write to CSV
with open("raw_survey_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # Write header row
    writer.writerows(data)    # Write data rows

print("raw_survey_data.csv created with inconsistent data types!")

import json

# Define a list of dictionaries with nested instructor data
courses = [
    {
        "course_id": "LATI2020",
        "section": "002",
        "title": "Intermediate Latin II", 
        "level": 2000,
        "instructors": [
            {"name": "Inger Kuin", "role": "Primary"},
        ]
    },
    {
        "course_id": "SDE2000",
        "section": "002",
        "title": "Discrete Mathematics and Theory 2",
        "level": 3000,
        "instructors": [
            {"name": "Ray Pettit", "role": "Primary"}
        ]
    },
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 2000,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    }
]

# Write the structure to a JSON file
with open("raw_course_catalog.json", "w") as f:
    json.dump(courses, f, indent=2)

print("raw_course_catalog.json created successfully!")

import pandas as pd

# Step 1: Load the raw CSV data into a DataFrame
df = pd.read_csv("raw_survey_data.csv")

print("Original DataFrame:")
print(df)
print("\nData types before cleaning:")
print(df.dtypes)

# Step 2: Enforce Boolean Type for 'is_cs_major'
# Convert 'Yes' -> True, 'No' -> False
df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False})

# Step 3: Enforce Numeric Types for 'credits_taken' and 'GPA'
df = df.astype({
    "credits_taken": "float64",
    "GPA": "float64"
})

print("\nCleaned DataFrame:")
print(df)
print("\nData types after cleaning:")
print(df.dtypes)

# Step 4: Save the cleaned DataFrame to a new CSV file
df.to_csv("clean_survey_data.csv", index=False)

print("\n✅ clean_survey_data.csv created successfully!")

import json
import pandas as pd

# Step 1: Load the raw JSON data
with open("raw_course_catalog.json", "r") as f:
    data = json.load(f)

print("Original JSON data loaded successfully!\n")

# Step 2: Normalize (flatten) the nested instructor data
# Each instructor in the 'instructors' list becomes its own row
df = pd.json_normalize(
    data,
    record_path=["instructors"],
    meta=["course_id", "title", "level"]
)

print("Normalized DataFrame:")
print(df)

# Step 3: Save the flattened data to a CSV file
df.to_csv("clean_course_catalog.csv", index=False)

print("\n✅ clean_course_catalog.csv created successfully!")

