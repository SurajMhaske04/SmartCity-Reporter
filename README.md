📘 SmartCity Reporter – Web Application

SmartCity Reporter is a Python Flask–based web application designed to allow users to report city-related issues digitally and enable an admin to manage and track those issues efficiently.
This project demonstrates backend development, session-based authentication, SQLite integration, and responsive web design.

🚀 Features
👤 User Features

🔐 User registration and login

📝 Report city-related issues (road damage, garbage, street lights, etc.)

🖼 Upload images with complaints

📄 View personal complaint history

🔄 Track complaint status (Pending / In Progress / Resolved)

📱 Mobile-friendly responsive interface

👮 Admin Features

🔐 Separate admin login

📋 View all user complaints

🔁 Update complaint status

🗑 Delete complaints

📊 Simple admin dashboard

🛠 Technologies Used

Python

Flask

SQLite

HTML

CSS

Bootstrap

Git & GitHub

🗂 Project Structure
smart_city_issue_reporting/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_complaint.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── complaint_detail.html
│   └── admin_complaint_detail.html
│
├── static/
│   └── css/
│
└── uploads/
    └── (empty folder for image uploads)

🗄 Database Setup (Automatic)

This project uses SQLite, so no manual database setup is required.

The database file (database.db) is automatically created when the application runs.

Required tables and default admin account are initialized at runtime.

▶️ How to Run the Project
Step 1: Open project folder in VS Code
Step 2: Open terminal

Press:

Ctrl + `

Step 3: Create virtual environment
python -m venv venv

Step 4: Activate virtual environment

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

Step 5: Install dependencies
pip install -r requirements.txt

Step 6: Run the application
python app.py

Step 7: Open in browser
http://127.0.0.1:5000

🔑 Sample Login Credentials
Admin Login
Username	Password
admin	admin123

Credentials are for demonstration purposes only.

🧩 Code Architecture

The project follows a simple and beginner-friendly structure:

Flask routes handle request/response logic

HTML templates manage UI rendering

SQLite manages persistent data

Session-based authentication ensures user separation

This design keeps the code easy to understand and extend.

📘 Key Concepts Used

Flask routing and templates

Session-based authentication

SQLite database operations

File upload handling

CRUD operations

Responsive web design using Bootstrap

Git & GitHub version control

🎓 Learning Outcomes

Understanding Flask web application flow

Hands-on experience with SQLite database

Practical authentication and role-based access

File handling in web applications

Building a complete full-stack web project

Preparing a project suitable for interviews and college evaluation

📌 Project Purpose

This project was developed to practice Python Flask backend development, database handling, and responsive UI design, and to build a professional web application prototype suitable for academic submission and interviews.

👨‍💻 Author

Suraj Mhaske
Computer Engineering Student

🔗 GitHub:
https://github.com/SurajMhaske04

📜 License

This project is licensed for academic and learning purposes only.
Free to use, modify, and study for educational use.