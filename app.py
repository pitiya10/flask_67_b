from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)

# For Database
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "flower_shop"

@app.route("/home")
def home():
   # return "<h1>Hello world</h1>"
    name = "Anya"
    age = 8
    my_dict = {"name": "Yor", "age":26}
    return render_template("home.html", name=name, age=age,
    my_dict=my_dict)

@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@app.route("/store", methods=["POST"])
def store():
    if request.method == "POST":
        flower_name = request.form['flower_name']
        lat_num = request.form['lat_num']
        long_num = request.form['long_num']
        place = request.form['place']
        detail = request.form['detail']
        print("input:", flower_name, lat_num, long_num, place, detail)

        # Connect Database
        my_db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME
        )
        my_cursor = my_db.cursor(dictionary=True)
        sql="INSERT INTO flowers (flower_name, lat_num, long_num, place, detail) VALUES (%s, %s, %s, %s, %s)"
        val = (flower_name, lat_num, long_num, place, detail)
        my_cursor.execute(sql, val)
        my_db.commit()

        return redirect("/create")
    else:
        return "<h1>No Way!</h1>"

if __name__ == "__main__":
   # app.run() # production
        app.run(debug=True) # Developer