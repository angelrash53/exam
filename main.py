from flask import Flask, render_template, request, redirect, url_for 
from trainers import Trainer 

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('login.html') 

@app.route('/login', methods = ['POST'])

user = {
    "username": "rashida",
    "password": 1234
    }

username = request.form['Username'] 
password = request.form['Password']

if username == 'rashida': 
    if password == '1234':
        return redirect(url_for('scores', username = username)) 

return "Wrong credentials"+ str(username)


@app.route('/scores/<username>') 
def scores(username): 
    exams = [ 
        {
            "subjectName": "Python",
            "marks": "20/25",
            "date": "13-04-2021"

        },
        {
            "subjectName": "C#",
            "marks": "2/25",
            "date": "13-04-2021"

        },
        {
            "subjectName": "JavaScript",
            "marks": "25/25",
            "date": "13-04-2021"

        },
    ]
    return render_template('scores.html', scores = exams, username = username) 



if __name__ == '__main__':
    app.run(debug = True) 