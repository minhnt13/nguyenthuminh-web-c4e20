from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/about-me')
def about_me():
    return render_template("about_me.html")

@app.route('/school')
def school_redirect():
    return redirect("http://techkids.vn")
    
if __name__ == '__main__':
  app.run(debug=True)
 
