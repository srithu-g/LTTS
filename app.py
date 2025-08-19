from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    rollno = request.form['rollno']
    year = request.form['year']
    return render_template('result.html', name=username, roll=rollno, mail=email, yr=year)

if _name_ == '_main_':
    app.run(debug=True,port=5001)
