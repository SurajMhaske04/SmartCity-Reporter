# 📱 SmartCity Reporter – Web Application

SmartCity Reporter is a modern **Python Flask–based web application** designed to report and manage city-related issues digitally.  
This project demonstrates backend development using Flask, SQLite database integration, session-based authentication, and responsive web design.

---

## 🚀 Features

### 👤 User Features
- 🔐 User registration and login  
- 📝 Report city-related issues  
- 🏷 Select issue category  
- 🖼 Upload images with complaints  
- 📄 View personal complaint history  
- 🔄 Track complaint status (Pending / In Progress / Resolved)  

### 👮 Admin Features
- 🔐 Separate admin login  
- 📋 View all user complaints  
- 🔁 Update complaint status  
- 🗑 Delete complaints  
- 📱 Mobile-friendly responsive interface  

---

## 🛠 Technologies Used

- Python  
- Flask  
- SQLite  
- HTML  
- CSS  
- Bootstrap  
- Git & GitHub  

---

## 🗂 Project Structure

```text

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
This project uses SQLite

No manual database setup is required

Database file is created automatically when the application runs

Tables and default admin account are initialized at runtime

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
Username	Password	Role
admin	admin123	ADMIN
🧩 Code Architecture
Flask routes handle request and response logic

HTML templates manage UI rendering

SQLite manages persistent data

Session-based authentication ensures user-wise separation

This structure follows a simple and beginner-friendly architecture suitable for academic projects.

📘 Key Concepts Used
Flask routing and templates

Session-based authentication

SQLite database operations

File upload handling

CRUD operations

Responsive UI with Bootstrap

Git & GitHub version control

🎓 Learning Outcomes
Understanding Flask web application flow

Hands-on experience with SQLite database

Practical authentication and role-based access

File handling in web applications

Full-stack development experience

Interview and placement readiness

👨‍💻 Author
Suraj Mhaske
Computer Engineering Student

GitHub: https://github.com/SurajMhaske04

📌 Project Purpose
This project was developed to practice Python Flask backend development, database handling, and responsive UI design, and to build a professional web application suitable for academic submission and interviews.

📜 License
This project is licensed for academic and learning purposes only.
Free to use, modify, and study for educational use.

