from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('demo/', views.demo, name='demo'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar, name='calendar'),
    path('contact/',views.contact, name='contact'),
    # path('index/', views.index, name='index'),
    # path('test/oneproject', views.oneProject, name='one'),
    # path('add/', views.add, name='add'),
    # path('copy/', views.copy, name='copy'),
    #path('demo/submit/<list_id>', views.submit, name='submit'),
]
