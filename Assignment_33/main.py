import psycopg2
from psycopg2 import sql

# Database connection parameters
HOST = 'localhost'
PORT = 5432
DATABASE = "test"
USER = "postgres"
PASSWORD = "A2b0r0a0m6a!"

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    database=DATABASE,
    user=USER,
    password=PASSWORD
)
cursor = conn.cursor()

## CREATING DATABASE

# Create Department table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Department (
#         DepartmentID SERIAL PRIMARY KEY,
#         DepartmentName VARCHAR(20) UNIQUE
#     )
# """)
#
# # Create Employee table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Employee (
#         EmployeeID SERIAL PRIMARY KEY,
#         Fullname VARCHAR(50),
#         HireDate DATE,
#         DepartmentID INTEGER REFERENCES Department(DepartmentID)
#     )
# """)
#
# # Insert data into Department table
# department_data = [
#     ("IT",),
#     ("HR",)
# ]
# cursor.executemany(
#     "INSERT INTO Department (DepartmentName) VALUES (%s)",
#     department_data
# )
#
# # Insert data into Employee table
# employee_data = [
#     ("John Doe", '2024-01-01', 1),
#     ("Jane Smith", '2023-05-15', 2)
# ]
# cursor.executemany(
#     "INSERT INTO Employee (Fullname, HireDate, DepartmentID) VALUES (%s, %s, %s)",
#     employee_data
# )
#
# # Commit changes
# conn.commit()

# Fetch and print Department table
cursor.execute("SELECT * FROM Department")
departments = cursor.fetchall()
print("Department Table:")
for department in departments:
    print(department)

# Fetch and print Employee table
cursor.execute("SELECT * FROM Employee")
employees = cursor.fetchall()
print("\nEmployee Table:")
for employee in employees:
    print(employee)

# Close cursor and connection
cursor.close()
conn.close()
