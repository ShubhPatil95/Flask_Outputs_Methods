'''
URL Format 
http://localhost:8000
'''

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data_req=dict(request.form) 
                data=list(data_req.values())
                data1 =list(map(int, data[:-1]))
                number1=data1[0]
                number2=data1[1]
                Operation=data[-1]
                
                if Operation=="SUM":
                    response=number1+number2
                elif Operation=="SUB":
                    response=number1-number2
                else:
                    response="Incorrect Operation"
                return render_template("index.html", response=response)
        except:
            return "Something Went Wrong"
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)