# --> Url Routing

from flask import Flask,render_template,request,redirect,url_for,jsonify

## create a simple application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return "<h1>Hello World!</h1>"


@app.route("/index",methods=["GET"])
def index():
    return "Another Page"

@app.route("/success/<score>")
def success(score):
    return "Person Has Passed and score is : " + score

@app.route("/failed/<score>")
def failed(score):
    return "The Person Has Failed and score is : " + score


@app.route("/form",methods = ["POST","GET"])

def form():
    if request.method == "GET":
       return render_template("form.html")
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        english = float(request.form["history"])
        average = (maths + science + english)/3
       
        # return render_template("form.html",score = average)
        res = ""
        if average >= 50:
            res = "success"
        else:
            res = "failed"
        return redirect(url_for(res,score = average))
    
@app.route("/api", methods = ["POST"])
def api():
    data = request.get_json()
    a_val = float(dict(data)["a"])
    b_val = float(dict(data)["b"])
    c_val = float(dict(data)["c"])
    return jsonify({"average":(a_val+b_val+c_val)/3})

if __name__ == "__main__":
    app.run(debug=True)