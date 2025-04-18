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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # الصفحة الرئيسية
    path('', views.home_view, name='home'),

    # تسجيل

    path('signup/', views.signup_view, name='signup'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('signup_lec/', views.signup_lec, name='signup_lec'),
    path('signup_sec/', views.signup_sec, name='signup_sec'),
    path('signup_lecc/', views.signup_lecc, name='signup_lecc'),
    path('update-profile/', views.update_student_profile, name='update_profile'),


    # تسجيل دخول
    path('accounts/', include('accounts.urls')),

    # الطالب
    path('student_requests/', views.student_requests, name='student_requests'),
    path('student/request_form/', views.request_form, name='request_form'),
    path('request_success/', views.success_view, name='request_success'),

    # פרופיל סטודנט
    path('profile/', views.student_profile, name='student_profile'),
    path('profile/edit/', views.student_profile, {'edit': True}, name='edit_student_profile'),
    path('update-profile/', views.update_student_profile, name='update_profile'),
    path('create-profile/', views.create_student_profile, name='create_student_profile'),

    # ساعات קבלה
    path('office_hours/', views.office_hours_list, name='office_hours_list'),
    path('add/', views.add_office_hours, name='add_office_hours'),

    # שיפור ציון
    path('request_list/', views.request_list, name='request_list'),

    # איפוס סיסמה
    path('password-reset/', views.send_password_reset_email, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
