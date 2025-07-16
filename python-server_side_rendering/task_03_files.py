from flask import Flask, render_template, request
import json
import csv

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
        try:
            products = read_json("products.json")
        except Exception as e:
            return render_template("product_display.html", error="Error reading JSON file.")
    elif source == "csv":
        try:
            products = read_csv("products.csv")
        except Exception as e:
            return render_template("product_display.html", error="Error reading CSV file.")
    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id is not None:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
