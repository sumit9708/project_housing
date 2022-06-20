import sys
from flask import Flask,request,jsonify
from housing.logger import logging
from housing.exception import HousingException


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "CI/CD pipe line created and deployed to heroku (Sumit Bhagat)"

if __name__=="__main__":
    app.run(debug=True)