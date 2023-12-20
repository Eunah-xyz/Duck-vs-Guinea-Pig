from flask import Flask, render_template, request
from DuckvsGuineaPig import conversation
# from DvG import conversation

app = Flask(__name__)

#new_question="Hello!"
bot1_answers=[]
bot2_answers=[]
input_text = "Hello"
duck = True

@app.route('/')
def index():
    # By adding global duck at the beginning of the index function, you're telling Python that the variable duck is a global variable
    global duck
    if duck == True:
        # Even iteration, use bot1
        convo = conversation(input_text, duck)
        bot1_answers.append(convo[0])
    else:
        # Odd iteration, use bot2
        convo = conversation(input_text, duck)
        bot2_answers.append(convo[0])
    duck = not duck

    return render_template("index.html", bot1_answers_html=bot1_answers, bot2_answers_html=bot2_answers)
