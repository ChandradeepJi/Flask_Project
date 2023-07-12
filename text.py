from flask import Flask
app=Flask(__name__)
@app.route("/")
def abc():
    return "this is my first program"

app.run(debug=True)
print("program is sccess")
