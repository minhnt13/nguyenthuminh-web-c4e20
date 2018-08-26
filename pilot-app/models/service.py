from mongoengine import *
# Re-Design Database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = IntField()
    image = StringField()
    measurements = ListField()
    descriptions = ListField()
