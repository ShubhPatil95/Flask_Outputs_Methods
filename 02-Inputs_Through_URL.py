'''
URL Format 
Addition: http://localhost:8000/addition?a=100&b=100
Substraction: http://localhost:8000/substraction?a=100&b=100
'''

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/substraction')
def Substraction():      
    a=request.args.get("a")
    b=request.args.get("b")
    c=int(a)-int(b)
    return f"Substraction is {c}"

@app.route('/addition')
def Addition():
    a=request.args.get("a")
    b=request.args.get("b")
    c=int(a)+int(b)
    return f"Addition is {c}"
  
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)

    