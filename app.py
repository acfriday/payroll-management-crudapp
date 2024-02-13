from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def root():
    return render_template("login.html")

@app.route('/register',methods=["POST", "GET"])
def register():
    return render_template("register.html")

@app.route('/dashboard',methods=["POST", "GET"])
def dashboard():
    return render_template("admin-dashboard.html")

if __name__== '__main__':
    app.run(debug=True)