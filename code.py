from flask import make_response,Flask,redirect,render_template,url_for,request,session
app = Flask(__name__,static_url_path='/static')



import minimax
app.secret_key = 'your secret'

@app.route('/')
def index():            #functions that handle application URLs are called view functions.
    return render_template('main.html')

@app.route('/resetBoard')
def reset():
    return redirect(url_for("index"))



@app.route('/startgame', methods =['GET', 'POST'])
def loop():
    game_is_on=True
    i=1    
    game_board=dict()
    while(i<10):
        cell='c'+str(i)
        game_board.update({str(i):request.form[cell]})
        i=i+1   
    ret=minimax.game_player(game_board,0,game_is_on)
    session['game']=ret[0]
    session['chance']=ret[1]
    session['status']=ret[2]
    if (len(ret[3])!=0):
        session['msg']= ret[3]
    else:
        session['msg']=''
    return render_template("second.html",btn="Next Move")
    
@app.route('/startgame/moves', methods =['GET', 'POST'])    
def l():
    if session['status']==True:
        game_board=session['game']
        game_is_on=session['status']

        ret=minimax.game_player(game_board,session['chance'],game_is_on)
        
        session['game']=ret[0]
        session['chance']=ret[1]
        session['status']=ret[2]
        session['msg']=ret[3]
        if (len(session['msg'])==0):
            return render_template("second.html",btn="Next Move")
        else:
            return render_template("second.html",btn="Return home")
    else:
        return redirect(url_for("index"))
    