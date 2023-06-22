from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        return redirect(url_for('mtavari'))
    return render_template('Login.html', title='Login')

@app.route('/main', methods=['POST', 'GET'])
def mtavari():
    return render_template('main.html', title='Mtavari')


@app.route('/shesvla', methods=['POST', 'GET'])
def shesvla():
    if request.method == 'POST':
        return redirect(url_for('signup'))
    return render_template('shesvla.html', title='Signup')


if __name__ == '__main__':
    app.run(debug=True)







