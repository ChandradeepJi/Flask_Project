from flask import Flask , render_template
app=Flask(__name__)
@app.route("/")
def hello():
    name="new web"
    return render_template("index.html",hname=name)
@app.route("/chan")
def chand():
    return "this is second path"
app.run(debug=True)