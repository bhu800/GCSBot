import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

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
    # ERROR_THRESHOLD = 0.25
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
    return {'response': result, 'probability': ints[0]["probability"], 'tag': tag}

def chatbot_response(msg):
    ints = predict_class(msg, model)
    print(ints)
    res = getResponse(ints, intents)
    return res