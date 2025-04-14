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


