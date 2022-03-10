'''
URL Format 
http://localhost:8000/apidocs
'''
from flask import Flask, request
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

@app.route('/substraction')
def Substraction():  
    
    """Click here for substraction
    This is Substraction Program
    ---
    parameters:  
      - name: First_Number
        in: query
        type: number
        required: true
      - name: Second_Number
        in: query
        type: number
        required: true
    responses:
        200:
            description: Here is Addition
    """
    a=request.args.get("First_Number")
    b=request.args.get("Second_Number")
    c=int(a)-int(b)
    return f"Substraction is {c}"

@app.route('/addition')
def Addition():
    
    """Click here for addition
    This is Addition Program
    ---
    parameters:  
      - name: First_Number
        in: query
        type: number
        required: true
      - name: Second_Number
        in: query
        type: number
        required: true
    responses:
        200:
            description: Here is Addition
    """
    a=request.args.get("First_Number")
    b=request.args.get("Second_Number")
    c=int(a)+int(b)
    return f"Addition is {c}" 

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)

    