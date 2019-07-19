from flask import Flask, render_template, request, url_for, redirect
# here you are calling up flask "the library", and then picking specific modules "books" to read.

app = Flask (__name__)

# here Flask is now redefined as 'app' and can be called so from here on in.


@app.route("/", methods=['GET', 'POST']) 
def sign_up():
    error = None
    if request.method=='POST':
        if request.form['email'] == 'joe.bloggs@hotmail.com':
            return redirect(url_for('thankyou'))
        else:
            error ='Please Try Again'
    return render_template('index.html') 

# @ is a decorator which calls up a route.
# the route being called opens your local server on PC. 
# Python code is used to define  a function being signup (): 

@app.route("/thankyou")
def thankyou ():
    return render_template("thankyou.html")

@app.route("/about")
def about ():
    return render_template("about.html")
    
@app.route("/playlist")
def playlist ():
    return render_template("playlist.html")

app.run(debug=True)
