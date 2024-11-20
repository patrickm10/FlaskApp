from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

# Mock database for demonstration
users = {
    'admin': 'admin'  # Pre-existing user
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet/<username>')
def greet(username):
    return f"Welcome {username}!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        UN = request.form['username']
        PW = request.form['password']

        # Check if the username exists and the password matches
        if UN in users and users[UN] == PW:
            return redirect(url_for('greet', username=UN))
        elif UN not in users:
            return redirect(url_for('register'))
        else:
            return "Incorrect password. Please try again."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        DUN = request.form['Dusername']
        DPW = request.form['Dpassword']

        # Check if the username already exists
        if DUN in users:
            return "Username already exists. Please choose a different one."
        else:
            users[DUN] = DPW
            return redirect(url_for('greet', username=DUN))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
