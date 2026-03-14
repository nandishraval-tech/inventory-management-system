from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():

    product = request.args.get("product")

    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%'+product+'%',))

    results = cursor.fetchall()

    connection.close()

    return render_template("search.html", products=results)

if __name__ == "__main__":
    app.run(debug=True)