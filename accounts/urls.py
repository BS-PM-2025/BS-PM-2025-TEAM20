# accounts/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views  # ייבוא ה-views מתוך האפליקציה הנוכחית
from accounts.views import home_view
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [




 path('signup/', views.signup_view, name='signup'),

    path('signup_student/', views.signup_student, name='signup_student'),

    path('', home_view, name='home'),# נתיב לדף ההרשמה
    path('login/', views.login_view, name='login'),
    path('login_lec/', views.login_lec, name='login_lec'),
    path('signup_lecc/', views.signup_lecc, name='signup_lecc'),
path('signup_lecc/', views.signup_lecc, name='signup_lecc'),
path('login_lecc/', views.login_lecc, name='login_lecc'),
path('login_sec/', views.login_sec, name='login_sec'),
    path('signup/', views.signup_view, name='signup'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('signup_lec/', views.signup_lec, name='signup_lec'),
path('signup_sec/', views.signup_sec, name='signup_sec'),
    path('login/student/', views.login_student, name='login_student'),
    path('login/lecturer/', views.login_lec, name='login_lec'),
    path('student/', views.student_page, name='student_page'),
   path('sec_page/', views.sec_page, name='sec_page'),
    path('lec_page/', views.lec_page, name='lec_page'),
path('lecc_page/', views.lecc_page, name='lecc_page'),
    path('', views.home_view, name='home'),

    path('request/', views.request_grade_improvement, name='request_grade_improvement'),
    path('request_success/', views.success_view, name='success'),
    path('my-requests/', views.student_requests, name='student_requests'),
    path('student/request_form/', views.request_form, name='request_form'),
    path('request_list/', views.request_list, name='request_list'),
]