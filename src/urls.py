# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns

urlpatterns = patterns('controllers',
    # Main page
    (r'^$','home.index'),
    # News Actions
    (r'^news/list/$','news.list'),
    (r'^news/edit/(?P<news_id>\w+)/$','news.edit'),
    (r'^news/add/$','news.add'),
    (r'^news/update/(?P<news_id>\w+)$','news.update'),
    (r'^news/create/$','news.create'),
    (r'^news/delete/(?P<news_id>\w+)/$','news.delete'),
    # User Actions
    (r'^user/list/$','user.list'),
    (r'^user/edit/(?P<user_id>\w+)/$','user.edit'),
    (r'^user/detail/(?P<user_id>\w+)/$','user.detail'),
    (r'^user/add/$','user.add'),
    (r'^user/create/$','user.create'),
    (r'^user/delete/(?P<user_id>\w+)/$','user.delete'),
)

urlpatterns += patterns('',
    # Django User Actions
    (r'^user/login/$', 'django.contrib.auth.views.login', {'template_name': 'user/login.html'}),
    (r'^user/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
