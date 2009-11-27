from appengine_django.auth.models import User
from appengine_django.models import BaseModel
from google.appengine.ext import db

# Create your models here.
# Movie info
class Movie(BaseModel):
    title = db.StringProperty()
    subTitle = db.StringProperty()
    releaseDate = db.DateProperty()
    director = db.StringProperty()
    imdbLink = db.LinkProperty()
    officalSummary = db.TextProperty()

# Review info   
class Review(BaseModel):
    title = db.StringProperty()
    createDate = db.DateTimeProperty(auto_now_add=True)
    summary = db.TextProperty()
    movie = db.ReferenceProperty(Movie)
    user = db.ReferenceProperty(User)

# Review rankings
class Ranking(BaseModel):
    rating = db.FloatProperty()
    ratingType = db.StringProperty()
    movie = db.ReferenceProperty(Movie)
    user = db.ReferenceProperty(User)

# Site News
class News(BaseModel):
    createDate = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    summary = db.TextProperty()
    user = db.ReferenceProperty(User)