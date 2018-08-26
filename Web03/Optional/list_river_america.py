import mlab
from mongoengine import *
mlab.connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

river_in_america = River.objects(
    continent__icontains = "S. America",
    length__lt=1000
    )

for index, river in enumerate(river_in_america):
    print(index + 1, ".", river.name)
    