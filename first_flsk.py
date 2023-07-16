from flask import Flask
app=Flask(__name__)
@app.route('/')
def abc():
    return "this is my first program"

@app.route('/python')
def defg():
    return 'this is your second program'
app.run()