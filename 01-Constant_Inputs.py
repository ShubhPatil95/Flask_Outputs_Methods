'''
URL Format 
Addition: http://localhost:8000/addition
Substraction: http://localhost:8000/substraction
'''

from flask import Flask

app=Flask(__name__)

@app.route('/substraction')
def Substraction():      
    a=20
    b=10
    c=int(a)-int(b)
    return f"Substraction is {c}"

@app.route('/addition')
def Addition():
    a=20
    b=10
    c=int(a)+int(b)
    return f"Addition is {c}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)

    