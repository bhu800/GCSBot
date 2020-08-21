from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from time import localtime, strftime
import os

# Custom Modules

# module to backup chat data in google sheets 
from handle_spreadsheet import appendDataInSpreadSheet
# module for intent classification and chatbot response
from intentClassifier import chatbot_response

# configure flask app
app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET') # flask app secret key from heroku
app.secret_key = "Illuminati"

# Initialize flask-SocketIO
socketio = SocketIO(app) 

@app.route('/')
def chatBot():
    return render_template('chatbot.html') 

@socketio.on('query')
def handle_query(user_query):
    """Broadcast user_query and bot_response and backup chat in google sheet """

    user_query = user_query["msg"]
    print("user: ", user_query)
    # get prediction using deep learning model
    prediction =  chatbot_response(user_query)
    bot_response = prediction["response"]
    tag = prediction["tag"]
    probability = prediction["probability"]
    print("Bot: ", bot_response)
    timestamp_short = strftime('%I:%M%p', localtime())
    timestamp_long = strftime('%b-%d %I:%M%p', localtime())
    # broadcast message
    emit('response', {"user_query": user_query, "bot_response": bot_response, "timestamp": timestamp_short})

    # backup chat in google sheet
    appendDataInSpreadSheet(timestamp_long, user_query, tag, probability)

if __name__ == "__main__":
    socketio.run(app, debug=True)
    # app.run() # using gunicorn server
