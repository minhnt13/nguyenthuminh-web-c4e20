from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search/<g>")
def search(g):
    all_service = Service.objects(gender=g)
    return render_template(
        "search.html",
        all_service=all_service
        )

@app.route("/customer")
def customer():
    all_customer = Customer.objects()
    return render_template(
        "customer.html",
        all_customer=all_customer
    )

@app.route("/customer/male/contacted")
def ten_first_male():
    ten_first_male = Customer.objects[:10](
        gender = 1,
        contacted = False
    )
    return render_template(
        "customer.html",
        all_customer=ten_first_male
    )


if __name__ == '__main__':
  app.run(debug=True)
 