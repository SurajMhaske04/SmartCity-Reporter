📘 SmartCity Reporter – Web Application

SmartCity Reporter is a modern Python Flask–based web application designed to report and manage city-related issues digitally.
This project demonstrates backend development using Flask, SQLite database integration, session-based authentication, and responsive web design.

🚀 Features

🔐 Secure user authentication

🏙 Issue Management

Report city-related issues

Select issue category

Upload images with complaints

📄 Complaint Tracking

View submitted complaints

Track complaint status (Pending / In Progress / Resolved)

👤 User-wise data separation

👮 Admin Management

View all complaints

Update complaint status

Delete complaints

📱 Mobile-friendly responsive web interface

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
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
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
├── static/
│   └── css/
└── uploads/
    └── (empty folder for image uploads)

🗄 Database Setup (Automatic)

This project uses SQLite, so no manual database setup is required.

The database file is automatically created when the application is first run

Required tables and default admin account are initialized automatically

▶️ How to Run the Project
Steps:

Download or clone the repository

Open the project folder in VS Code

Open terminal inside the project folder

Create a virtual environment:

python -m venv venv


Activate virtual environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open browser:

http://127.0.0.1:5000

🔑 Sample Login Credentials
Username	Password	Role
admin	admin123	ADMIN
🧩 Code Architecture
smart_city_issue_reporting/
├── app.py
├── templates/
├── static/
├── uploads/
├── database (auto-created)
└── README.md


This structure follows a simple and beginner-friendly separation of concerns suitable for academic projects.

📘 Key Concepts Used

Flask routing and templates

Session-based authentication

SQLite database operations

File upload handling

CRUD operations

Responsive design using Bootstrap

Git & GitHub version control

🎓 Learning Outcomes

Strong understanding of Flask web application flow

Hands-on experience with SQLite database

Practical authentication and role-based access

File handling in web applications

Full-stack project development experience

Preparation for placements and interviews

👨‍💻 Author

Suraj Mhaske
Computer Engineering Student

GitHub: https://github.com/SurajMhaske04

📌 Project Purpose

This project was developed to practice Python Flask backend development, database handling, and responsive UI design, and to build a professional web application suitable for academic submission and interviews.

📜 License

This project is licensed for academic and learning purposes only.