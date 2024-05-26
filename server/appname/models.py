from mongoengine import Document, StringField


class User(Document):
    username = StringField(max_length=50)
    password = StringField(max_length=50)
