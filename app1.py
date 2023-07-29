from flask import Flask,request
import json

obj=Flask(__name__)

@obj.route('/') #Creating home route
def welcome():
    return "Welcome to flask"

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"] #To request input in form of json
    number1=request.json["number1"]
    number2=request.json["number2"]


    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=='multiply':
        result=int(number1)*int(number2)
    elif operation=='division':
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return f"The operation is {operation} and the result is {result}"

print(__name__)

if __name__=="__main__":
    obj.run(debug=True)
