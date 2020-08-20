# GCSBot

GCS is Guidance and Counseling Service of IIT Mandi, which manages the whole admission process from councelling and registration to induction programme for newly joined students.  
A freshman joining the institute has a lot of information to search, assimilate and keep track of. What is the procedure for registration? When will I get my ID card? Where can I get food late at night around the campus? Which documents are required to submit at registration desk? How can I book institute guest house for my parents? These are just a few of the very common queries one might have apart from a ton of other academics and clubs related queries.
Although GCS tries it's best to help students with their queries by it's freshman-forum fb pages, faq pages and assigning mentors for each freshman, but still there is a scope for solving most of these queries much more quickly and efficiently, as they are generally standard and common among freshers.  

**GCSBot is a retrevial-based chatbot, which tries to solve the same problem.**

## How to deploy ?

Get the code
```bash
$ git clone https://github.com/bhu800/GCSBot.git
$ cd GCSBot
```
Virtualenv modules installation (Unix based systems)
```bash
$ virtualenv env
$ source env/bin/activate
```
Virtualenv modules installation (Windows based systems)
```bash
$ virtualenv env
$ source env/bin/activate
```

Install modules
```bash
$ pip3 install -r requirements.txt
```   

This ChatBot backs up the chat data in google sheets so that it can be later be used to improve prediction model of Bot.
For this you have to make make project and get credentials to use google sheets api from https://console.cloud.google.com/.
There are a few steps that need to be followed to start using the google sheets API:

* Create a project on google cloud console
* Activate the google drive API
* Create credentials for the google drive API
* Activate the google sheets API
* Install a few modules with pip
* Open the downloaded json file and get the client email
* Share the desired sheet with that email
* To Connect google sheet via python code, rename downloaded credentials file GCSBot_Google_API_Credentials.json and put it in the root directory
For more detailed setup you can follow [this tutorial](https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/).

 Now start the application (development mode)
 ```bash
 $ python server.py # default port 5000
 ```
 
 Access the web app in browser: http://127.0.0.1:5000

## Task-List
- [ ] Building a deep learning model for intent classification
    - [x] try basic models
    - [ ] try open source chatbot libraries like rasa.
    - [ ] try other state of the art models
    - [ ] try third party APIs like dialogueflow etc.
- [x] Deplying model using flask
- [x] Using socket.io for making chatbot real-time
- [x] adding frontend and chatbot UI
- [x] store user queries and Bot's reponses on them in database/sheet, so that we can later improve our database and hence prediction model
