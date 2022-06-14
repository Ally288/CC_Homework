from app import app
from flask import render_template
from models.Order_List import orders


@app.route("/")
def customer_orders():
    return render_template("index.html", title="Order Page", orders=orders)

@app.route("/indexorders"):
def index_orders(index):
    chosen_order = orders[int(index)]
    return remder_template('order.html', order=chosen_order)