# Create your views here.
from django.shortcuts import render_to_response
from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from jivemonkey import models

class NewsForm(djangoforms.ModelForm):
    class Meta:
        model = models.News

def add(request):
    form = NewsForm(request.POST)
    if not form.is_valid():
        return render_to_response('news/edit.html',
                                  {'action':'add',
                                   'form': form})

    news = form.save(commit=False)
    news.put()
    return list(request)

def update(request, news_id):
    news = db.get(news_id)
    form = NewsForm(data=request.POST, instance=news)

    if not form.is_valid():
        return render_to_response('news/edit.html',
                                  {'action':'update',
                                   'form': form})
    
    news = form.save(commit=False)
    news.put()
    return list(request)

def list(request):
    query = models.News.all()
    return render_to_response('news/list.html',
                              {'news': query.run()})

def delete(request, news_id):
    db.get(news_id).delete()
    return list(request)

def create(request):
    form = NewsForm()
    return render_to_response('news/edit.html',
                              {'action':'add',
                               'form': form})

def edit(request, news_id):
    news = db.get(news_id)
    form = NewsForm(instance=news)
    return render_to_response('news/edit.html',
                              {'action':'update',
                               'id':news_id,
                               'form': form})

def detail(request, news_id):
    news = db.get(news_id)

    query = db.GqlQuery("select * from Review where news= :1", news)

    return render_to_response('news/detail.html',
                              {'reviews': query.run(),
                               'news': news})