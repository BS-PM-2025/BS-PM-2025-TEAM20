"""
URL configuration for djangoProject11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# djangoProject11/urls.py
from accounts.views import home_view
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from accounts import views  # ייבוא ה-views מתוך האפליקציה 'accounts'
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),  # נתיב לממשק הניהול
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('', home_view, name='home'),# נתיב לדף ההרשמה

   path('accounts/', include('accounts.urls')),

    path('', lambda request: render(request, 'home.html'), name='home'),

    path('admin/', admin.site.urls),  # נתיב לממשק ניהול
    path('signup/', views.signup_view, name='signup'),  # נתיב להרשמה (האם יש צורך בו?)
    path('home/', views.home_view, name='home'),  # נתיב לדף הבית
    path('', home_view, name='home'),  # נתיב לברירת מחדל (דף הבית)
    path('accounts/', include('accounts.urls')),
    path('signup_student/', views.signup_student, name='signup_student'),
 path('signup_lec/', views.signup_student, name='signup_lec'),
path('signup_sec/', views.signup_sec, name='signup_sec'),
path('signup_lecc/', views.signup_lecc, name='signup_lecc'),
    path('student_requests/', views.student_requests, name='student_requests'),  # הנתיב לדף student_requests
    path('student/request_form/', views.request_form, name='request_form'),
    path('request_success/', views.success_view, name='success'),
    path('request_list/', views.request_list, name='request_list'),

]
