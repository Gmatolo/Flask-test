from flask import Flask, render_template, url_for

#reference the imported module
app = Flask(__name__)

#create an index route, exepts error 404
#define the function for the route, feel free to return a string
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


