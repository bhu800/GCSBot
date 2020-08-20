import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, redirect

from flask_socketio import SocketIO, send, emit, join_room, leave_room

from time import localtime, strftime

model = load_model('trainedModelInUse/FAQbot_model.h5') # accuracy = 93.6%
import json
import random
intents = json.loads(open('trainedModelInUse/intents.json').read())
words = pickle.load(open('trainedModelInUse/words.pkl','rb'))
classes = pickle.load(open('trainedModelInUse/classes.pkl','rb'))

# intent-classification utility functions
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    # print("p: ", p)
    res = model.predict(np.array([p]))[0]
    # print("res: ", res)
    ERROR_THRESHOLD = 0.25
    # results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results = [[i,r] for i,r in enumerate(res)]
    # print("results: ", results)
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    print(ints)
    res = getResponse(ints, intents)
    return res

# user_query = "question goes here"
# bot_reply = "bot reply goes here!"

# configure flask app
app = Flask(__name__)
app.secret_key = 'Illuminati'

# Initialize flask-SocketIO
socketio = SocketIO(app) 

# @app.route('/')
# def hello_world():
#     return render_template('index.html', questionAsked=query, response=reply)

# @app.route('/signup', methods = ['POST'])
# def signup():
# 	global query
# 	global reply
# 	query = request.form['question']
# 	response = chatbot_response(query)
# 	print(response)
# 	reply = response
# 	return redirect('/')

@app.route('/')
def chatBot():

    return render_template('chatbot.html') 

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('query')
def handle_query(user_query):
    """Broadcast user_query and bot_response and """

    user_query = user_query["msg"]
    print("user: ", user_query)
    bot_response =  chatbot_response(user_query)
    print("Bot: ", bot_response)
    emit('response', {"user_query": user_query, "bot_response": bot_response}, callback=messageReceived)



if __name__ == "__main__":
    socketio.run(app, debug=True)
