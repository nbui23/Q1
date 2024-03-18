# Student Database Management System

[Youtube](https://youtu.be/w3Cn0mxjiII)

## Requirements

- Python 3.6 or higher
- PostGreSQL 10 or higher
- psycopg2 or psycopg2-binary
- pgAdmin 4 (optional)

## Setup

Database Setup

1. Download and install PostgreSQL and remember the credentials for the superuser.
2. Create the database in pgAdmin or with the `psql` command-line interface to create a new database named `students`.
3. Connect to the database using pgAdmin's query tool or `psql` and execute SQL commands to create the `students` table and insert initial data.

Applicaiton Setup

1. Clone or download the project source code to your local machine.
2. Open terminal/command prompt, navigate to the project directory, and run `pip install psycopg2-binary`.

## Running the Application

1. Update the database connection details (database name, user, password, host, port) to match your PostgreSQL setup.
2. Run the application using Python with `python q1.py`.