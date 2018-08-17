from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"
# without render_template()
@app.route('/bmi/<int:weight>/<int:height_cm>')
def calc_bmi(weight, height_cm):
    height_m = height_cm/100
    bmi = weight/height_m**2
    if bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# with render_template()
@app.route('/bmi/<int:weight>/<int:height_cm>')
def calc_bmi(weight, height_cm):
    height_m = height_cm/100
    bmi = weight/height_m**2
    return render_template("bmi.html", bmi=bmi)

if __name__ == '__main__':
  app.run(debug=True)
 