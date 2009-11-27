# Create your views here.
from django.shortcuts import render_to_response
from google.appengine.ext import db

from jivemonkey import models

def index(request):
    query = models.News.all()
    return render_to_response('index.html',
                              {'user':request.user,'news': query.run()})