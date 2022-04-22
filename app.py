# Step – 1(import necessary library)
from flask import (Flask, render_template, request, redirect, session)
from flask_mysqldb import MySQL
# Step – 2 (configuring your application)
app = Flask(__name__)
app.secret_key = 'ItShouldBeAnythingButSecret'

# step – 3 (creating a dictionary to store information about users)
user = {"username": "abc", "password": "xyz"}



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'June2020$$**'
app.config['MYSQL_DB'] = 'practice'
app.config['MYSQL_DB1'] = 'dataset'
app.config['MYSQL_DB2'] = 'dataset2'
mysql = MySQL(app)
mysql1 = MySQL(app)
mysql2= MySQL(app)


# Step – 4 (creating route for login)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/dashboard')

        return "<h1>Wrong username or password</h1>"

    return render_template("login.html")


# Step -5(creating route for dashboard and logout)
@app.route('/dashboard')
def dashboard():
    if 'user' in session and session['user'] == user['username']:
        return '<h1>Welcome to the dashboard</h1>'

    return '<h1>You are not logged in.</h1>'


# Step -6(creating route for logging out)
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

# Coonecting to Db
@app.route('/insert/student', methods=['POST', 'GET'])
def InsertStudent():
    if request.method == 'POST':

        data = request.get_json()

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')

        cursor = mysql.connection.cursor()

        sql = "INSERT INTO practice.student (firstname, lastname, email) VALUES (%s, %s,%s)"
        val = (firstname, lastname,email)
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()



        return f"Done!!"
#Searching from DB

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        data = request.get_json()
        firstname = data.get('firstname')
        cursor = mysql.connection.cursor()
        # search by firstname
        cursor.execute("SELECT firstname from practice.student WHERE firstname LIKE %s ", (firstname, firstname))
        mysql.connection.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cursor.execute("SELECT firstname from practice.student")
            mysql.connection.commit()
            data = cursor.fetchall()
            sql = "INSERT INTO practice.student (firstname) VALUES (%s)"
            val = (firstname)
            cursor.execute(sql, val)
            mysql.connection.commit()
            cursor.close()
    return f"Done!!"
# Retrieving data from dataset to Dataset2
mydb = mysql1.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="dataset"
)

mydb2 = mysql2.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="dataset2"
)
@app.route('/insert/dataset', methods=['POST', 'GET'])
def Insertdata():
        cursor1 = mydb1.cursor()

        mycursor.execute("SELECT * FROM agents")

        data = mycursor.fetchall()

        AGENT_CODE = data.get('AGENT_CODE')
        AGENT_NAME = data.get('AGENT_NAME')
        WORKING_AREA = data.get('WORKING_AREA')
        COMISSION = data.get('COMISSION')
        PHONE_NO = data.get('PHONE_NO')
        COUNTRY = data.get('COUNTRY')

        curs = mysql2.connection.cursor()

        sql = "INSERT INTO dataset2.dagents (AGENT_CODE, AGENT_NAME, WORKING_AREA, COMISSION, PHONE_NO, COUNTRY) VALUES (%s, %s,%s, %s, %s,%s)"
        val = (AGENT_CODE, AGENT_NAME, WORKING_AREA, COMISSION, PHONE_NO, COUNTRY)
        curs.execute(sql, val)
        mysql2.connection.commit()
        cursor.close()
        return f"Done!!"



# Step -7(run the app)
if __name__ == '__main__':
    app.run(debug=True)
