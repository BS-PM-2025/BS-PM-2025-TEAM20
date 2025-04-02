from django.db import models

class UserData(models.Model):
    # עמודות לטבלת משתמשים
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # הסיסמה תשמר כטקסט מוצפן
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return self.username


from django.db import models
from django.contrib.auth.models import User

class GradeImprovementRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    current_grade = models.IntegerField()
    desired_grade = models.IntegerField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course_name} ({self.status})"
