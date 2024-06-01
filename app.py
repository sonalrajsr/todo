from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    disc = db.Column(db.String(500), nullable=False)
    deadline = db.Column(db.Date, nullable=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("home.html", todos=todos)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        discrip = request.form.get('discription')
        deadline_str = request.form['deadline']
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        new_todo = Todo(title=title, disc=discrip, deadline = deadline)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.disc = request.form['discription']
        deadline_str = request.form['deadline']
        todo.deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
