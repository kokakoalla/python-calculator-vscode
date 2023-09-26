from flask import Flask, render_template, request

app = Flask(__name__)

def perform_calculation(num1, num2, operator):
    if operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    elif operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

@app.route("/")
def home():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operator = request.form["operator"]
    result = perform_calculation(num1, num2, operator)
    return render_template("calculator.html", result=result)
