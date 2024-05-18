
from model import session, Department, Employee

joined_query = session.query(Employee, Department).join(Department, Employee.DepartmentID == Department.DepartmentID)

result = joined_query.all()


def print_table():
    # Print the headers
    print("\nEmployeeID  | Fullname                | HireDate   | DepartmentID | DepartmentName")
    print("-" * 80)

    for employee, department in result:
        print(f"{employee.EmployeeID:<11} | {employee.Fullname:<23} | {employee.HireDate} | {employee.DepartmentID:<12} |"
              f" {department.DepartmentName}")


if __name__ == "__main__":
    print_table()