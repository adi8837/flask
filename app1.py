from flask import Flask,request,render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to flask"

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"] #To request input
    number1=request.json["number1"]
    number2=request.json["number2"]


    if operation=="add":
        result=number1+number2
    elif operation=='multiply':
        result=number1*number2
    elif operation=='division':
        result=number1/number2
    else:
        result=number1-number2
    return result

if __name__=="__main__":
    app.run(debug=True)
