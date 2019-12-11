from django.db.models import *


# Create your models here.

class Project(Model):
    title = CharField(max_length=100)
    description = TextField()
    technology = CharField(max_length=20)
    image = FilePathField(path='/img')
