# Create your views here.
from appengine_django.auth.models import User

from django.shortcuts import render_to_response
from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from jivemonkey import models

class ReviewForm(djangoforms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ['movie','user']

def add(request):
    form = ReviewForm(request.POST)
    if not form.is_valid():
        return render_to_response('review/edit.html',
                                  {'action':'add',
                                   'form': form})

    review = form.save(commit=False)
    review.movie = db.get(request.POST['movie_id'])
    if not request.user.is_anonymous() and request.user.is_authenticated():
        review.user = request.user
    review.put()
    return HttpResponseRedirect('/movie/detail/%s'%request.POST['movie_id'])

def update(request, review_id):
    review = db.get(review_id)
    form = ReviewForm(data=request.POST, instance=review)

    if not form.is_valid():
        return render_to_response('review/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    review = form.save(commit=False)

    if not request.user.is_anonymous() and request.user.is_authenticated():
        review.user = request.user

    review.put()
    return HttpResponseRedirect('/movie/detail/%s' % review.movie.key())

def list(request):
    query = models.Review.all()
    return render_to_response('review/list.html',
                              {'reviews': query.run(),
                               'form': ReviewForm()})

def delete(request, review_id):
    review = db.get(review_id)
    movie_id = review.movie.key()
    review.delete()
    return HttpResponseRedirect('/movie/detail/%s'%movie_id)

def create(request, movie_id):
    form = ReviewForm()
    return render_to_response('review/edit.html',
                              {'action':'add',
                               'movie_id':movie_id,
                               'form': form})

def edit(request, review_id):
    review = db.get(review_id)
    form = ReviewForm(instance=review)
    return render_to_response('review/edit.html',
                              {'action':'update',
                               'id':review_id,
                               'form': form})

def detail(request, review_id):
    review = db.get(review_id)
    return render_to_response('review/detail.html',
                              {'review': review})

def index(request):
    return render_to_response('review/list.html',
                              {'reviews': query.run(),
                               'form': ReviewForm()})