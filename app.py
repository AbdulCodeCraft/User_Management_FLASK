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

# Edit user
@app.route('/editUser/<int:id>', methods=['GET', 'POST'])
def editUser(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        sql = "UPDATE users SET NAME=%s, AGE=%s, CITY=%s WHERE ID=%s"
        con.execute(sql, [name, age, city, id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for('index'))
    sql = "SELECT * FROM users WHERE ID=%s"
    con.execute(sql, [id])
    res = con.fetchone()
    con.close()
    return render_template('editUser.html', user=res)

# Delete user
@app.route('/deleteUser/<int:id>')
def deleteUser(id):
    con = mysql.connection.cursor()
    sql = "DELETE FROM users WHERE ID=%s"
    con.execute(sql, [id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 