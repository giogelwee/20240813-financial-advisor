# render_template renders the html template & return them as a response
# request handles the incoming request (like the prompt)
from flask import Flask, render_template, request

# this creates the web application - initialising the process
app = Flask(__name__)

# @app.route gets the root URL: http://localhost:5000/
# GET: request data, POST: submit data
@app.route("/", methods = ["GET","POST"])
# this function is called whenever someone visits the root URL of http://localhost:5000/ 
def index():
    # access the front-end specifics
    return(render_template("index_tut.html"))

# this runs the web application 
if __name__ == "__main__":
    app.run()
