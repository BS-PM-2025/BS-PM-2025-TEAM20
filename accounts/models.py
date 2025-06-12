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

class UserRegisterLec(models.Model):
    # עמודות לטבלת משתמשים
    username = models.CharField(max_length=100, unique=True)  # אם ברצונך למנוע כפילויות בשמות משתמשים
    email = models.EmailField(unique=True)  # אם ברצונך למנוע כפילויות בדוא"ל
    password = models.CharField(max_length=255)  # הסיסמה תשמר כטקסט מוצפן
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import User  # Importing the User model
from django.contrib.auth.hashers import make_password

def get_last_user():
    return User.objects.last().id if User.objects.exists() else 1  # Or another default ID if no users exist
from django.utils import timezone

class UserRegisterStu1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_last_user)
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


# models.py
from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - Rating {self.rating}"




from django.db import models
from django.contrib.auth.models import User

class ChatbotQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text


class ChatbotConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(ChatbotQuestion, on_delete=models.CASCADE)
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation with {self.user.username} at {self.timestamp}"


# models.py
from django.db import models

class ChatHistory(models.Model):
    user_id = models.CharField(max_length=100)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.timestamp}"


from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=50)  # student or lecturer
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.timestamp}"


from django.db import models

class ChatMessagee(models.Model):
    SENDER_CHOICES = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
    ]

    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:30]}"






from django.db import models

class MessageHistory(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.timestamp}'


from django.db import models
from django.contrib.auth.models import User

class FormRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=200)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"{self.student.username} requested {self.form_name}"


class FormUpload(models.Model):
    form_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='forms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form_name



# models.py
from django.db import models
from django.db import models

class TimeExtensionRequest(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    subject = models.CharField(max_length=100)
    original_deadline = models.DateField()
    requested_extension_time = models.IntegerField()
    reason_for_extension = models.TextField()
    supporting_documents = models.FileField(upload_to='extensions/', null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'בהמתנה'), ('approved', 'מאושר'), ('rejected', 'נדחה')],
        default='pending'
    )

    def __str__(self):
        return f"{self.student_name} - {self.subject}"




from django.db import models

class MeetingRequest(models.Model):
    student_email = models.EmailField()
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'ממתין'), ('confirmed', 'מאושר'), ('rejected', 'נדחה')])

    def __str__(self):
        return f"פגישה עם {self.student_email} בתאריך {self.meeting_date} בשעה {self.meeting_time}"

# models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    office_hours = models.CharField(max_length=100, help_text="שעות קבלה של המרצה")
    email = models.EmailField(help_text="מייל המרצה")
    specialization = models.CharField(max_length=100, help_text="התמחות המרצה")

    def __str__(self):
        return self.name


class Meeting(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    date = models.DateTimeField(help_text="תאריך ושעה לפגישה", default=datetime.now)  # הוספת ערך ברירת מחדל
    confirmed = models.BooleanField(default=False, help_text="אם הפגישה אושרה")

    def __str__(self):
        return f"פגישה עם {self.lecturer.name} בתאריך {self.date}"




from django.db import models
from django.contrib.auth.models import User

class OfficeHour(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.lecturer.username} - {self.day} {self.start_time}-{self.end_time}"

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    office_hour = models.ForeignKey(OfficeHour, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} -> {self.office_hour}"


from django.db import models
from django.utils import timezone

from django.db import models

class ChatMessageSec(models.Model):
    SENDER_CHOICES = (
        ('student', 'Student'),
        ('secretary', 'Secretary'),
    )
    sender = models.CharField(max_length=20, choices=SENDER_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} at {self.timestamp}'











from django.db import models

class StudentRequest(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    professor_email = models.EmailField(verbose_name="מייל המרצה", null=True, blank=True)
    request_type = models.CharField(max_length=200)
    description = models.TextField()
    professor_response = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'בהמתנה'), ('answered', 'נענה')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.request_type} - {self.status}"





from django.db import models

DOCUMENT_CHOICES = [
    ('study_confirmation', 'אישור לימודים'),
    ('payment_confirmation', 'אישור תשלום'),
    ('other', 'אחר'),
]

from django.db import models

DOCUMENT_CHOICES = [
    ('study_cert', 'אישור לימודים'),
    ('grade_cert', 'אישור ציונים'),
]

class DocumentRequest(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    document_type = models.CharField(max_length=50, choices=DOCUMENT_CHOICES)
    additional_info = models.TextField(blank=True, null=True)
    uploaded_document = models.FileField(upload_to='documents/', blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.get_document_type_display()}"



class UploadedDocument(models.Model):
    document_request = models.ForeignKey(DocumentRequest, on_delete=models.CASCADE, related_name='uploaded_documents')
    uploaded_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for {self.document_request} uploaded at {self.uploaded_at}"


from django.db import models
from django.utils import timezone

class ScheduleSlot(models.Model):
        lecturer_name = models.CharField(max_length=100)
        lecturer_email = models.EmailField()
        date = models.DateField()
        time = models.TimeField()
        is_booked = models.BooleanField(default=False)

        def __str__(self):
            return f"{self.lecturer_name} - {self.date} {self.time}"
class Booking(models.Model):
        slot = models.OneToOneField(ScheduleSlot, on_delete=models.CASCADE)
        student_name = models.CharField(max_length=100)
        student_email = models.EmailField()
        created_at = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return f"Booking with {self.student_name} on {self.slot}"



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






# accounts/models.py

from django.db import models
from django.conf import settings  # ✅ זה חשוב

class StuProf(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # ✅ במקום לשים ישירות את UserRegisterStu1
        on_delete=models.CASCADE
    )
    birth_date = models.DateField(null=True, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)  # השדה החדש





from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ReceptionHour(models.Model):
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reception_hours')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.lecturer.username} - {self.date} {self.start_time}-{self.end_time}"

class ReceptionBooking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reception_bookings')
    reception_hour = models.ForeignKey(ReceptionHour, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} booked {self.reception_hour}"


from django.db import models
from django.contrib.auth.models import User


class Consul(models.Model):
    title = models.CharField("נושא", max_length=100)
    date = models.DateField("תאריך")
    time = models.TimeField("שעה")
    location = models.CharField("מיקום", max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="נוצר על ידי")

    def __str__(self):
        return f"{self.title} - {self.date} {self.time}"

    class Meta:
        verbose_name = "שעת קבלה"
        verbose_name_plural = "שעות קבלה"
