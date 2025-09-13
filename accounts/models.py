from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




from django.contrib.auth.models import User
from django.db import models
class GradeImprovementRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=100, null=True)
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



class LoginLog(models.Model):
    username = models.CharField(max_length=150)
    login_time = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=100)  # לדוגמה: 'views.py'

    def __str__(self):
        return f"{self.username} - {self.login_time} - {self.file}"


class UserRegister(models.Model):
    # עמודות לטבלת משתמשים
    username = models.CharField(max_length=100, unique=True)  # אם ברצונך למנוע כפילויות בשמות משתמשים
    email = models.EmailField(unique=True)  # אם ברצונך למנוע כפילויות בדוא"ל
    password = models.CharField(max_length=255)  # הסיסמה תשמר כטקסט מוצפן
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Model to store lecturer registration information
class UserRegisterLec(models.Model):
    # Username field - must be unique (no duplicate usernames)
    username = models.CharField(max_length=100, unique=True)

    # Email field - must be unique (no duplicate emails)
    email = models.EmailField(unique=True)

    # Password field - stored as plain text for now (should be encrypted ideally)
    password = models.CharField(max_length=255)

    # First name of the lecturer
    first_name = models.CharField(max_length=100)

    # Last name of the lecturer
    last_name = models.CharField(max_length=100)

    # String representation of the lecturer (shows username)
    def __str__(self):
        return self.username


# Required Django imports
from django.db import models
from django.contrib.auth.models import User  # Importing Django's built-in User model (optional if needed)
from django.contrib.auth.hashers import make_password  # For encrypting passwords if used
from django.utils import timezone  # For handling time fields if needed


class UserRegisterStu1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=timezone.now)  # הוספת שדה last_login

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def update_last_login(self):
        self.last_login = timezone.now()  # עדכון הזמן הנוכחי
        self.save()
    def get_email_field_name(self):
        return 'email'
class StudentLoginHistory(models.Model):
    username = models.CharField(max_length=100)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} - {self.login_time}"



from django.db import models


class OfficeHours(models.Model):
    # שם הסניף/המשרד
    office_name = models.CharField(max_length=100)

    # שעות הקבלה
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    # פרטים נוספים (לדוגמה, מה צריך להביא)
    additional_info = models.TextField()

    def __str__(self):
        return f"{self.office_name} - {self.opening_time} to {self.closing_time}"



from django.db import models


class OfficeHours11(models.Model):
    # שם הסניף/המשרד
    office_name = models.CharField(max_length=100)

    # שעות הקבלה
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    # פרטים נוספים (לדוגמה, מה צריך להביא)
    additional_info = models.TextField()

    def __str__(self):
        return f"{self.office_name} - {self.opening_time} to {self.closing_time}"




from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserRegisterStu1  # ודא שזה הנתיב הנכון למודל

class StudentProfile(models.Model):
    student = models.OneToOneField(UserRegisterStu1, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='student_images/', null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)  # השדה החדש


    def __str__(self):
        return f"{self.student.username}'s Profile"




from django.db import models
from django.contrib.auth.models import User

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    # משתמש המחובר
    login_time = models.DateTimeField(auto_now_add=True)  # תאריך ושעה של התחברות
    success = models.BooleanField(default=True)  # הצלחה או כישלון בהתחברות
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # כתובת IP של המשתמש (אם תרצה)

    def __str__(self):
        return f'{self.user.username} - {self.login_time} - Success: {self.success}'





from django.db import models
from django.utils import timezone

class StudentLoginHistory(models.Model):
    username = models.CharField(max_length=100)
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username} - {self.login_time}"
