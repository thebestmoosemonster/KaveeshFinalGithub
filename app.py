from flask import Flask,render_template,session,request,redirect,url_for
import sqlite3 as sql
app = Flask(__name__)

app.config["SECRET_KEY"]="Roboloxy"
user_details={"Kaveesh":"1ombreeze","yitiej":"Ipadpro1","ishyr1234":"Givemefive"}
@app.route('/')
def index():
    return render_template("newindex.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")
# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if session.get("authenticated") ==True:
        session["score"]=0
        return render_template("loginSuccess.html")
    else:
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_user",methods=["POST"])
def register_user():
    username=request.form.get("username")
    password=request.form.get("password")
    session["username"]=request.form["username"]
    print(username)
    with sql.connect("Kaveesh.db") as conn:
        cur=conn.cursor()
        cur.execute("INSERT into user(username,password)VALUES(?,?)",(username,password))
        conn.commit()
        print("changes are commited")
        message= "operation successful"
    return render_template("registerSuccess.html",message=message)

@app.route("/verify",methods=['POST','GET'])
def verify():
    username=request.form.get("username")
    password=request.form.get("password")
    returnvale = verify_user(username,password)
    # returnvale = verify_user(username,password)

    if(returnvale==True):
        session["authenticated"]=True
        return render_template("loginSuccesws.html",username=username)
    else:
        session["authenticated"]=False
        return render_template("loginfailure.html")
        

def loginsucess(dictionary,username,password):
    if (dictionary.get(username,"Invaild details")==password):
        return True
    else:
        return False
def verify_user(username,password):
    loginsucess = False
    conn = sql.connect('Kaveesh.db')
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute('SELECT password from user where username = ?' ,[username])
    records = cur.fetchall()
    dbpassword = ''
    for record in records:
        dbpassword = record[0]
    if dbpassword==password:
        loginsucess=True
    else:
        loginsucess=False
    return loginsucess

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/q1")
def q1():
    return render_template("q1.html",score=0)

@app.route("/q2",methods=["POST","GET"])
def q2():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q2.html",score= c_score)

@app.route("/q3",methods= ["POST","GET"])
def q3():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q3.html",score= c_score)

@app.route("/q4",methods= ["POST","GET"])
def q4():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q4.html",score= c_score)

@app.route("/q5",methods= ["POST","GET"])
def q5():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q5.html",score= c_score)

@app.route("/space")
def space():
    return render_template("space.html")

@app.route("/mars")
def mars():
    return render_template("Mars.html")

@app.route("/venus")
def venus():
    return render_template("Venus.html")

@app.route("/mecury")
def mecury():
    return render_template("Mecury.html")

@app.route("/neptune")
def neptune():
    return render_template("Neptune.html")

@app.route("/pluto")
def pluto():
    return render_template("Pluto.html")

@app.route("/saturn")
def saturn():
    return render_template("saturn.html")

@app.route("/uranus")
def uranus():
    return render_template("Uranus.html")

@app.route("/jupiter")
def jupiter():
    return render_template("Jupiter.html")

@app.route("/earth")
def earth():
    return render_template("Earth.html")


@app.route("/submit")
def submit():
    return render_template("sumbit.")

@app.route("/q6",methods= ["POST","GET"])
def q6():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q6.html",score= c_score)

@app.route("/q7",methods= ["POST","GET"])
def q7():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q7.html",score= c_score)

@app.route("/q8",methods= ["POST","GET"])
def q8():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q8.html",score= c_score)

@app.route("/q9",methods= ["POST","GET"])
def q9():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q9.html",score= c_score)    

@app.route("/q10",methods= ["POST","GET"])
def q10():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q10.html",score= c_score)

@app.route("/q11",methods= ["POST","GET"])
def q11():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q11.html",score= c_score)


@app.route("/q12",methods= ["POST","GET"])
def q12():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")

    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("q12.html",score= c_score)



@app.route("/start_quiz",methods= ["POST","GET"])
def start_quiz():
    if session.get("authenticated") ==True:
        session["score"]=0
        return render_template("q1.html", score = 0)
    else:
        return render_template("loginfailure.html")

@app.route("/end_quiz",methods= ["POST","GET"])
def end_quiz():
    p_score= session.get("score",0)
    c_score = p_score
    s_answer = request.form.get("answer")
    c_answer = request.form.get("ca")
    print(c_score)
    if s_answer== c_answer:
        marks= 10
        c_score= p_score+marks
        session["score"]= c_score    
    return render_template("end_quiz.html",score= c_score)

@app.route("/violin")
def violin():
    return render_template("Music.html")

@app.route("/helicopter")
def helicopter():
    return render_template("Lego.html")

@app.route("/registerSuccess")
def registerSuccess():
    return render_template("registerSuccess.html")

@app.route("/robloxlink")
def robloxlink():
    return render_template("robloxlink.html")

@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")

@app.route("/art")
def art():
    return render_template("art.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

def addition(num1,num2):
    add= num1+num2
    return add

def subtraction(num1,num2):
    subtract= num1-num2
    return subtract

def multiplication(num1,num2):
    multiply= num1*num2
    return multiply

def division(num1,num2):
    divide= num1/num2
    return divide


@app.route("/calculator_verify", methods= ["POST"])
def calculator_verify():
    result=0
    operator1 = request.form.get("enternumber1")
    operator2 = request.form.get("enternumber2")
    selector=request.form.get("selector")
    operator1= int(operator1)
    operator2= int(operator2)
    if selector== 'Addition':
        result= addition(operator1,operator2)
    elif selector== 'Subtraction':
        result= subtraction(operator1,operator2)
    elif selector== 'Multiplication':
        result= multiplication(operator1,operator2)
    elif selector== 'Division':
        result= division(operator1,operator2)
    # return '<h1> Result for {} on {} and {} is {} </h1>'.format(selector,operator1,operator2,result)
    return render_template('math.html',result=result,operator1=operator1,operator2= operator2)
    




if __name__ == '__main__': 
    app.run(debug=True)