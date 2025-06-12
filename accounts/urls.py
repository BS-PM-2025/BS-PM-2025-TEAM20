# accounts/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views  # ייבוא ה-views מתוך האפליקציה הנוכחית
from accounts.views import home_view, manage_my_profile
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import views as auth_views
#from .views import profile_view
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
path('signup_sec/', views.signup_lec, name='signup_sec'),



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



    path('feedback/', views.feedback_page, name='feedback_page'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('chatroom1/', views.chatroom, name='chatroom1'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('send_message/', views.send_message, name='send_message'),
    path('request_for_form/', views.request_for_form, name='request_for_form'),
    path('form_requests/', views.form_requests, name='form_requests'),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('form_list/', views.form_list, name='form_list'),
 path('update_office_hour/<int:id>/', views.update_office_hour, name='update_office_hour'),
    path('submit_extension_request/', views.submit_extension_request, name='submit_extension_request'),
    path('request_success/', views.request_success, name='request_success'),
path('request_time_extension/', views.submit_time_extension_request, name='request_time_extension'),
    path('requests/', views.extension_request_list, name='request_list'),
    path('last-requests/', views.last_student_requests, name='last_student_requests'),

    path('schedule/', views.schedule_meeting, name='schedule_meeting'),
    path('lecturer/add_or_update/', views.add_or_update_lecturer, name='add_or_update_lecturer'),
    path('lecturer/profile/', views.lecturer_profile, name='lecturer_profile'),

    path('lecturer/<int:lecturer_id>/schedule/', views.schedule_meeting, name='schedule_meeting'),
path('office-hours/', views.office_hours_list, name='office_hours_list'),
    path('book/<int:pk>/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.my_appointments, name='my_appointments'),
    path('create-slots/', views.create_slots, name='create_slots'),
    path('book_appointment/<int:pk>/', views.book_appointment, name='book_appointment'),
path('available_hours/', views.available_office_hours, name='available_hours'),
path('confirm_appointment/<int:pk>/', views.confirm_appointment, name='confirm_appointment'),
    path('available_hours/', views.student_available_hours, name='student_available_hours'),
    path('student-secretary-chat/', views.student_secretary_chat_view, name='student_secretary_chat'),
    path('get_messages_sec/', views.get_messages_sec, name='get_messages_sec'),
    path('send_message_sec/', views.send_message_sec, name='send_message_sec'),
    path('submit-request/', views.submit_request_view, name='submit_request'),
    path('requests/', views.professor_requests_view, name='professor_requests'),
    path('request/<int:request_id>/respond/', views.respond_request_view, name='respond_request'),

path('student_request/', views.submit_request_view, name='submit_request'),
    path('all-feedbacks/', views.all_feedbacks_view, name='all_feedbacks'),
    path('submit_document_request/', views.submit_document_request, name='submit_document_request'),
    path('secretary_requests/', views.secretary_requests_view, name='secretary_requests'),
    path('upload_document/<int:request_id>/', views.upload_document_view, name='upload_document'),
    path('lecturer/create/', views.lecturer_create_slot, name='lecturer_create'),
    path('student/', views.student_view_slots, name='student_view'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('cancel/<int:slot_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/edit/', views.student_profile, name='update_profile'),
    path('profile/', views.student_profile, name='student_profile'),

    path('my-profile/', manage_my_profile, name='my_profile'),
    path('lecturer_rec/', views.lecturer_reception_hours, name='lecturer_reception_hours'),
    path('student_rec/', views.student_reception_hours, name='student_reception_hours'),
    path('student/book/<int:reception_hour_id>/', views.book_reception_hour, name='book_reception_hour'),
    path('student/cancel/<int:booking_id>/', views.cancel_reception_booking, name='cancel_reception_booking'),
    path('add1/', views.add1_consul, name='add1_consul'),
    path('student/list/', views.consul_list, name='consul_list'),
# urls.py
path('document_request/<int:request_id>/', views.document_request_detail, name='document_request_detail'),


]