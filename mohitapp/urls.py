
from django.urls import path

from mohitapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('nott',views.nott,name='nott'),
    path('project',views.proj,name='proj'),
    path('ende',views.ende,name='ende')
    
]
