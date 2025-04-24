from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build REST API", "done": False}
]

# Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Get a single todo by ID
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Todo not found"}), 404

# Create a new todo
@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    new_todo = {
        "id": todos[-1]["id"] + 1 if todos else 1,
        "task": data.get("task", ""),
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Update a todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    todo["task"] = data.get("task", todo["task"])
    todo["done"] = data.get("done", todo["done"])
    return jsonify(todo)

# Delete a todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})

if __name__ == "__main__":
    import os
    os.environ["FLASK_ENV"] = "development"  # Optional
    app.run(use_reloader=False, debug=True)
