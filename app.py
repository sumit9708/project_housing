from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route("/")
def hi():
    return "CI/CD pipe line created and deployed to heroku (Sumit Bhagat)"

if __name__=="__main__":
    app.run(debug=True)