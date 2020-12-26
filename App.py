#Importing necessary libraries
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Creating an Application
app = Flask(__name__)

#Training the ChatBot
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


#Displaying the HTML page
@app.route("/")
def home():
    return render_template("index.html")


#Displaying the responses
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


#Main Function
if __name__ == "__main__":
    app.run()

