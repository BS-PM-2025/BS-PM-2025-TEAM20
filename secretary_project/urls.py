from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ضروري علشان يعمل redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # إعادة توجيه مباشرة إلى login
    path('admin/', admin.site.urls),
    path('accounts/', include('secretary_app.urls')),  # روابط تسجيل الدخول والتسجيل
]
