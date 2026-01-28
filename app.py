from flask import Flask, render_template, request, redirect, session, send_from_directory
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "simple_secret_key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            description TEXT,
            image TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def create_admin():
    conn = get_db_connection()
    admin = conn.execute("SELECT * FROM admin").fetchone()
    if not admin:
        conn.execute(
            "INSERT INTO admin (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )
        conn.commit()
    conn.close()


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/")
def home():
    return render_template("home.html")


#USER AUTH

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (
                request.form["name"],
                request.form["email"],
                request.form["password"]
            )
        )
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (request.form["email"], request.form["password"])
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


#USER DASHBOAR

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    complaints = conn.execute(
        "SELECT * FROM complaints WHERE user_id=? ORDER BY id DESC",
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        complaints=complaints,
        name=session["user_name"],
        email=session["user_email"]
    )


@app.route("/complaint/<int:id>")
def complaint_detail(id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    complaint = conn.execute(
        "SELECT * FROM complaints WHERE id=? AND user_id=?",
        (id, session["user_id"])
    ).fetchone()
    conn.close()

    return render_template("complaint_detail.html", c=complaint)


@app.route("/delete_complaint/<int:id>")
def delete_complaint(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM complaints WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/dashboard")


@app.route("/add_complaint", methods=["GET", "POST"])
def add_complaint():
    if request.method == "POST":
        image = request.files["image"]
        image_name = image.filename if image else ""

        if image:
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO complaints (user_id, category, description, image) VALUES (?, ?, ?, ?)",
            (
                session["user_id"],
                request.form["category"],
                request.form["description"],
                image_name
            )
        )
        conn.commit()
        conn.close()
        return redirect("/dashboard")

    return render_template("add_complaint.html")

#ADMIN 

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        conn = get_db_connection()
        admin = conn.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        ).fetchone()
        conn.close()

        if admin:
            session["admin_id"] = admin["id"]
            return redirect("/admin/dashboard")

    return render_template("admin_login.html")


@app.route("/admin/dashboard")
def admin_dashboard():
    if "admin_id" not in session:
        return redirect("/admin")

    status = request.args.get("status")

    conn = get_db_connection()
    if status:
        complaints = conn.execute(
            """SELECT complaints.*, users.name 
               FROM complaints JOIN users ON complaints.user_id = users.id
               WHERE status=?""",
            (status,)
        ).fetchall()
    else:
        complaints = conn.execute(
            """SELECT complaints.*, users.name 
               FROM complaints JOIN users ON complaints.user_id = users.id"""
        ).fetchall()
    conn.close()

    return render_template("admin_dashboard.html", complaints=complaints)


@app.route("/admin/complaint/<int:id>")
def admin_complaint_detail(id):
    conn = get_db_connection()
    c = conn.execute(
        """SELECT complaints.*, users.name, users.email
           FROM complaints JOIN users ON complaints.user_id = users.id
           WHERE complaints.id=?""",
        (id,)
    ).fetchone()
    conn.close()
    return render_template("admin_complaint_detail.html", c=c)


@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):
    conn = get_db_connection()
    conn.execute(
        "UPDATE complaints SET status=? WHERE id=?",
        (request.form["status"], id)
    )
    conn.commit()
    conn.close()
    return redirect("/admin/dashboard")


@app.route("/admin/delete/<int:id>")
def admin_delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM complaints WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/admin/dashboard")


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_id", None)
    return redirect("/admin")


if __name__ == "__main__":
    init_db()
    create_admin()
    app.run(host="0.0.0.0", port=5000, debug=True)

