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
from accounts.views import home_view, update_profile, update_student_profile
# , profile_view
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from accounts import views  # ייבוא ה-views מתוך האפליקציה 'accounts'
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # נתיב לממשק הניהול
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('', home_view, name='home'),# נתיב לדף ההרשמה

                  path('request_success/', views.request_success, name='request_success'),

                  path('update-profile/', update_profile, name='update_profile'),
                  path('api/update-profile/', update_student_profile, name='api_update_profile'),

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
    path('profile/', views.student_profile, name='student_profile'),
    path('office_hours/', views.office_hours_list, name='office_hours_list'),
    path('add/', views.add_office_hours, name='add_office_hours'),
  path('profile/edit/', views.student_profile, {'edit': True}, name='edit_student_profile'),
    path('profile/edit/', views.student_profile, {'edit': True}, name='student_profile_edit'),  # נתיב לעריכת פרופיל
path('update_profile/', views.update_student_profile, name='update_student_profile'),
                  path('password-reset/', views.send_password_reset_email, name='password_reset'),
                  path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

path('password-reset/', views.send_password_reset_email, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

                  path('create-profile/', views.create_student_profile, name='create_student_profile'),
path('profile/', views.student_profile, name='profile'),

path('profile/', views.student_profile, name='profile'),
    path('update-profile/', views.update_student_profile, name='update_profile'),  # הוספת אפשרות עדכון
    path('create-profile/', views.create_student_profile, name='create_student_profile'),
path('update_profile/', views.update_student_profile, name='update_profile'),



                  path('password_reset_done/', views.password_reset_done, name='password_reset_done'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
