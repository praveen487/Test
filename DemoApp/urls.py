from django.urls import path
from DemoApp import views

urlpatterns = [

    path('',views.indexview,name='index'),

]
