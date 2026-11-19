from flask import Flask, render_template, request, send_from_directory, flash, redirect, url_for, abort, session
import os
from markdown import markdown
from functools import wraps
import yaml
import bcrypt

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

def valid_credentials(username, password):
    root = os.path.abspath(os.path.dirname(__file__))
    if app.config["TESTING"]:
        user_directory_path = os.path.join(root, "tests", "users.yaml")
    else:
        user_directory_path = os.path.join(root, "cms", "users.yaml")
    with open(user_directory_path, 'r') as file:
        user_directory = yaml.safe_load(file)
    if username in user_directory:
        stored_password = user_directory[username].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    else:
        return False

def get_data_path():
    root = os.path.abspath(os.path.dirname(__file__))

    if app.config["TESTING"]:
        return os.path.join(root, "tests", "data")
    else:
        return os.path.join(root, "cms", "data")

def user_signed_in():
    return "username" in session

def require_signed_in_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not user_signed_in():
            flash("You must be signed in to do that.")
            return redirect(url_for('signin'))

        return f(*args, **kwargs)

    return decorated_function

@app.route("/")
def index():
    data_dir = get_data_path()
    files = [os.path.basename(path) for path in os.listdir(data_dir)]
    return render_template("index.html", files=files)

@app.route("/<filename>")
def file_lookup(filename):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, filename)
    
    if os.path.isfile(file_path):
        if file_path.endswith(".md"):
            with open(file_path, "r") as f:
                content =  f.read()
                return render_template('markdown.html', content=markdown(content))
        return send_from_directory(data_dir, filename)
    else:
        flash(f"{filename} does not exist.")
        return redirect(url_for('index'))

@app.route("/<filename>/edit", methods=["GET"])
@require_signed_in_user
def file_edit(filename):
    data_dir =  get_data_path()
    file_path = os.path.join(data_dir, filename)
    
    if not os.path.isfile(file_path):
        abort(404, description=f"{filename} does not exist.")
    with open(file_path, "r") as f:
        content = f.read()
    return render_template("file_editor.html", filename=filename, content=content)

@app.route("/<filename>/edit", methods=["POST"])
@require_signed_in_user
def update_file(filename):
    data_dir =  get_data_path()
    file_path = os.path.join(data_dir, filename)
    
    if not os.path.isfile(file_path):
        abort(404, description=f"{filename} does not exist.")
    new_content = request.form["contents"]
    with open(file_path, "w") as f:
        f.write(new_content)
    flash(f"{filename} has been updated.")
    return redirect(url_for('index'))

@app.route("/new", methods=["GET", "POST"])
@require_signed_in_user
def create_document():
    if request.method == "POST":
        filename = request.form.get("filename", '').strip()
        if not filename:
            flash('A name is required.')
            return render_template('new_document.html'), 422
        data_dir =  get_data_path()
        file_path = os.path.join(data_dir, filename)
        if os.path.isfile(file_path):
                flash(f"{filename} already exists.")
                return render_template('new_document.html'), 422
        with open(file_path, 'w'):
            pass
        flash(f"{filename} has been created.")
        return redirect(url_for('index'))
    else:
        return render_template('new_document.html')

@app.route("/<filename>/delete", methods=["POST"])
@require_signed_in_user
def delete_file(filename):
    data_dir =  get_data_path()
    file_path = os.path.join(data_dir, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        flash(f"{filename} has been deleted.")
    else:
        flash(f"{filename} does not exist.")        
    return redirect(url_for('index'))

@app.route("/users/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if valid_credentials(username, password):
        session["username"] = username
        flash("Welcome!")
        return redirect(url_for("index"))
    else:
        flash("Invalid credentials")
        return render_template("signin.html"), 422

@app.route("/users/signout", methods=["POST"])
def signout():
    print(session)
    session.pop("username", None)
    print(session)
    flash("You have been signed out.")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)