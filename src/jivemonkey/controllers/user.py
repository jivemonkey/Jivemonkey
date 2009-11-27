#User views
from django.shortcuts import render_to_response
from google.appengine.ext.db import djangoforms
from google.appengine.ext import db

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from appengine_django.auth.models import User

from django.contrib.auth.views import login

class UserForm(djangoforms.ModelForm):
    class Meta:
        model = User

def add(request):

    form = UserForm(request.POST)

    if not form.is_valid():
        return render_to_response('user/edit.html',
                                  {'action':'add','form': form})
    
    user = User.all().filter("username =", request.POST['username']).get()

    if user != None:
        form.errors['User Already Exists'] = "- A user with this username already exists"
        return render_to_response('user/edit.html',
                          {'action':'add','form': form})
        
    user = form.save(commit=False)
    user.set_password(user.password)
    user.save()

    return HttpResponseRedirect('/')

def list(request):
    query = User.all()
    return render_to_response('user/list.html',
                              {'users': query.run(),
                               'form': UserForm()})

def create(request):
    form = UserForm()
    return render_to_response('user/edit.html',
                              {'action':'add','form': form})

def edit(request, user_id):
    user = db.get(user_id)
    form = UserForm(instance=user)
    return render_to_response('user/edit.html',
                              {'action':'update',
                               'form': form})

def detail(request, user_id):
    user = db.get(user_id)

    return render_to_response('user/detail.html',
                              {'user': user})

def delete(request, user_id):
    db.get(user_id).delete()
    return HttpResponseRedirect('/')