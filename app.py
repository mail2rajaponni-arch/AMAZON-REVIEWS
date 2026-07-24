import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask,request,jsonify

app=Flask(__name__)

model=joblib.load('model.joblib') #Loading the saved model
vectorizer=joblib.load('vectorizer.joblib')#loading the saved TF-IDF vectorizer

@app.route("/predict",methods=["POST"])# wheneveruser POSTs data to "/predict",call this function
def predict():

    data=request.get_json() #Reading the incoming JSON data
    
    reviews=data['reviews'] #Extract the feature valuesfrom the message
    
    process_review=preprocess(reviews) #preprocess the review posted
    
    process_review=vectorizer.transform([process_review])  #Extract featuresfrom the review
    
    prediction=model.predict(process_review) #predict the sentiment

    return jsonify({"prediction":"positive" if prediction[0] == "1" else "negative"})
    # output the sentiment.jsonify is used to convert python dict to JSON object


@app.route("/health",methods=['GET']) # used to check if the server is running.It'll output{"status":"ok"} if serveris running.
def health():
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    import os
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",5000))) # Host :0.0.0.0 means any computer can connect to this host