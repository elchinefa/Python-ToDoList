from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

# Initialize the database
database.init_db()

@app.route("/")
def index():
    tasks = database.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        database.add_task(task)
    return redirect("/")

@app.route("/mark_completed/<int:task_id>")
def mark_completed(task_id):
    database.mark_task_completed(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

