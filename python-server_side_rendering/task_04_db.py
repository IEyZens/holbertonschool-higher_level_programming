from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def read_csv(file_path):
    with open(file_path, newline='') as file:
        dict_reader = csv.DictReader(file)
        return [
            {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            for row in dict_reader
        ]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)
        items = data.get("items", [])
    return render_template("items.html", items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        data = read_json("products.json")

    elif source == "csv":
        data = read_csv("products.csv")

    elif source == "sql":
        connection = sqlite3.connect("products.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()

        data = []
        for row in rows:
            product = {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3]
            }
            data.append(product)
        connection.close()

    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id is None:
        return render_template("product_display.html", products=data)

    product_id = int(product_id)
    product = None

    for p in data:
        if "id" in p and int(p["id"]) == product_id:
            product = p
            break

    if product is None:
        return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=[product])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
