import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds125872.mlab.com:25872/muadongkhonglanh

host = "ds125872.mlab.com"
port = 25872
db_name = "muadongkhonglanh"
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

