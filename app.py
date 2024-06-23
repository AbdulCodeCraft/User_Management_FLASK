from flask import Flask, render_template,url_for,redirect,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "@A1b2d3u4l5"
app.config["MYSQL_DB"] = "crud"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

# Inserting new user

@app.route("/addUsers",methods =['GET','POST'])
def addUsers():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        con = mysql.connection.cursor()
        sql = "insert into users(NAME,AGE,CITY) value (%s,%s,%s)"
        con.execute(sql,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("index"))
    return render_template("addUsers.html")


#Home page loading
@app.route('/')
def index():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM users"
    con.execute(sql)
    res = con.fetchall()
    return render_template('index.html',datas = res)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 