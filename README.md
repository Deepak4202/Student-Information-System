🎓 Student Information System (Python + MySQL)

A simple console-based Student Information System built using Python and MySQL that allows users to manage student records such as adding, updating, viewing, deleting, and searching student information through a menu-driven interface.

🚀 Features

✅ Add new student record
✅ View all student records
✅ View limited records
✅ Update student details
✅ Delete student record
✅ Search student by ID
✅ Input validation for:

Name

Marks

Phone number
✅ Data stored securely in MySQL
✅ Simple and beginner-friendly interface

🛠️ Technologies Used

Python 3

MySQL

mysql-connector-python

📂 Project Structure
Student-Information-System/
│
├── StudentMainProj.py      # Main program
├── StudentMenu.py          # Menu display
├── StudentAdd.py           # Insert student
├── StudentViews.py         # View records
├── StudentUpdate.py        # Update records
├── StudentDelete.py        # Delete record
├── StudentSearch.py        # Search student
└── README.md

🏗️ Database Setup

Run this once in MySQL:

CREATE DATABASE college;
USE college;

CREATE TABLE students (
    sid INT PRIMARY KEY,
    sname VARCHAR(50),
    marks FLOAT,
    phone VARCHAR(10)
);

⚙️ Installation & Setup
1. Install Python library:
pip install mysql-connector-python

2. Update Database Credentials (in all files)

Change this line in your Python code:

passwd="your_password"

▶️ Run the Project

Run the main file:

python StudentMainProj.py

🖥️ Sample Menu
======================================================
        Student Information System
======================================================

1. Add New Student
2. View All Student Details
3. View Single Student Details
4. Delete Student
5. Update Student
6. Search for Student
7. Exit


👨‍💻 Author

Deepak
Computer Science Student
Python Developer

⭐ Support

If you find this useful, give this repository a ⭐ on GitHub!
