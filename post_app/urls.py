
from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
  path('',PostLists.as_view(),name='page-list'),
  path('post/<str:slug>/',PostDetails.as_view(),name='page-detail'),   
  path('login/',LoginView.as_view(),name='login-view'),
  path('register/',RegisterUser.as_view(),name='register-view'),  
  path('create-post/',CreatePost.as_view(),name='create-post'),  
]
