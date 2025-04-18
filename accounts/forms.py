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
from .models import UserRegister, UserRegisterLec


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


# Django ModelForm for registering a lecturer
class UserRegisterLecForm(forms.ModelForm):
    class Meta:
        # Link this form to the UserRegisterLec model
        model = UserRegisterLec

        # Specify the fields to include in the form
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

