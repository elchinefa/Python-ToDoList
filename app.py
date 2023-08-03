from flask import Flask, render_template, request, redirect, session
import database
import hashlib

app = Flask(__name__)
app.secret_key = "3fe1be74e3069726893354e506bffe9a039aa5252c271c2aa1ead89c5cc16662"  # Replace with your own secret key


# Initialize the database
database.init_db()
# ... (Existing routes and functions)

def verify_password(password, hashed_password):
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_input_password == hashed_password

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = database.get_user(username)
        if user and verify_password(password, user["password"]):
            session["user_id"] = user["id"]
            return redirect("/home")
        else:
            return "Invalid username or password."

    return render_template("login.html")

@app.route("/")
def login_redirect():
    return redirect("/login")


@app.route("/home")
def home():
    user_id = session.get("user_id")
    username = None

    if user_id:
        user = database.get_user_by_id(user_id)  # Make sure to add get_user_by_id function to database.py
        if user:
            username = user["username"]

    tasks = database.get_tasks(user_id)  # Pass the user_id to fetch tasks for the specific user
    return render_template("index.html", user_id=user_id, username=username, tasks=tasks)



@app.route("/")
def index():
    user_id = session.get("user_id")
    username = None

    if user_id:
        user = database.get_user(user_id)
        if user:
            username = user["username"]

    tasks = database.get_tasks(user_id)  # Pass the user_id to fetch tasks for the specific user
    return render_template("index.html", user_id=user_id, username=username, tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print("Registration form submitted.")
        username = request.form.get("username")
        password = request.form.get("password")
        print("Received username:", username)
        if not username or not password:
            return "Username and password are required."
        if database.get_user(username):
            return "Username already exists."

        # Hash the password before storing it in the database
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("Hashed password:", hashed_password)
        database.add_user(username, hashed_password)
        print("User added to the database.")
        return redirect("/login")
    return render_template("register.html")





@app.route("/logout")
def logout():
    # Clear the user session data (logout)
    session.clear()
    return redirect("/login")
  

@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        user_id = session.get("user_id")
        if not user_id:
            return redirect("/login")

        task = request.form.get("task")
        if task:
            database.add_task(user_id, task)

        return redirect("/home")

    # For GET requests, simply redirect to the home page ("/")
    return redirect("/")



@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    database.mark_task_completed(task_id)
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
