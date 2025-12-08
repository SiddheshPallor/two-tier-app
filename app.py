from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os   

app = Flask(__name__)

# ---------- MySQL CONFIG (uses env vars if available) ----------
db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3307")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "Root@1234"),  
    "database": os.getenv("DB_NAME", "two_tier_db"),
}
# --------------------------------------------------------------



def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn


@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    total_users = len(users)

    return render_template("home.html", users=users, total_users=total_users)


@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        # basic check
        if name and email:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            cursor.close()
            conn.close()

            # after inserting, go back to dashboard
            return redirect(url_for("home"))

    # for GET request – just show the form
    return render_template("add_user.html")

@app.route("/delete-user/<int:user_id>")
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))



@app.route("/db-test")
def db_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"✅ Connected to MySQL database: {db_name}"
    except Exception as e:
        return f"❌ Database connection failed: {e}"


if __name__ == "__main__":
    app.run(debug=True)
