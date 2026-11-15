from flask import Flask, render_template, request, redirect, url_for, g, abort
import yaml

app = Flask(__name__)


@app.before_request
def load_shared_data():
    with open('users.yaml', 'r') as file:
        g.user_data = yaml.safe_load(file)
        g.users = tuple(g.user_data.keys())
        g.number_of_users = len(g.user_data)

@app.template_filter('total_interests')
def total_interests(users):
    total = 0
    for user_data in users.values():
        total += len(user_data['interests'])
    return total

def format_interests(interests):
    if not interests:
        return ''
    if len(interests) == 1:
        return interests[0] + '.'
    return ", ".join(interests[:-1]) + " and " + interests[-1] + "."

@app.route("/")
def index():
    return redirect(url_for("read_users"))

@app.route('/users')
def read_users():
    return render_template('users.html', users=g.users)

@app.route('/users/<name>')
def user_profile(name):
    if name not in g.user_data:
        abort(404)

    user_data = g.user_data[name]
    user_email = user_data['email']
    user_interests = format_interests(user_data['interests'])
    
    return render_template(
        'user_profile.html',
        user=name, 
        email=user_email, 
        interests=user_interests
    )

if __name__ == "__main__":
    app.run(debug=True, port=5003)  # Local development only