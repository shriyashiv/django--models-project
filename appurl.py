from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home),
    path('Bookflight/',views.index),
    path('Aboutus/',views.value),


]
