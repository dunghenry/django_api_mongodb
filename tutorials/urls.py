from django.urls import re_path as url
from django.urls import path, include
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list, name='tutorial_list'),
    # path('/tutorials', views.tutorial_list, name='tutorial_list'),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]