# Create your views here.
from django.shortcuts import render_to_response
from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from jivemonkey import models

class MovieForm(djangoforms.ModelForm):
    class Meta:
        model = models.Movie

def add(request):
    form = MovieForm(request.POST)
    if not form.is_valid():
        return render_to_response('movie/edit.html',
                                  {'action':'add',
                                   'form': form})

    #movie = form.save(commit=False)
    form.save()
    #models.Movie.
    #movie.save()
    return list(request)

def update(request, movie_id):
    movie = db.get(movie_id)
    form = MovieForm(data=request.POST, instance=movie)

    if not form.is_valid():
        return render_to_response('movie/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    movie = form.save(commit=False)
    movie.put()
    return list(request)

def list(request):
    query = models.Movie.all()
    return render_to_response('movie/list.html',
                              {'user':request.user,'movies': query.run(),
                               'form': MovieForm()})

def delete(request, movie_id):
    db.get(movie_id).delete()
    return list(request)

def create(request):
    form = MovieForm()
    return render_to_response('movie/edit.html',
                              {'action':'add',
                               'form': form})

def edit(request, movie_id):
    movie = db.get(movie_id)
    form = MovieForm(instance=movie)
    return render_to_response('movie/edit.html',
                              {'action':'update',
                               'id':movie_id,
                               'form': form})

def detail(request, movie_id):
    movie = db.get(movie_id)

    query = db.GqlQuery("select * from Review where movie= :1", movie)

    return render_to_response('movie/detail.html',
                              {'reviews': query.run(),
                               'movie': movie})

def index(request):
    return render_to_response('movie/list.html',
                              {'movies': query.run(),
                               'form': MovieForm()})