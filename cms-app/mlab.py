import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds031822.mlab.com:31822/cms

host = "ds031822.mlab.com"
port = 31822
db_name = "cms"
user_name = "admin"
password = "1inalifetime"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password
        )