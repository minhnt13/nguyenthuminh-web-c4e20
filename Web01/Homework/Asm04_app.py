from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def users(username):
    users = {
        "minh" : {
                "name": "Nguyen Minh",
                "age": 25,
                "gender": "female",
                "hobbies": "stare into the void"
            },
        "cat" : {
                "name": "Con cho 1",
                "age": 3,
                "gender": "neutered",
                "hobbies": "slap the dog, being a dick"
            },
        "dog" : {
                "name": "Con cho 2",
                "age": 1.5,
                "gender": "neutered",
                "hobbies": "bark at the cat, get slapped"
            }
        }
    if username in users:
        return render_template('users.html',username=users[username])
    else:
        return "User not found"

if __name__ == '__main__':
  app.run(debug=True)
 