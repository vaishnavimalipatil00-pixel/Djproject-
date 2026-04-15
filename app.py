from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return "Login Successful ✅"
        else:
            error = "Invalid Credentials ❌"

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
