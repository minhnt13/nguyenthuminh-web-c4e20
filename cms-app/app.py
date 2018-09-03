from flask import *
import mlab
from models.video import Video
from youtube_dl import YoutubeDL
app = Flask(__name__)
mlab.connect()
# session require a secret key
app.secret_key = "a super secret key"

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos=videos)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        if username == "admin" and password == "admin":
            session["loggedin"]=True
            return redirect(url_for("admin"))
        else:
            return "Đi chỗ khác đê"
            
@app.route("/logout")
def logout():
    session["loggedin"]=False
    return redirect(url_for("index"))

@app.route('/admin', methods=["GET","POST"])
def admin():
    if "loggedin" in session:
        if session["loggedin"]==True:
            if request.method == "GET":
                videos = Video.objects()
                return render_template('admin.html', videos=videos)
            elif request.method == "POST":
                form = request.form
                link = form["link"]
                ydl = YoutubeDL()
                data = ydl.extract_info(link, download=False)
                title = data["title"]
                thumbnail = data["thumbnail"]
                views = data["view_count"]
                youtube_id = data["id"]

                new_video = Video(
                    title=title,
                    link=link,
                    thumbnail=thumbnail,
                    views=views,
                    youtube_id=youtube_id
                )

                new_video.save()
                return redirect(url_for("admin"))
        else:
            return "Yêu cầu đăng nhập"
    else:
        return "Đi chỗ khác chơi"

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id=youtube_id)

if __name__ == '__main__':
  app.run(debug=True)
