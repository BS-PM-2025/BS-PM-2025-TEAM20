from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, UserRegisterForm, UserRegisterLecForm, UserRegisterStu1Form

from django.shortcuts import render, redirect
from .models import StudentProfile


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # שנה את הכתובת לאן שתרצה להפנות אחרי שהטופס יישלח
    else:
        form = UserRegister()
    return render(request, 'signup.html', {'form': form})




from django.shortcuts import render, redirect
#from .forms import UserDataForm  # טופס הרשמה (וודא שהוא קיים)

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from .forms import UserDataForm
from .models import UserRegister, OfficeHours11, UserRegisterLec, UserRegisterStu1

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from .forms import UserDataForm


from django.shortcuts import render, redirect
from .forms import UserRegisterForm
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterStu1Form
from .models import UserRegisterStu1
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterStu1Form
from .models import UserRegisterStu1

from django.shortcuts import render, redirect
from .forms import UserRegisterStu1Form
from .models import UserRegisterStu1
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterStu1Form
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from .models import UserRegisterStu1
from .forms import UserRegisterStu1Form

def signup_student(request):
    if request.method == 'POST':
        form = UserRegisterStu1Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            student = form.save(commit=False)
            student.user = user
            student.save()

            return redirect('login')
    else:
        form = UserRegisterStu1Form()

    return render(request, 'signup_student.html', {'form': form})


# View to handle lecturer signup and redirect to 'lec_page'
def signup_lec(request):
    if request.method == 'POST':
        # Create a form instance with submitted POST data
        form = UserRegisterLecForm(request.POST)
        if form.is_valid():
            # Save the new lecturer to the database
            form.save()
            # Redirect to lecturer page after successful registration
            return redirect('lec_page')
    else:
        # If GET request, create an empty form
        form = UserRegisterLecForm()
    # Render the signup template with the form
    return render(request, 'signup_lec.html', {'form': form})





from django.shortcuts import render, redirect
from .forms import UserRegisterForm





def student_page(request):
    return render(request, 'student_page.html')  # דף התלמיד לאחר ההרשמה

def sec_page(request):
    return render(request, 'sec_page.html')  # דף התלמיד לאחר ההרשמה

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # ודא שקובץ home.html קיים בתיקיית templates שלך


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import UserRegister # Importing the UserData model

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import UserRegisterStu1, StudentLoginHistory
from .forms import LoginForm
from django.utils.timezone import now

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import LoginForm  # החלף עם הדרך שלך להיבא את טופס הכניסה
from django.utils.timezone import now
from .models import StudentLoginHistory
from accounts.models import UserRegisterStu1  # ודא שזה הנתיב הנכון למודל

from django.shortcuts import render, redirect
from django.utils.timezone import now
from .forms import LoginForm  # החלף עם הדרך שלך להיבא את טופס הכניסה
from .models import StudentLoginHistory
from accounts.models import UserRegisterStu1  # ודא שזה הנתיב הנכון למודל
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from .forms import LoginForm  # החלף עם הדרך שלך להיבא את טופס הכניסה
from .models import StudentLoginHistory
from accounts.models import UserRegisterStu1  # ודא שזה הנתיב הנכון למודל

from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserRegisterStu1, StudentLoginHistory
from django.utils.timezone import now

def login_view(request):
    print("Login function triggered!")  # Debugging message

    form = LoginForm()  # Initialize form

    if request.method == 'POST':
        print("POST request received!")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid!")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(f"Attempting login for: {username}")
            StudentLoginHistory.objects.create(username=username, login_time=now())
            print(f"Login attempt recorded for: {username}")

            try:
                user = UserRegisterStu1.objects.get(username=username)
                print(f"User found: {user.username}")

                if password == user.password:  # Match without encryption
                    print(f"Password matched for: {username}")
                    # שמירה ב-session (למשל)
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    return redirect('student_page')  # שים את שם הנתיב של הדף הבא שלך
                else:
                    print("Password mismatch.")
                    form.add_error(None, 'סיסמה לא נכונה')

            except UserRegisterStu1.DoesNotExist:
                print("User does not exist.")
                form.add_error(None, 'שם משתמש לא קיים')

        else:
            print("Form is not valid.")

    else:
        print("Request method is not POST.")

    return render(request, 'login.html', {'form': form})



# accounts/views.py
from django.shortcuts import render
# views.py
from .models import UserRegister

def student_page(request):
    return render(request, 'student_page.html')  # Render the student page template


from django.shortcuts import render, redirect

from .forms import LoginForm

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserRegister
from .models import StudentLoginHistory  # ייבוא הטבלה החדשה
from django.utils.timezone import now

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .models import UserRegisterStu1, StudentLoginHistory
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserRegisterStu1, StudentLoginHistory
from django.contrib.auth.hashers import check_password
from django.utils.timezone import now


def login_student(request):
    print("Login function triggered!")  # הדפסה בתחילת הפונקציה

    if request.method == 'POST':
        print("POST request received!")  # הדפסה אם הפנייה היא מסוג POST
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # הדפסה אם הטופס תקין
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(f"Attempting login for: {username}")  # הדפסה לבדוק שהנתונים נכונים

            try:
                user = UserRegisterStu1.objects.get(username=username)
                print(f"User found: {user.username}")  # הדפסה אם נמצא משתמש

                if check_password(password, user.password):  # בדיקת סיסמה
                    # 🔸 שמירה בהיסטוריית התחברויות
                    print(f"Password matched for: {username}")  # הדפסה אם הסיסמה נכונה
                    StudentLoginHistory.objects.create(username=username, login_time=now())

                    # התחברות עם Django
                    django_user = authenticate(request, username=username, password=password)
                    if django_user:
                        login(request, django_user)
                        print(f"Login successful for: {username}")  # הדפסה אחרי התחברות

                    return redirect('student_page')

                else:
                    form.add_error(None, 'סיסמה לא נכונה')

            except UserRegisterStu1.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')
                print(f"User not found: {username}")  # הדפסה אם לא נמצא משתמש

        else:
            print("Form is not valid.")  # הדפסה אם הטופס לא תקין

    else:
        print("Request method is not POST.")  # הדפסה





# View to handle secretary login
def login_sec(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                # Search for the user in UserRegister table by username
                user = UserRegister.objects.get(username=username)

                if user.password == password:
                    # If password matches, authenticate with Django system
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # If Django user is valid, log in the user
                        login(request, django_user)
                        # Redirect to secretary page after successful login
                        return redirect('sec_page')
                    else:
                        # If Django user not found, still redirect (can be improved)
                        return redirect('sec_page')
                else:
                    # Add form error if password is incorrect
                    form.add_error(None, 'Incorrect password')
            except UserRegister.DoesNotExist:
                # Add form error if username does not exist
                form.add_error(None, 'Username does not exist')
    else:
        form = LoginForm()

    return render(request, 'login_sec.html', {'form': form})


from .forms import UserRegisterForm

# views.py
from .forms import UserRegisterForm  # שים לב שאתה מייבא את הטופס, לא את המודל

def signup_sec(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # ודא שאתה משתמש בטופס ולא במודל
        if form.is_valid():
            form.save()  # שמירה של הטופס אם הוא תקין
            return redirect('sec_page')  # הפניה לעמוד הבא לאחר שמירה
    else:
        form = UserRegisterForm()  # יצירת טופס ריק אם לא נשלח POST
    return render(request, 'signup_sec.html', {'form': form})




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm
from .models import GradeImprovementRequest, UserRegisterStu1

def request_grade_improvement(request):
    if request.method == 'POST':
        form = GradeImprovementRequestForm(request.POST)
        if form.is_valid():
            grade_request = form.save(commit=False)

            # Assign the currently logged-in user (if exists)
            if request.user.is_authenticated:
                grade_request.student = request.user
                grade_request.save()
                return redirect('request_success')
            else:
                return redirect('login')  # Force login if no user
    else:
        form = GradeImprovementRequestForm()

    return render(request, 'request_form.html', {'form': form})
from django.shortcuts import render

def success_view(request):
    return render(request, 'request_success.html')




from .models import UserRegister, GradeImprovementRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import GradeImprovementRequest
from .models import UserRegisterStu1  # במידה ואתה משתמש בטבלה נפרדת להרשמת סטודנטים


from .models import UserRegisterStu1, GradeImprovementRequest
from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from .models import StudentLoginHistory, UserRegisterStu1, GradeImprovementRequest
from django.shortcuts import render
from .models import StudentLoginHistory, UserRegisterStu1, GradeImprovementRequest

from django.shortcuts import render
from django.contrib.auth.models import User  # Ensure this import exists


def student_requests(request):
    # 1. Get the most recent request from GRADEIMPROVEMENT
    last_request = GradeImprovementRequest.objects.order_by('-created_at').first()

    if not last_request:
        return render(request, 'student_requests.html', {
            'error': 'No grade improvement requests found',
            'requests': []
        })

    # 2. Get all requests from this user (by username)
    username = last_request.username
    requests = GradeImprovementRequest.objects.filter(username=username)

    return render(request, 'student_requests.html', {
        'requests': requests,
        'username': username,
        'last_login_time': last_request.created_at
    })
# student_requests/views.py
from django.shortcuts import render

# student_requests/views.py
from django.shortcuts import render




from django.shortcuts import render

from django.shortcuts import render
from .forms import GradeImprovementRequestForm  # אם אתה משתמש בטופס מותאם אישית
from django.shortcuts import render, redirect
from .forms import GradeImprovementRequestForm
from .models import GradeImprovementRequest  # הוספת המודל לשימוש

from django.shortcuts import redirect
from .models import UserRegisterStu1

from django.shortcuts import render, redirect
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm
from django.contrib.auth.decorators import login_required
from .models import UserRegisterStu1
from django.shortcuts import render, redirect
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm
from django.contrib.auth.decorators import login_required
from .models import UserRegisterStu1

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest, UserRegisterStu1
from .forms import GradeImprovementRequestForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GradeImprovementRequest, UserRegisterStu1
from .forms import GradeImprovementRequestForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest, UserRegisterStu1
from .forms import GradeImprovementRequestForm
from django.contrib import messages

@login_required
def request_form(request):
    if request.method == "POST":
        form = GradeImprovementRequestForm(request.POST)
        if form.is_valid():
            grade_request = form.save(commit=False)

            # קבלת הרשומה האחרונה מטבלת UserRegisterStu
            last_user_register = UserRegisterStu1.objects.order_by('-id').first()
            if not last_user_register:
                messages.error(request, "לא נמצאו משתמשים רשומים במערכת")
                return redirect('student_page')

            # ודא של־last_user_register יש אובייקט User תקין
            if not last_user_register.user:
                messages.error(request, "למשתמש האחרון אין משתמש מקושר")
                return redirect('student_page')

            # השמת ה‑student לפי user_id
            grade_request.student_id = last_user_register.user_id

            # מילוי אוטומטי של שדות email ו‑username אם הם ריקים
            if not grade_request.email:
                grade_request.email = last_user_register.email
            if not grade_request.username:
                grade_request.username = last_user_register.username

            grade_request.save()
            return redirect('request_success')
    else:
        # אפשר למלא מראש שדות מתוך המשתמש האחרון
        initial_data = {}
        last_user_register = UserRegisterStu1.objects.order_by('-id').first()
        if last_user_register and last_user_register.user:
            initial_data = {
                'email': last_user_register.email,
                'username': last_user_register.username,
            }
        form = GradeImprovementRequestForm(initial=initial_data)

    return render(request, 'request_form.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest




from django.shortcuts import render, get_object_or_404, redirect
from .models import GradeImprovementRequest
 # אני מניח שיש פונקציה כזו לשליחת המייל


from django.shortcuts import render
from .models import GradeImprovementRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import GradeImprovementRequest

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import GradeImprovementRequest  # ודא שזה הנתיב הנכון

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest  # ודא שזה הנתיב הנכון
@login_required
def request_list(request):
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        new_status = request.POST.get('status')

        grade_request = get_object_or_404(GradeImprovementRequest, id=request_id)
        grade_request.status = new_status
        grade_request.save()

        # ✅ Auto-send email in English
        student_email = grade_request.email
        subject = "Grade Improvement Request Status Update"
        body = f"""
Dear {grade_request.username},

The status of your grade improvement request for the course "{grade_request.course_name}" has been updated to: {new_status}

Request Details:
• Current Grade: {grade_request.current_grade}
• Desired Grade: {grade_request.desired_grade}
• Reason: {grade_request.reason}

If you have any questions or concerns, please contact the academic office.

Best regards,  
Grade Improvement System
"""

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [student_email],
                fail_silently=False
            )
        except BadHeaderError:
            print("Invalid header found.")
        except Exception as e:
            print(f"Error sending email: {e}")

        return redirect('request_list')

    requests = GradeImprovementRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def send_status_update_email(student_email, new_status, course_name):
    subject = f"Status Update for {course_name}"
    body = f"Dear Student,\n\nYour grade improvement request for {course_name} has been {new_status}.\n\nBest regards,\nYour University"

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,  # נוודא שהמייל שמוגדר ב־settings.py ישלח
        [student_email],  # שולחים לסטודנט
        fail_silently=False,
    )


from django.http import JsonResponse
from django.views import View


from django.shortcuts import render, redirect
from .models import OfficeHours11
from .forms import OfficeHoursForm

def add_office_hours(request):
    if request.method == 'POST':
        form = OfficeHoursForm(request.POST)
        if form.is_valid():
            form.save()  # שומר את המידע במסד הנתונים
            return redirect('show_office_hours')  # הפנה לדף שמציג את שעות הקבלה
    else:
        form = OfficeHoursForm()
    return render(request, 'add_office_hours.html', {'form': form})

def show_office_hours(request):
    hours = OfficeHours11.objects.all()  # טוען את כל שעות הקבלה מהמסד נתונים
    return render(request, 'show_office_hours.html', {'hours': hours})



from django.shortcuts import render
from .models import OfficeHours11

def office_hours_list(request):
    # טוען את כל שעות הקבלה מתוך הטבלה OfficeHours11
    office_hours = OfficeHours11.objects.all()
    return render(request, 'office_hours_list.html', {'office_hours': office_hours})


from django.shortcuts import render, redirect, get_object_or_404
from .models import UserRegisterStu1
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import UserRegisterStu1

from django.shortcuts import render, redirect
from .models import UserRegisterStu1, StudentProfile
from .forms import StudentProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserRegisterStu1, StudentProfile
from .forms import StudentProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserRegisterStu1, StudentProfile
from .forms import StudentProfileForm
def student_profile(request, edit=False):
    student = request.user
    student = get_object_or_404(UserRegisterStu1, pk=student.pk)
    profile, created = StudentProfile.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=profile)

    # אם עדיין אין מידע אקדמי בסיסי - נציג טופס בלבד
    needs_initial_data = not all([
        profile.birth_date,
        profile.field_of_study,
        profile.graduation_year,
        profile.gpa
    ])

    return render(request, 'profile.html', {
        'student': student,
        'form': form,
        'profile': profile,
        'edit_mode': edit or needs_initial_data,
        'needs_initial_data': needs_initial_data
    })

from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudentProfile
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import StudentProfile, UserRegisterStu1
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm
from django.views.decorators.csrf import csrf_exempt


def update_profile(request):
    # Get the student profile for the logged-in user
    student = get_object_or_404(UserRegisterStu1, user=request.user)
    profile = get_object_or_404(StudentProfile, student=student)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_profile')  # Redirect to profile page
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})


@csrf_exempt  # Only use this if absolutely necessary
def update_student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'student_profile_form.html', {'form': form})

from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm

def student_profile_view(request):
    # שליפת הסטודנט האחרון לפי id הגבוה ביותר
    student = UserRegisterStu1.objects.order_by('-id').first()

    if not student:
        return render(request, 'student_profile.html', {
            'error': 'No students found.'
        })

    # שליפת הפרופיל או יצירתו אם לא קיים
    profile, created = StudentProfile.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=profile)

    needs_initial_data = not all([
        profile.birth_date,
        profile.field_of_study,
        profile.graduation_year,
        profile.gpa
    ])

    return render(request, 'student_profile.html', {
        'student': student,
        'form': form,
        'profile': profile,
        'edit_mode': 'edit' in request.GET or needs_initial_data,
        'needs_initial_data': needs_initial_data
    })


from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import SetPasswordForm
from django.utils.encoding import force_bytes, force_str
from accounts.models import UserRegisterStu1  # שימוש בטבלה הנכונה
from django import forms


# טופס מותאם: בודק אימייל לפי המודל שלך
from django import forms

class CustomSetPasswordForm(forms.Form):
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("new_password1")
        pw2 = cleaned_data.get("new_password2")
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

from django import forms
from accounts.models import UserRegisterStu1

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not UserRegisterStu1.objects.filter(email=email).exists():
            raise forms.ValidationError("Email not found in the system.")
        return email


def send_password_reset_email(request):
    if request.method == "POST":
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = UserRegisterStu1.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')

                send_mail(
                    'Password Reset Request',
                    f'Click the following link to reset your password: {reset_link}',
                    'no-reply@yourapp.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('password_reset_done')
            except UserRegisterStu1.DoesNotExist:
                return render(request, 'password_reset.html', {'form': form, 'error': 'Email not found'})
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserRegisterStu1.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserRegisterStu1.DoesNotExist):
        return render(request, 'reset_password.html', {'error': 'Invalid reset link'})

    if not default_token_generator.check_token(user, token):
        return render(request, 'reset_password.html', {'error': 'Invalid token'})

    if request.method == "POST":
        form = CustomSetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password1"]
            user.password = new_password  # שימו לב: ללא הצפנה
            user.save()
            return redirect('login')
    else:
        form = CustomSetPasswordForm()

    return render(request, 'reset_password.html', {'form': form})


def password_reset_done(request):
    return render(request, 'password_reset_done.html')




###################################################################

# views.py

from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile, UserRegisterStu1
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def create_student_profile(request):
    # שליפת המשתמש האחרון שנוסף לטבלה
    user_register_stu = UserRegisterStu1.objects.order_by('-id').first()

    try:
        profile = StudentProfile.objects.get(student=user_register_stu)
        return redirect('profile')
    except StudentProfile.DoesNotExist:
        form = StudentProfileForm(request.POST or None, request.FILES or None)
        if request.method == "POST" and form.is_valid():
            profile = form.save(commit=False)
            profile.student = user_register_stu
            profile.save()
            return redirect('profile')

    return render(request, 'student_profile_form.html', {'form': form})
@login_required
def student_profile(request):
    try:
        # שליפת המשתמש האחרון בטבלה
        user_register_stu = UserRegisterStu1.objects.latest('id')
    except UserRegisterStu1.DoesNotExist:
        # אם אין משתמשים בטבלה - הפנה לעמוד יצירת פרופיל
        return redirect('create_student_profile')

    try:
        # שליפת פרופיל הסטודנט
        profile = StudentProfile.objects.get(student=user_register_stu)
    except StudentProfile.DoesNotExist:
        # אם אין פרופיל - הפנה ליצירת פרופיל
        return redirect('create_student_profile')

    # הוספת שם המשפחה כאן


    return render(request, 'profile.html', {
        'profile': profile,

    })
@login_required
def update_student_profile(request):
    try:
        user_register_stu = UserRegisterStu1.objects.get(user=request.user)
    except UserRegisterStu1.DoesNotExist:
        print("UserRegisterStu does not exist")
        return redirect('create_student_profile')

    try:
        profile = StudentProfile.objects.get(student=user_register_stu)
    except StudentProfile.DoesNotExist:
        print("StudentProfile does not exist")
        return redirect('create_student_profile')

    if request.method == "POST":
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
            return redirect('profile')
        else:
            print("Form errors:", form.errors)  # הדפס שגיאות אם ישנן
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'student_profile_form.html', {'form': form})
from django.shortcuts import render

def request_success(request):
    return render(request, 'request_success.html')
