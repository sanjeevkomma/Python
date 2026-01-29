from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []  # in-memory storage

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=["GET", "POST"])
def user_list():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        users.append({"name": name, "email": email})
        return redirect(url_for("user_list"))

    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)

