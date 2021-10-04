import random

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

# chnage the key name 
app.secret_key = "random key"  


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/guess', methods = ['POST'] )
def guessNumber():

    print(request.form)

    if 'guessedNum' not in session:
        randomNum = random.randint(1,100);
        session['randomNum'] = randomNum;

    session['guessedNum'] = int(request.form['input']);
    

    return redirect('/answer')

@app.route('/answer')
def answer():


    guessedNum = session['guessedNum']
    randomNum = session['randomNum']
    session['showBackButton'] = False
    text = " "

    print(session);

    print(request);
    if(guessedNum < randomNum):
        print("Too Low");
        text += "Too Low!"
        return render_template('answer.html', answer = text, color = "danger")
    elif(guessedNum > randomNum):
        print("Too High")
        text += "Too High!"
        return render_template('answer.html', answer = text, color = "danger")
    else:
        print( str(guessedNum) + "was the Number")
        text += (str(guessedNum) + " was the Number!")
        session['showBackButton'] = True
        return render_template('answer.html', answer = text, color = "success")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
