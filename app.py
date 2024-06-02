from flask import Flask, render_template, url_for, request
from math import cos, sin, tan, sqrt, exp, log, acosh,  asinh, atanh, asin, acos

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html',home=True)

@app.route("/advanced")
def advanced():
    return render_template('advanced.html')

@app.route("/simple")
def simple():
    return render_template('simple.html')

@app.route("/calculate",methods=["post"])
def calculate():
    first_number=int(request.form["firstNumber"])
    operation=request.form["operation"]
    second_number=int(request.form["secondNumber"])
    color="alert-success"
    try:
        if operation=="plus":
            result=first_number+second_number
            note="Addition was performed successfully"
        elif operation=="minus":
            result=first_number-second_number
            note="Subtraction was performed successfully"
        elif operation=="multiply":
            result=first_number*second_number
            note="Multiplication was performed successfully"
        elif operation=="divide":
            result=first_number/second_number
            note="Division was performed successfully"
        else:
            result=0
            note="There is an Error! Please try again."
            color="alert-warning"
    except Exception as error:   
        result=0
        note=f"An Exception occurred: {type(error).__name__}"  
        color="alert-danger"    
    
    return render_template('simple.html',result=result,note=note, color=color)

@app.route("/calculate_advanced",methods=["post"])
def calculate_advanced():
    first_number=int(request.form["firstNumber"])
    operation=request.form["operation"]
    color="alert-success"
    try:
        if operation=="cos":
            result=cos(first_number)
            note="cos has been calculated."
        elif operation=="sin":
            result=sin(first_number)
            note="sin has been calculated."
        elif operation=="tan":
            result=tan(first_number)
            note="tan has been calculated."
        elif operation=="sqrt":
            result=sqrt(first_number)
            note="square root has been calculated."
        elif operation=="exp":
            result=exp(first_number)
            note="exp has been calculated."
        elif operation=="log":
            result=log(first_number)
            note="log has been calculated."
        elif operation=="acosh":
            result=acosh(first_number)
            note="acosh has been calculated."  
        elif operation=="asinh":
            result=asinh(first_number)
            note="asinh has been calculated."
        elif operation=="atanh":
            result=atanh(first_number)
            note="atanh has been calculated."
        elif operation=="acos":
            result=acos(first_number)
            note="acos has been calculated."   
        elif operation=="asin":
            result=asin(first_number)
            note="asin has been calculated."                
        else:
            result=0
            note="No function has been selected. Try Again."
            color="alert-warning"
    except Exception as error:
        result=0
        note=f"An Exception occurred: {type(error).__name__}"  
        color="alert-danger"      
    
    return render_template('advanced.html',result=result,note=note, color=color)


if __name__=='__main__':
    app.run(debug=True, port=5005)