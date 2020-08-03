# GCSBot

GCS is Guidance and Counseling Service of IIT Mandi, which manages the whole admission process from councelling and registration to induction programme for newly joined students.  
A freshman joining the institute has a lot of information to search, assimilate and keep track of. What is the procedure for registration? When will I get my ID card? Where can I get food late at night around the campus? Which documents are required to submit at registration desk? How can I book institute guest house for my parents? These are just a few of the very common queries one might have apart from a ton of other academics and clubs related queries.
Although GCS tries it's best to help students with their queries by it's freshman-forum fb pages, faq pages and assigning mentors for each freshman, but still there is a scope for solving most of these queries much more quickly and efficiently, as they are generally standard and common among freshers.  

**GCSBot is a retrevial-based chatbot, which tries to solve the same problem.**

## How to deploy ?
```bash
$ # Get the code
$ git clone https://github.com/bhu800/GCSBot.git
$ cd GCSBot
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Start the application (development mode)
$ python server.py # default port 5000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:5000
```


## Task-List
- [ ] Building a deep learning model for intent classification
    - [ ] try basic models
    - [ ] try open source chatbot libraries like rasa.
    - [ ] try other state of the art models
    - [ ] try third party APIs like dialogueflow etc.
- [ ] Deplying model using flask
- [ ] Using socket.io for making chatbot real-time
- [ ] adding frontend and chatbot UI
