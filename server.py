import random

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

# chnage the key name 
app.secret_key = "random key"  


@app.route('/')
def home():

    # print(session)
    # if 'counter' in session:
    #     print('listOfFruits exits!')
    #     session['counter'] += 1;
    #     print(session['counter'])
        
    # else:
    #     print("there is no fruits array in session")
    #     session['anything'] = ['apple', 'bananna']
    #     session['counter'] = 0;
    return render_template('index.html')

@app.route('/guess', methods = ['POST'] )
def guessNumber():

    print(request.form)

    if 'guessedNum' not in session:
        randomNum = random.randint(1,101);
        session['randomNum'] = randomNum;

    session['guessedNum'] = int(request.form['input']);
    

    return redirect('/answer')

@app.route('/answer')
def answer():

    guessedNum = session['guessedNum']
    randomNum = session['randomNum']
    text = " "
    if(guessedNum < randomNum):
        print("Too Low");
        text += "Too Low!"
    elif(guessedNum > randomNum):
        print("Too High")
        text += "Too High!"
    else:
        print( str(guessedNum) + "is the Number")
        text += (str(guessedNum) + " is the Number!")

    print(session);

    print(request);

    return render_template('answer.html', answer = text)

@app.route('/right-answer')
def rightAnswer():

    guessedNum = session['guessedNum']
    randomNum = session['randomNum']
    text = " "
    if(guessedNum == randomNum):
        print( str(guessedNum) + "is the Number")
        text += (str(guessedNum) + " is the Number!")
    
    print(session);

    print(request);

    return render_template('right_answer.html', answer = text)

@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/")


    return render_template('right_answer.html', answer = text)
if __name__=="__main__":
    app.run(debug=True)
