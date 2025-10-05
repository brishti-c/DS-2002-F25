# Survey Data Schema

This document describes the schema of the cleaned survey dataset stored in `clean_survey_data.csv`.

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for each student in the survey. |
| `major` | `VARCHAR(50)` | The academic major or field of study declared by the student. |
| `GPA` | `FLOAT` | The student’s Grade Point Average on a 4.0 scale. |
| `is_cs_major` | `BOOL` | Indicates whether the student is a Computer Science major (`True` or `False`). |
| `credits_taken` | `FLOAT` | The total number of academic credits the student has completed or is currently taking. |
