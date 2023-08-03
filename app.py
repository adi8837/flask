##Create a simple flask application

from flask import Flask,redirect,url_for

##create the flask app

app=Flask(__name__) #This line creates the flask app. This is our WSGI application which will be
                    #communicating with the server

@app.route('/') #This is a decorator. These are routes and functions to handle request
def home():     #inside route(), we define two parameters which are our route URL and methods(post/get)
    return "<h1>Hello world</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to flask tutorial"

@app.route('/index')
def index():
    #return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and the score is "+str(score)

#Result checker
'''@app.route('/results/int:marks>')
def results(marks):
    result=""
    if marks>50:
        result='success'
    else:
        result='fail'
        return redirect(url_for(result,score=marks))'''

@app.route('/results/<int:marks>')
def results(marks):
    if marks > 50:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))



if __name__=="__main__": #Entry point of program
    #app.run()
    app.run(debug=True) #Never use this in production, only development env. Used for reloading of page