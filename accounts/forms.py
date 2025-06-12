from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
#from .models import UserData

# בתוך קובץ forms.py
from django import forms
from .models import UserRegister, UserRegisterLec, Appointment


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
class UserRegisterLecForm(forms.ModelForm):
    class Meta:
        model = UserRegisterLec
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


# forms.py
# forms.py
from django import forms
from .models import UserRegisterStu1

from django import forms
from .models import UserRegisterStu1

class UserRegisterStu1Form(forms.ModelForm):
    class Meta:
        model = UserRegisterStu1
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

# forms.py
from django import forms
from django.contrib.auth.models import User

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)  # שדה שם משתמש
    password = forms.CharField(widget=forms.PasswordInput())  # שדה סיסמה







from django import forms
from .models import GradeImprovementRequest

class GradeImprovementRequestForm(forms.ModelForm):
    class Meta:
        model = GradeImprovementRequest
        fields = ['username', 'course_name', 'current_grade', 'desired_grade', 'reason', 'email']  # הוספתי את 'username' לשדות
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 4}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter student email'})
        }



from django import forms
from .models import UserRegisterStu1

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegisterStu1
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import OfficeHours11

class OfficeHoursForm(forms.ModelForm):
    class Meta:
        model = OfficeHours11
        fields = ['office_name', 'opening_time', 'closing_time', 'additional_info']



from django import forms
from .models import StudentProfile
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['birth_date', 'field_of_study', 'graduation_year', 'gpa', 'profile_picture', 'email']



from django import forms
from .models import LoginHistory

class LoginHistoryForm(forms.ModelForm):
    class Meta:
        model = LoginHistory
        fields = ['user', 'success', 'ip_address']  # לא כולל את login_time כי הוא אוטומטי



# forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']


from django import forms

class ChatbotForm(forms.Form):
    user_message = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'chat-input'}))



# forms.py
from django import forms
from .models import TimeExtensionRequest
from django import forms
from .models import TimeExtensionRequest

class TimeExtensionRequestForm(forms.ModelForm):
    class Meta:
        model = TimeExtensionRequest
        fields = ['student_name', 'email', 'subject', 'original_deadline', 'requested_extension_time', 'reason_for_extension', 'supporting_documents']
        widgets = {
            'reason_for_extension': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django import forms
from .models import Lecturer, Meeting

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['name', 'office_hours', 'email', 'specialization']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['office_hours'].widget = forms.TextInput(attrs={'placeholder': 'שעות קבלה'})
        self.fields['specialization'].widget = forms.TextInput(attrs={'placeholder': 'התמחות'})

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateTimeInput(attrs={'placeholder': 'בחר תאריך ושעה לפגישה', 'type': 'datetime-local'})




# forms.py
from django import forms
from .models import OfficeHour

DAYS_OF_WEEK = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

TIME_CHOICES = [
    ('08:00', '08:00'),
    ('08:30', '08:30'),
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    # המשך לפי הצורך
]

import datetime

class OfficeHourForm(forms.ModelForm):
    day = forms.ChoiceField(choices=DAYS_OF_WEEK)
    start_time = forms.ChoiceField(choices=TIME_CHOICES)
    end_time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = OfficeHour
        fields = ['day', 'start_time', 'end_time']

    def clean_start_time(self):
        time_str = self.cleaned_data['start_time']
        return datetime.datetime.strptime(time_str, '%H:%M').time()

    def clean_end_time(self):
        time_str = self.cleaned_data['end_time']
        return datetime.datetime.strptime(time_str, '%H:%M').time()

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['phone_number']


from django import forms
from .models import StudentRequest

class StudentRequestForm(forms.ModelForm):
    professor_email = forms.EmailField(label="מייל המרצה")

    class Meta:
        model = StudentRequest
        fields = ['student_name', 'student_email', 'professor_email', 'request_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ProfessorResponseForm(forms.ModelForm):
    class Meta:
        model = StudentRequest
        fields = ['professor_response']
        widgets = {
            'professor_response': forms.Textarea(attrs={'rows': 4}),
        }



from django import forms
from .models import DocumentRequest

class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = DocumentRequest
        fields = ['student_name', 'student_email', 'document_type', 'additional_info']

from django import forms
from .models import DocumentRequest

from django import forms
from .models import UploadedDocument

class UploadedDocumentForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['uploaded_file']




from django import forms
from .models import ScheduleSlot

class ScheduleSlotForm(forms.ModelForm):
    class Meta:
        model = ScheduleSlot
        fields = ['lecturer_name', 'lecturer_email', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


from django import forms
from .models import UserRegisterStu1

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegisterStu1
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
from django import forms
from django.contrib.auth import get_user_model
from .models import StuProf

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StuProfForm(forms.ModelForm):
    class Meta:
        model = StuProf
        fields = ['birth_date', 'field_of_study', 'graduation_year', 'gpa', 'profile_picture']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }




from django import forms
from .models import ReceptionHour

class ReceptionHourForm(forms.ModelForm):
    class Meta:
        model = ReceptionHour
        fields = ['date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }





from django import forms
from .models import Consul

class ConsulForm(forms.ModelForm):
    class Meta:
        model = Consul
        fields = ['title', 'date', 'time', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
