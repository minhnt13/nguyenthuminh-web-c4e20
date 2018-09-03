from mongoengine import *
class Video(Document):
    title=StringField()
    link=StringField()
    views=IntField()
    thumbnail=StringField()
    youtube_id=StringField()
