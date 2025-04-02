from django.contrib import admin
from .models import UserData

admin.site.register(UserData)

from django.contrib import admin
from .models import GradeImprovementRequest

@admin.register(GradeImprovementRequest)
class GradeImprovementRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_name', 'current_grade', 'desired_grade', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('student__username', 'course_name')
