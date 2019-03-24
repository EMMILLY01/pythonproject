from flask import Flask, render_template, request
# here you are calling up flask "the library", and then picking specific modules "books" to read.

app = Flask ("App") 

# here Flask is now redefined as 'app' and can be called so from here on in.

@app.route("/")
def hello ():
    render_template("index.html")

# @ is a decorator which calls up a route.
# the route being called opens your local server on PC. 
# Python code is used to define  a function being hello (): as a return of words 'test, test, test'

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html", name=name.title())
    
# 1. @app.route("/<wrong_website>") - Python defines the physical directory name that people should type in.
# 2. When the user visits this URL, the 'hello_someone' function defined above will run.
    # it will use the 'wrong_website' argument/variable typed in the URL.
# 3. The function says to 'return'/show the user the "rendered" 'hello.html' file
    #...using the 'render_template' module imported at the start, and to convert the 
    # ...Users input 'wrong_website' into a title format.


@app.route("/index", methods=["POST"]) 
def sign_up():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

@app.route("/like", methods=["POST"]) 
def like():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

@app.route("/entry", methods=["POST"]) 
def entry():
    form_data = request.form
    print (form_data["entry"])
    return "All OK"

app.run(debug=True)


#@app.route("/fizzbuzz/<int:number>")
#def fizz_buzz(number):
#    return fizzbuzz_site(number)

#'''
#@app.route("/<string:name>")
#def hello_name (name):
#    return f "Hello {name}!"
#'''