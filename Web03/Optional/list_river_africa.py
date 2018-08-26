import mlab
from mongoengine import *
mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

river_in_africa = River.objects(continent__icontains = "Africa")

for index, river in enumerate(river_in_africa):
    print(index + 1, ".", river.name)
    