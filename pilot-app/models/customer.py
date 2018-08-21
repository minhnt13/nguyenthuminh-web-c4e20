from mongoengine import *
class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    adress = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()