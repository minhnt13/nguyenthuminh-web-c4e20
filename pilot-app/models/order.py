from mongoengine import *
import datetime

class Order(Document):
    user=ReferenceField("User")
    service=ReferenceField("Service")
    order_time=DateTimeField(default=datetime.datetime.utcnow)
    is_accepted=BooleanField()