from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "completed": False})
    return redirect("/")

@app.route("/mark_completed/<int:task_index>")
def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    return redirect("/")

#if __name__ == "__main__":
#    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="192.168.8.178", port=8000, debug=True)
