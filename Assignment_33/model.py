import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker


HOST = 'localhost'
PORT = 5432
DATABASE = "DATABASE NAME"
USER = "YOUR USER HERE!"
PASSWORD = "YOUR PASSWORD HERE!"

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

Base = sqlalchemy.orm.declarative_base()


class Department(Base):

    __tablename__ = 'department'

    DepartmentID = Column("departmentid", Integer, primary_key=True, autoincrement=True)
    DepartmentName = Column("departmentname", String(20))


class Employee(Base):

    __tablename__ = 'employee'

    EmployeeID = Column("employeeid", Integer, primary_key=True, autoincrement=True)
    Fullname = Column("fullname", String(50))
    HireDate = Column("hiredate", Date)
    DepartmentID = Column("departmentid",Integer, ForeignKey('Department.DepartmentID'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Function for printing tables separately
# def print_output():
#     print("Department Table:")
#     departments = session.query(Department).all()
#     for department in departments:
#         print(f"DepartmentID: {department.DepartmentID}, DepartmentName: {department.DepartmentName}")
#
#     print("\nEmployee Table:")
#     employees = session.query(Employee).all()
#     for employee in employees:
#         print(f"EmployeeID: {employee.EmployeeID}, Fullname: {employee.Fullname}, HireDate: {employee.HireDate},"
#               f" DepartmentID: {employee.DepartmentID}")
#
#
# if __name__ == "__main__":
#     print_output()
