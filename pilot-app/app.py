from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
import datetime
from gmail import GMail, Message

app = Flask(__name__)
app.secret_key = "a secret string"
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

@app.route('/sign-in', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('sign-in.html')
    elif request.method == "POST":
        form = request.form
        fullname = form["fullname"]
        email = form["email"]
        username = form["username"]
        password = form["password"]

        new_user = User(
            username=username,
            password=password,
            email=email,
            fullname=fullname
        )

        new_user.save()
        return redirect(url_for("index"))

@app.route("/detail/<service_id>")
def detail(service_id):
    service = Service.objects.with_id(service_id)
    session["service"]=str(service.id)
    if "loggedin" in session:
        if session["loggedin"] == True:
            if service is not None:
                return render_template(
                    "detail.html", 
                    service=service)
            else:
                return "Service is not found"
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        found_user = User.objects(
            username=username,
            password=password
        )
        if found_user:
            session["loggedin"] = True
            user = User.objects.get(username=username)
            session["user"] = str(user.id)
            service_id = session["service"]
            return redirect(url_for("detail", service_id=service_id))
        else:
            return redirect(url_for("signin"))

@app.route('/logout')
def logout():
    session["loggedin"]=False
    session.clear()
    return redirect(url_for("index"))

@app.route("/ordered") #create new order
def ordered():
    if "loggedin" in session:
        if session["loggedin"] == True:
            user = session["user"]
            service = session["service"]
            new_order = Order(
                user=user,
                service=service,
                order_time=datetime.datetime.now(),
                is_accepted = False
            )
            new_order.save()
            return "Đã gửi yêu cầu"
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@app.route("/order")
def order():
    orders = Order.objects()
    return render_template('order.html',orders=orders)

@app.route("/accepted/<order_id>")
def accepted(order_id):
    order = Order.objects.with_id(order_id)
    email = order.user.email
    # update field
    order.update(
        is_accepted = True
    )
    # send email
    gmail = GMail("Minh<minhnt13@gmail.com>","someknownow")
    msg = Message(
    "Xét duyệt yêu cầu - Mùa Đông Không Lạnh",
    to=email,
    text="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’")
    gmail.send(msg)

    return redirect(url_for("order"))

if __name__ == '__main__':
  app.run(debug=True)
 