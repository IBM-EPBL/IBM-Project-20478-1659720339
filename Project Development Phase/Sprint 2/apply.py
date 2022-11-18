import ibm_db
from flask import Flask, redirect, render_template, request, session, url_for

app=Flask(__name__)

conn=ibm_db.connect('DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=certi.crt;UID=spy48271;PWD=80QbK1bDsTDY3NOO;','','')

@app.route("/")
def index():
        return render_template("Register.html")


@app.route("/dash",methods=["GET","POST"])
def dash():
   return render_template("Register.html")

@app.route("/Register",methods=["GET","POST"])
def Register():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        phonenumber=request.form['phonenumber']
        emailid=request.form['emailid']
        sql="Insert INTO REGISTER VALUES(?,?,?,?)"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.bind_param(stmt,3,phonenumber)
        ibm_db.bind_param(stmt,4,emailid)
        ibm_db.execute(stmt)
        return render_template("Login.html")


@app.route("/Login",methods=["GET","POST"])
def Login():
    if request.method=="POST":
        Username=request.form['username']
        Password=request.form['password']
        sql="Insert INTO LOGIN VALUES(?,?)"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,Username)
        ibm_db.bind_param(stmt,2,Password)
        ibm_db.execute(stmt)
        return render_template("upload.html")

        
@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method=="POST":
         myfile=request.form['myfile']
         sql="Insert INTO UPLOAD VALUES(?)"
         stmt=ibm_db.prepare(conn,sql)
         ibm_db.bind_param(stmt,1,myfile)
         ibm_db.execute(stmt)
         return render_template("BMI_Calculation.html")



@app.route("/BMI_Calculation",methods=["GET","POST"])
def BMI_Calculation():
    if request.method=="POST":
         Height=request.form['Height']
         Weight=request.form['Weight']
         sql="Insert INTO BMI_CALCULATION VALUES(?,?)"
         stmt=ibm_db.prepare(conn,sql)
         ibm_db.bind_param(stmt,1,Height)
         ibm_db.bind_param(stmt,2,Weight)
         ibm_db.execute(stmt)
         return render_template("ref.html")


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)      



        
