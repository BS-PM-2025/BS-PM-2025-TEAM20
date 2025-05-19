from django.contrib import admin
from .models import UserRegister, LoginLog, OfficeHours11, GradeImprovementRequest, UserRegisterLec, UserRegisterStu1, \
    LoginHistory

# רישום המודלים לממשק האדמין
admin.site.register(UserRegister)
admin.site.register(LoginLog)
admin.site.register(OfficeHours11)
admin.site.register(UserRegisterLec)
# רישום UserRegisterLec
admin.site.register(LoginHistory)

# רישום GradeImprovementRequest עם אפשרויות מותאמות אישית
@admin.register(GradeImprovementRequest)
class GradeImprovementRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_name', 'current_grade', 'desired_grade', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('student__username', 'course_name')



from django.contrib import admin
from .models import StudentLoginHistory

admin.site.register(StudentLoginHistory)


from django.contrib import admin
from .models import OfficeHour, Appointment

from django.contrib import admin
from .models import OfficeHour, Appointment

admin.site.register(OfficeHour)
admin.site.register(Appointment)


# admin.py
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message', 'timestamp')
    list_filter = ('sender',)
    search_fields = ('sender', 'message')
    ordering = ('timestamp',)


from django.contrib import admin
from .models import ChatbotQuestion, ChatbotConversation

admin.site.register(ChatbotQuestion)
admin.site.register(ChatbotConversation)
from django.contrib import admin
from .models import ChatHistory
from django.contrib import admin
from .models import MessageHistory

admin.site.register(MessageHistory)

admin.site.register(ChatHistory)


# admin.py
from django.contrib import admin
from .models import TimeExtensionRequest

# רישום המודל ב-Django Admin
admin.site.register(TimeExtensionRequest)




from django.contrib import admin
from .models import MeetingRequest

class MeetingRequestAdmin(admin.ModelAdmin):
    list_display = ('student_email', 'meeting_date', 'meeting_time', 'status')
    list_filter = ('status', 'meeting_date')
    search_fields = ('student_email',)

admin.site.register(MeetingRequest, MeetingRequestAdmin)


from django.contrib import admin
from .models import Lecturer, Meeting

admin.site.register(Lecturer)
admin.site.register(Meeting)



from django.contrib import admin
from .models import StudentRequest

@admin.register(StudentRequest)
class StudentRequestAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_email', 'professor_email', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('student_name', 'student_email', 'professor_email', 'request_type')
    readonly_fields = ('created_at',)



from django.contrib import admin
from .models import DocumentRequest

@admin.register(DocumentRequest)
class DocumentRequestAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_email', 'document_type', 'is_completed', 'created_at')
    list_filter = ('document_type', 'is_completed', 'created_at')



from django.contrib import admin
from .models import ScheduleSlot, Booking

admin.site.register(ScheduleSlot)
admin.site.register(Booking)


from django.contrib import admin
from .models import StudentProfile

admin.site.register(StudentProfile)

from django.contrib import admin
from .models import StuProf

admin.site.register(StuProf)