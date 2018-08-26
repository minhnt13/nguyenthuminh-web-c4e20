from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search")
def search_all():
    all_service = Service.objects()
    return render_template(
        "search.html",
        all_service = all_service)

@app.route("/search/<g>")
def search(g):
    all_service = Service.objects(
        gender=g,
        yob__lte=1998,
        height__gte=165
        )
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

@app.route("/admin")
def admin():
    all_service = Service.objects()
    return render_template(
        "admin.html",
        all_service=all_service
    )

@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_del = Service.objects.with_id(service_id)
    if service_to_del is not None:
        service_to_del.delete()
        return redirect(url_for("admin"))
    else:
        return "Service is not found"

@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        return render_template(
            "detail.html", 
            service=service)
    else:
        return "Service is not found"


@app.route("/new-service", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        gender = form["gender"]

        new_service = Service(
            name=name,
            yob=yob,
            phone=phone,
            gender =gender
        )

        new_service.save()
        return redirect(url_for("admin"))

@app.route("/update-service/<service_id>", methods=["GET","POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template("update.html", service=service)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form["gender"]
        height = form["height"]
        phone = form['phone']
        address = form["address"]

        if gender == "Nam":
            service.gender = 1
        elif gender == "Nữ":
            service.gender = 0
        service.name = name
        service.yob = yob
        service.phone = phone
        service.address = address
            
        service.save()
        
        return redirect(url_for("admin"))

if __name__ == '__main__':
  app.run(debug=True)
 