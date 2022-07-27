# Put your app in here.

from re import A
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add")
def add_num():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = add(a, b)

    return f"<html><body><h1>'{total}'</h1></body></html>"

@app.get("/sub")
def sub_num():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = sub(a, b)

    return f"<html><body><h1>'{total}'</h1></body></html>"

@app.get("/mult")
def mult_num():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = mult(a, b)

    return f"<html><body><h1>'{total}'</h1></body></html>"

@app.get("/div")
def div_num():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = div(a, b)

    return f"<html><body><h1>'{total}'</h1></body></html>"

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.get("/math/<operation>")
def math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    total = operations[operation](a, b)
    return f"<html><body><h1>'{total}'</h1></body></html>"