# Course Catalog Schema

This document describes the schema of the normalized course catalog dataset stored in `clean_course_catalog.csv`.

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `name` | `VARCHAR(100)` | Full name of the instructor associated with the course. |
| `role` | `VARCHAR(25)` | Role of the instructor (e.g., "Primary", "TA"). |
| `course_id` | `VARCHAR(10)` | Unique identifier for the course (e.g., "CS3100", "DS2002"). |
| `title` | `VARCHAR(100)` | Official title of the course. |
| `level` | `INT` | Numeric level of the course (e.g., 2000 for sophomore-level courses). |
