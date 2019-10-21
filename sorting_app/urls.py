from django.urls import path
from . import views

app_name = 'sorting_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('summary', views.summary, name='summary')
]
