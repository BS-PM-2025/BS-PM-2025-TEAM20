# accounts/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views  # ייבוא ה-views מתוך האפליקציה הנוכחית
from accounts.views import home_view, student_profile_view, update_profile, update_student_profile
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import views as auth_views
#from .views import profile_view
urlpatterns = [




 path('signup/', views.signup_view, name='signup'),

    path('signup_student/', views.signup_student, name='signup_student'),
    path('update-profile/', update_profile, name='update_profile'),
    path('api/update-profile/', update_student_profile, name='api_update_profile'),
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
path('signup_sec/', views.signup_lec, name='signup_sec'),
    path('profile/', views.student_profile, name='student_profile'),
    path('profile/edit/', views.student_profile, name='edit_student_profile'),
path('update_profile/', views.update_student_profile, name='update_student_profile'),


    path('profile/edit/', views.student_profile, {'edit': True}, name='student_profile_edit'),  # נתיב לעריכת פרופיל
    path('request_success/', views.request_success, name='request_success'),

    path('login/student/', views.login_student, name='login_student'),
    path('login/lecturer/', views.login_lec, name='login_lec'),
    path('student/', views.student_page, name='student_page'),
   path('sec_page/', views.sec_page, name='sec_page'),
    path('lec_page/', views.lec_page, name='lec_page'),
path('lecc_page/', views.lecc_page, name='lecc_page'),
    path('', views.home_view, name='home'),
    path('office_hours/', views.office_hours_list, name='office_hours_list'),
    path('add/', views.add_office_hours, name='add_office_hours'),
    path('show/', views.show_office_hours, name='show_office_hours'),
    path('request/', views.request_grade_improvement, name='request_grade_improvement'),
    path('request_success/', views.success_view, name='success'),
    path('my-requests/', views.student_requests, name='student_requests'),
    path('student/request_form/', views.request_form, name='request_form'),
    path('request_list/', views.request_list, name='request_list'),

    path('password-reset/', views.send_password_reset_email, name='password_reset'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
path('password-reset/', views.send_password_reset_email, name='password_reset'),
    path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('create-profile/', views.create_student_profile, name='create_student_profile'),
path('profile/', views.student_profile, name='profile'),
path('profile/', views.student_profile, name='profile'),
    path('update-profile/', views.update_student_profile, name='update_profile'),  # הוספת אפשרות עדכון
    path('create-profile/', views.create_student_profile, name='create_student_profile'),
path('update_profile/', views.update_student_profile, name='update_profile'),




    ]