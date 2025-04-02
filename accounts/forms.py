from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


# forms.py
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())







from django import forms
from .models import GradeImprovementRequest

class GradeImprovementRequestForm(forms.ModelForm):
    class Meta:
        model = GradeImprovementRequest
        fields = ['course_name', 'current_grade', 'desired_grade', 'reason']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 4})
        }
