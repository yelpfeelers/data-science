
import sys

"""
Entry Point for Mota Analytica Flask Application
"""
#Dependencies
#   NLTK
import nltk
from nltk import sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#   Flask
from flask import Flask, request, jsonify,render_template
from flask_pymongo import PyMongo
from flask_cors import CORS


#Setup
app = Flask(__name__)
CORS(app)


#Pre-trained Naive-Bayes Classifier
sid = SentimentIntensityAnalyzer()





#Sentiment Analysis 

def basic_sentiment_analysis(review_input):
    sentiment_values = sid.polarity_scores(review_input)
    scoreval = sentiment_values['compound']
    scoreval = scoreval * 0.25
    scoreval = scoreval * 10
    scoreval += 2.5
    return scoreval

#Connecting to the database
app.config['MONGO_URI'] = 'mongodb://localhost:27017/yelp'
mongo = PyMongo(app)



@app.route('/')
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'API Version': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Mota-Analytica API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


#Hardcoded feature, will delete comment when app is ready for deployment
""" 
@app.route('/review', methods=['GET'])
def get_all_stars():
    review = mongo.db.reviews
    output = []
    for r in review.find( {"business_id" : "qx6WhZ42eDKmBchZDax4dQ"} ).limit(50):
        output.append({'id' : r["business_id"], 'review' : r["text"]})
    return jsonify({'result' : output})
 """


#This aggregates and formats a large amount about taco restaurants in las vegas
#This is commented out because it uses a substantial amount of system resources to run on the API (Mongo doesn't like SQL styled joins)
'''@app.route('/tacotest', methods=['GET'])
def lots_of_tacos():
    businesses = mongo.db.business
    business_list = []
    output1 = []
    review = mongo.db.reviews
   
    for b in businesses.find( {"$text": {"$search": "taco"}, "city" : "Las Vegas" } ).limit(10):
        business_list.append(b["business_id"])
        output1.append({  'name' : b["name"] , 'id': b["business_id"],  'reviews': [] }    ) 

    for o in output1:
       
        for r in review.find( {"business_id" : o['id']} ).limit(40):
            score = r['stars']
            review_text = r['text']
            adjusted_score = basic_sentiment_analysis(review_text)
            o['reviews'].append({ 'text' : r['text'], 'stars' : score, 'adjusted_stars' : adjusted_score  } )
            
            
       
    output = output1
      
                
    return jsonify( {'results' : output } )'''




@app.route("/business/<business_id>", methods=['GET'])
def fetch_reviews(business_id):

    #page = request.args.get('page')
    page = 1
    review = mongo.db.reviews
    
    output = []
    for r in review.find( {"business_id" : business_id} ).skip((page-1)*50).limit(50):
        review_text = r['text']
        adjusted_score = basic_sentiment_analysis(review_text)
        output.append(  {   'score': r['stars'],'adjusted score' : adjusted_score , 'review' : review_text  }   )
    return jsonify({'result' : output})




#For running sentiment analysis on user input
@app.route("/sentiment/<user_string>", methods=['GET'])
def analyze_user_input(user_string):
    user_string = str(user_string)

    user_string = user_string.replace('_', ' ')
    output_text = user_string
    
    user_string = basic_sentiment_analysis(user_string)
    
    return jsonify({output_text : user_string })






if __name__ == "__main__":
    app.run()
   