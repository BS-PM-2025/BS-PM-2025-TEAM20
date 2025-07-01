from datetime import timezone

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, UserRegisterForm, UserRegisterLecForm, UserRegisterStu1Form

from django.shortcuts import render, redirect


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

def signup_student(request):
    if request.method == 'POST':
        form = UserRegisterStu1Form(request.POST)  # השתמש בטופס הנכון
        if form.is_valid():
            form.save()  # שומר את הנתונים בטבלה UserRegisterLec
            return redirect('login')  # הפנייה לדף המתאים לאחר ההרשמה
    else:
        form = UserRegisterStu1Form()  # יוצרים את הטופס החדש במידה ולא נשלח טופס

    return render(request, 'signup_student.html', {'form': form})




def signup_lec(request):
    if request.method == 'POST':
        form = UserRegisterLecForm(request.POST)  # השתמש בטופס הנכון
        if form.is_valid():
            form.save()  # שומר את הנתונים בטבלה UserRegisterLec
            return redirect('lec_page')  # הפנייה לדף המתאים לאחר ההרשמה
    else:
        form = UserRegisterLecForm()  # יוצרים את הטופס החדש במידה ולא נשלח טופס

    return render(request, 'signup_lec.html', {'form': form})


def signup_lec(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lec_page')  # לאחר ההרשמה, הפנייה לדף התלמיד
    else:
        form = UserRegister()
    return render(request, 'signup_lec.html', {'form': form})  # הטופס יוצג ב-HTML

from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def signup_lecc(request):
    if request.method == 'POST':
        form = UserRegisterLecForm(request.POST)  # השתמש בטופס הנכון
        if form.is_valid():
            form.save()  # שומר את הנתונים בטבלה UserRegisterLec
            return redirect('lecc_page')  # הפנייה לדף המתאים לאחר ההרשמה
    else:
        form = UserRegisterLecForm()  # יוצרים את הטופס החדש במידה ולא נשלח טופס

    return render(request, 'signup_lec.html', {'form': form})



def student_page(request):
    return render(request, 'student_page.html')  # דף התלמיד לאחר ההרשמה
def lecc_page(request):
    return render(request, 'lecc_page.html')  # דף התלמיד לאחר ההרשמה

def lec_page(request):
    return render(request, 'sec_page.html')  # דף התלמיד לאחר ההרשמה

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


def login_lec(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user =  UserRegister.objects.get(username=username)
                if user.password == password:  # בדוק אם הסיסמה תואמת
                    # אם הסיסמה נכונה, צור אובייקט משתמש של Django ואותך לאימות
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # התחבר למערכת
                        login(request, django_user)
                        return redirect('lec_page')  # הפנה את המשתמש לדף הבית
                    else:
                        return redirect('lec_page')   # אם לא נמצא משתמש
                else:
                    form.add_error(None, 'סיסמה לא נכונה')  # שגיאה אם הסיסמה לא נכונה
            except  UserRegister.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login_lec.html', {'form': form})

def login_sec(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user =  UserRegister.objects.get(username=username)
                if user.password == password:  # בדוק אם הסיסמה תואמת
                    # אם הסיסמה נכונה, צור אובייקט משתמש של Django ואותך לאימות
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # התחבר למערכת
                        login(request, django_user)
                        return redirect('sec_page')  # הפנה את המשתמש לדף הבית
                    else:
                        return redirect('sec_page')   # אם לא נמצא משתמש
                else:
                    form.add_error(None, 'סיסמה לא נכונה')  # שגיאה אם הסיסמה לא נכונה
            except  UserRegister.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login_sec.html', {'form': form})


from .forms import UserRegisterForm  # וודא שזה הייבוא

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


def lec_page(request):
    return render(request, 'sec_page.html')  # Render the lecturer page template

def login_lecc(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserRegister לפי שם המשתמש
            user = UserRegisterLec.objects.filter(username=username).first()  # השתמש ב-filter

            if user:  # אם נמצא משתמש
                if user.password == password:  # בדוק אם הסיסמה תואמת
                    # אם הסיסמה נכונה, צור אובייקט משתמש של Django ואותך לאימות
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # התחבר למערכת
                        login(request, django_user)
                        return redirect('lecc_page')  # הפנה את המשתמש לדף הבית
                    else:
                        return redirect('lecc_page')   # אם לא נמצא משתמש
                else:
                    form.add_error(None, 'סיסמה לא נכונה')  # שגיאה אם הסיסמה לא נכונה
            else:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login_lecc.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm
from .models import GradeImprovementRequest, UserRegisterStu1

@login_required
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
    return render(request, 'request_success.html')  # עמוד הצלחה




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
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OfficeHours11
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OfficeHours11

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import OfficeHours11  # ודא שזה המודל הנכון שלך

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import OfficeHours11
import json

@csrf_exempt
def update_office_hour(request, id):  # לא office_id אלא id
    if request.method == 'POST':
        try:
            # עדכון הרשומה
            data = json.loads(request.body)
            office_name = data['office_name']
            opening_time = data['opening_time']
            closing_time = data['closing_time']
            additional_info = data['additional_info']

            office_hour = OfficeHours11.objects.get(id=id)
            office_hour.office_name = office_name
            office_hour.opening_time = opening_time
            office_hour.closing_time = closing_time
            office_hour.additional_info = additional_info
            office_hour.save()

            # החזרת HTML עם תוצאה מוצלחת
            return HttpResponse("""
                <html>
                <head><title>Office Hours Update</title></head>
                <body>
                    <h1>העדכון הצליח!</h1>
                    <p>המידע עודכן בהצלחה.</p>
                    <a href="/office_hours/">חזור</a>
                </body>
                </html>
            """)
        except Exception as e:
            return HttpResponse(f"""
                <html>
                <head><title>שגיאה</title></head>
                <body>
                    <h1>שגיאה בעדכון</h1>
                    <p>{str(e)}</p>
                    <a href="/office_hours/">חזור</a>
                </body>
                </html>
            """)

    elif request.method == 'DELETE':
        try:
            # מחיקת הרשומה
            office_hour = OfficeHours11.objects.get(id=id)
            office_hour.delete()

            # החזרת תוצאה מוצלחת
            return JsonResponse({"message": "המידע נמחק בהצלחה."}, status=200)

        except OfficeHours11.DoesNotExist:
            return JsonResponse({"error": "הרשומה לא נמצאה."}, status=404)

    else:
        return HttpResponse("""
            <html>
            <head><title>Invalid Request</title></head>
            <body>
                <h1>שגיאה</h1>
                <p>שיטה לא חוקית. רק POST ו-DELETE נתמכים.</p>
                <a href="/office_hours/">חזור</a>
            </body>
            </html>
        """)

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
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required




from django.views.decorators.csrf import csrf_exempt







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




from django.shortcuts import render

def request_success(request):
    return render(request, 'request_success.html')



# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback
import json

def feedback_page(request):
    return render(request, 'feedback.html')

def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = data.get('comment')
        rating = data.get('rating')

        if comment and rating:
            Feedback.objects.create(comment=comment, rating=rating)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})


from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatbotQuestion, ChatbotConversation
from .forms import ChatbotForm

from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatbotForm

from django.http import JsonResponse
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
# views.py
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import ChatHistory

import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatHistory
from django.shortcuts import render

def chatroom(request):
    return render(request, 'chatroom.html')
def chatroom1(request):
    return render(request, 'chatroom1.html')
def chatbot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('user_message', '')
            user_id = data.get('user_id', 'anonymous')

            if user_message:
                bot_response = get_bot_response(user_message)

                ChatHistory.objects.create(
                    user_id=user_id,
                    user_message=user_message,
                    bot_response=bot_response
                )

                return JsonResponse({'response': bot_response})
            else:
                return JsonResponse({'error': 'No message provided'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'chatbot.html')
from django.http import JsonResponse
from .models import ChatMessage

def get_messages(request):
    messages = ChatMessage.objects.order_by('timestamp')
    data = [
        {'sender': m.sender, 'message': m.message, 'timestamp': m.timestamp.strftime('%H:%M')}
        for m in messages
    ]
    return JsonResponse(data, safe=False)
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ChatMessage.objects.create(
            sender=data['sender'],
            message=data['message']
        )
        return JsonResponse({'status': 'success'})

def get_bot_response(user_message):
    if user_message.lower() == "hi":
        return "Hello, how can I assist you today?\n1. Improve your grade\n2. Request more time\n3. Schedule a meeting\n4. Other assistance"
    elif user_message == "1":
        return "You selected 'Improve your grade'. Would you like tips on studying or help with a specific subject?\n1. Tips for studying\n2. Help with a specific subject"
    elif user_message == "1.1":
        return "Focus on understanding key concepts and practice regularly."
    elif user_message == "1.2":
        return "Please tell me the subject you're struggling with."
    elif user_message == "2":
        return "You selected 'Request more time'. For assignment or exam?\n1. Assignment\n2. Exam"
    elif user_message == "3":
        return "Please provide a date/time and who you want to meet (tutor/professor)."
    elif user_message == "4":
        return "Please explain what other help you need."
    else:
        return "Sorry, I didn't understand that. Type 'hi' to start."


def chat_history_api(request, user_id):
    history = ChatHistory.objects.filter(user_id=user_id).order_by('timestamp')
    data = [
        {
            'user_message': c.user_message,
            'bot_response': c.bot_response,
            'timestamp': c.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        for c in history
    ]
    return JsonResponse(data, safe=False)



from django.shortcuts import render
from django.http import JsonResponse
from .models import MessageHistory
import json
from django.views.decorators.csrf import csrf_exempt

def chatroom(request):
    return render(request, 'chatroom.html')

def get_messages(request):
    # מציאת כל ההודעות בטבלה MessageHistory
    messages = MessageHistory.objects.order_by('timestamp')
    data = [
        {'sender': m.sender, 'message': m.message, 'timestamp': m.timestamp.strftime('%H:%M')}
        for m in messages
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        # קריאת נתוני ההודעה שנשלחה
        data = json.loads(request.body)
        sender = data['sender']
        message = data['message']

        # יצירת אובייקט חדש בטבלה MessageHistory
        MessageHistory.objects.create(
            sender=sender,
            message=message
        )

        return JsonResponse({'status': 'success'})




from django.shortcuts import render, redirect
from .models import FormRequest, FormUpload
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# דף בו סטודנט יכול לבקש טופס
@login_required
def request_for_form(request):
    if request.method == "POST":
        form_name = request.POST.get('form_name')
        FormRequest.objects.create(student=request.user, form_name=form_name)
        return redirect('form_requests')  # אחרי שמגישים את הבקשה, מעבירים לדף בקשות הטפסים

    return render(request, 'request_for_form.html')

# דף שמציג את כל הבקשות של הסטודנט
@login_required
def form_requests(request):
    # הצגת כל הבקשות של הסטודנט הנוכחי
    requests = FormRequest.objects.filter(student=request.user)

    if request.method == 'POST':
        form_name = request.POST['form_name']

        # יצירת בקשה חדשה והקשר למשתמש הנוכחי
        form_request = FormRequest(
            student=request.user,  # כאן אנחנו שומרים את המשתמש הנוכחי
            form_name=form_name,
            request_date=timezone.now(),
            status='Pending'
        )
        form_request.save()

        return redirect('form_requests')  # לאחר ההגשה, החזר את המשתמש לאותו דף

    return render(request, 'form_requests.html', {'requests': requests})


# דף שמציג את כל הטפסים שהעלו המזכירות
@login_required
def form_list(request):
    forms = FormUpload.objects.all()
    return render(request, 'form_list.html', {'forms': forms})


from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FormRequest
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FormRequest
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


@login_required
def upload_form(request):
    if request.method == 'POST':
        form_name = request.POST.get('form_name')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        student_email = request.POST.get('Email')

        # קבלת קובץ ה-PDF
        pdf_file = request.FILES['file']

        # אחסון הקובץ במערכת הקבצים
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)

        # יצירת אובייקט חדש עם פרטי הבקשה
        form_request = FormRequest(
            student=request.user,
            form_name=form_name,
            pdf_file=filename
        )
        form_request.save()

        return HttpResponse('Your form request has been uploaded successfully.')

    return render(request, 'upload_form.html')



# views.py
from django.shortcuts import render, redirect
from .forms import TimeExtensionRequestForm
from .models import TimeExtensionRequest

def submit_extension_request(request):
    if request.method == 'POST':
        form = TimeExtensionRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('last_student_requests.html')
    else:
        form = TimeExtensionRequestForm()
    return render(request, 'submit_extension_request.html', {'form': form})

def request_success(request):
    return render(request, 'request_success.html')




# views.py
from django.shortcuts import render, redirect
from .forms import TimeExtensionRequestForm
from django.shortcuts import render, redirect
from .forms import TimeExtensionRequestForm
from .models import TimeExtensionRequest
from django.shortcuts import render, redirect
from .forms import TimeExtensionRequestForm
from .models import TimeExtensionRequest

def submit_time_extension_request(request):
    if request.method == 'POST':
        form = TimeExtensionRequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save()

            # שמירת האימייל של הסטודנט בסשן
            request.session['last_student_email'] = new_request.email

            return redirect('last_student_requests')
        else:
            print("הטופס לא תקין:", form.errors)
            return render(request, 'request_time_extension.html', {'form': form})
    else:
        form = TimeExtensionRequestForm()

    return render(request, 'request_time_extension.html', {'form': form})

def last_student_requests(request):
    last_email = request.session.get('last_student_email')

    if not last_email:
        return render(request, 'last_student_requests.html', {
            'student_requests': [],
            'error': 'לא נמצאה כתובת אימייל של סטודנט. יש להגיש בקשה תחילה.'
        })

    student_requests = TimeExtensionRequest.objects.filter(email=last_email)
    return render(request, 'last_student_requests.html', {
        'student_requests': student_requests,
        'email': last_email
    })

def request_success(request):
    # הצגת הודעת הצלחה
    return render(request, 'request_success.html', {'message': 'הבקשה הוגשה בהצלחה!'})



from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import TimeExtensionRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages  # נוסיף את המודול הזה
from .models import TimeExtensionRequest

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
import logging
import logging
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages

# הגדרת לוגינג
logger = logging.getLogger(__name__)
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
import logging
from .models import TimeExtensionRequest  # ודא שזה הנתיב למודל שלך

# הגדרת הלוגר
logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import TimeExtensionRequest

def extension_request_list(request):
    print("📍 נכנסתי לפונקציה extension_request_list")

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        new_status = request.POST.get('status')

        print(f"🔄 קיבלנו בקשה לעדכון סטטוס. מזהה הבקשה: {request_id}, סטטוס חדש: {new_status}")

        try:
            extension_request = get_object_or_404(TimeExtensionRequest, id=request_id)
            print(f"✅ הבקשה נמצאה: {extension_request}")
        except Exception as e:
            print(f"❌ שגיאה באחזור הבקשה: {e}")
            messages.error(request, f"שגיאה באחזור הבקשה: {e}")
            return redirect('extension_request_list')

        try:
            extension_request.status = new_status
            extension_request.save()
            print(f"✅ סטטוס הבקשה עודכן ל: {extension_request.get_status_display()}")
        except Exception as e:
            print(f"❌ שגיאה בעדכון הסטטוס: {e}")
            messages.error(request, f"שגיאה בעדכון הסטטוס: {e}")
            return redirect('extension_request_list')

        student_email = extension_request.email
        print(f"📧 כתובת המייל של הסטודנט: {student_email}")

        if student_email:
            subject = "עדכון סטטוס לבקשת הארכת זמן"
            body = f"""
שלום {extension_request.student_name},

הסטטוס של בקשתך להארכת זמן במקצוע "{extension_request.subject}" 
עודכן ל: {extension_request.get_status_display()}

פרטי הבקשה:
• מועד הגשה מקורי: {extension_request.original_deadline}
• מספר ימים שהתבקשו: {extension_request.requested_extension_time}
• סיבה: {extension_request.reason_for_extension}

בברכה,
מערכת ניהול בקשות
"""
            try:
                print("📤 מנסה לשלוח את המייל עם התוכן הבא:")
                print("נושא:", subject)
                print("גוף ההודעה:\n", body)

                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [student_email],
                    fail_silently=False,
                )
                print("✅ המייל נשלח בהצלחה.")
                messages.success(request, f"המייל נשלח לכתובת {student_email} בהצלחה.")
            except BadHeaderError:
                print("❌ שגיאה: כותרת מייל לא תקינה.")
                messages.error(request, "כותרת המייל לא תקינה.")
            except Exception as e:
                print(f"❌ שגיאה בשליחת מייל: {e}")
                messages.error(request, f"שגיאה בשליחת מייל: {e}")
        else:
            print("⚠️ אין כתובת מייל תקינה לסטודנט.")
            messages.warning(request, "לא קיימת כתובת מייל תקינה לסטודנט.")

        return redirect('extension_request_list')

    # GET - הצגת כל הבקשות
    requests = TimeExtensionRequest.objects.all()
    print(f"📋 מספר הבקשות הכולל: {requests.count()}")
    return render(request, 'extension_request_list.html', {'requests': requests})



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MeetingRequest

def schedule_meeting(request):
    if request.method == 'POST':
        meeting_date = request.POST.get('date')
        meeting_time = request.POST.get('time')
        student_email = request.user.email  # אם הסטודנט מחובר

        try:
            # יצירת בקשה לפגישה
            meeting_request = MeetingRequest(
                student_email=student_email,
                meeting_date=meeting_date,
                meeting_time=meeting_time,
                status='pending'
            )
            meeting_request.save()

            # שליחת הודעה על הצלחה
            messages.success(request, f"פגישה נקבעה בהצלחה לתאריך {meeting_date} בשעה {meeting_time}.")
        except Exception as e:
            # שליחת הודעה על שגיאה
            messages.error(request, f"שגיאה בקביעת הפגישה: {e}")

        return redirect('schedule_meeting')

    return render(request, 'schedule_meeting.html')


# accounts/views.py

from django.shortcuts import render




# accounts/views.py

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Lecturer, Meeting
from .forms import LecturerForm, MeetingForm

# View למרצה להוסיף/לעדכן את פרטיו
@login_required
def add_or_update_lecturer(request):
    try:
        lecturer = Lecturer.objects.get(user=request.user)
    except Lecturer.DoesNotExist:
        lecturer = None

    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.user = request.user
            lecturer.save()
            return redirect('lecturer_profile')
    else:
        form = LecturerForm(instance=lecturer)

    return render(request, 'lecturer_form.html', {'form': form})

# View לסטודנט לקבוע פגישה עם המרצה
@login_required
def schedule_meeting(request, lecturer_id):
    lecturer = Lecturer.objects.get(id=lecturer_id)
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.student = request.user
            meeting.lecturer = lecturer
            meeting.save()

            # שליחת מייל לאישור הפגישה
            send_mail(
                'אישור פגישה עם מרצה',
                f'שלום {request.user.username},\n\n הפגישה שלך עם {lecturer.name} נקבעה ל-{meeting.date}.',
                'from@example.com',
                [request.user.email],
            )

            send_mail(
                'פגישה חדשה',
                f'שלום {lecturer.name},\n\n סטודנט {request.user.username} קבע פגישה לתאריך {meeting.date}.',
                'from@example.com',
                [lecturer.email],
            )

            return redirect('student_profile')
    else:
        form = MeetingForm()

    return render(request, 'schedule_meeting.html', {'form': form, 'lecturer': lecturer})

# View לפרופיל המרצה
@login_required
def lecturer_profile(request):
    try:
        lecturer = Lecturer.objects.get(user=request.user)
    except Lecturer.DoesNotExist:
        lecturer = None
    return render(request, 'lecturer_profile.html', {'lecturer': lecturer})

# View לפרופיל הסטודנט עם כל הפגישות
@login_required
def student_profile(request):
    meetings = Meeting.objects.filter(student=request.user)
    return render(request, 'student_profile.html', {'meetings': meetings})





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StuProf
from .forms import StuProfForm,UserProfileForm

@login_required
def manage_my_profile(request):
    user = request.user
    profile = StuProf.objects.filter(student=user).first()

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        profile_form = StuProfForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            prof = profile_form.save(commit=False)
            prof.student = user
            prof.save()
            return redirect('my_profile')

    else:
        user_form = UserProfileForm(instance=user)
        profile_form = StuProfForm(instance=profile)

    if profile:
        return render(request, 'my_profile_info.html', {
            'user': user,
            'profile': profile
        })
    else:
        return render(request, 'my_profile_form.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })









from django.shortcuts import render, get_object_or_404, redirect
from .models import OfficeHour, Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OfficeHour, Appointment
from .forms import AppointmentForm, OfficeHourForm

@login_required
def create_slots(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        form = OfficeHourForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.lecturer = request.user
            slot.save()
            return redirect('my_appointments')
    else:
        form = OfficeHourForm()
    return render(request, 'create_slots.html', {'form': form})

def office_hours_list(request):
    hours = OfficeHour.objects.all()
    return render(request, 'office_hours_list.html', {'hours': hours})
@login_required
def book_appointment(request, pk):
    office_hour = get_object_or_404(OfficeHour, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = request.user
            appointment.office_hour = office_hour
            appointment.save()
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'office_hour': office_hour})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import OfficeHour

@login_required
def my_appointments(request):
    # אם המשתמש הוא מרצה, נקבל את כל שעות הקבלה שלו
    if request.user.is_staff:
        office_hours = OfficeHour.objects.filter(lecturer=request.user).order_by('day', 'start_time')
    else:
        # אם זה סטודנט, נציג את כל שעות הקבלה הקיימות של כל המרצים
        office_hours = OfficeHour.objects.all().order_by('lecturer__username', 'day', 'start_time')

    return render(request, 'my_appointments.html', {'office_hours': office_hours})
@login_required
def lecturer_appointments(request):
    if not request.user.is_staff:
        return redirect('home')  # או דף אחר

    appointments = Appointment.objects.filter(office_hour__lecturer=request.user).select_related('student', 'office_hour')
    return render(request, 'lecturer_appointments.html', {'appointments': appointments})


@login_required
def available_office_hours(request):
    # רק לסטודנטים מותר לראות את הדף הזה
    if request.user.is_staff:
        return redirect('home')

    booked = Appointment.objects.filter(student=request.user).values_list('office_hour_id', flat=True)
    office_hours = OfficeHour.objects.exclude(id__in=booked)

    return render(request, 'student_available_hours.html', {
        'office_hours': office_hours
    })

@login_required
def confirm_appointment(request, pk):
    office_hour = get_object_or_404(OfficeHour, pk=pk)

    # למנוע כפילויות
    if Appointment.objects.filter(student=request.user, office_hour=office_hour).exists():
        return redirect('my_appointments')

    Appointment.objects.create(
        student=request.user,
        office_hour=office_hour
    )
    return redirect('my_appointments')
# views.py
@login_required
def student_available_hours(request):
    office_hours = OfficeHour.objects.all()
    return render(request, 'student_available_hours.html', {'office_hours': office_hours})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import ChatMessageSec
from django.utils.timezone import localtime
import json

def student_secretary_chat_view(request):
    return render(request, 'student_secretary_chat.html')

def get_messages_sec(request):
    messages = ChatMessageSec.objects.order_by('timestamp')
    data = [
        {
            'sender': msg.sender,
            'message': msg.message,
            'timestamp': localtime(msg.timestamp).strftime('%H:%M')
        }
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def send_message_sec(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ChatMessageSec.objects.create(sender=data['sender'], message=data['message'])
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'fail'}, status=400)



from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import StudentRequest
from .forms import StudentRequestForm, ProfessorResponseForm
from django.conf import settings

def submit_request_view(request):
    if request.method == 'POST':
        form = StudentRequestForm(request.POST)
        if form.is_valid():
            student_request = form.save()

            # שליחת מייל למרצה (לפי המייל שהסטודנט הזין)
            subject = f"בקשה חדשה מסטודנט: {student_request.request_type}"
            message = f"""
שלום,

סטודנט בשם {student_request.student_name} שלח לך בקשה מסוג: {student_request.request_type}

פרטים:
{student_request.description}

ליצירת קשר עם הסטודנט:
אימייל: {student_request.student_email}

---

מערכת ניהול הבקשות
"""
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [student_request.professor_email],
                fail_silently=False,
            )

            messages.success(request, "הבקשה נשלחה בהצלחה למייל של המרצה.")
            return redirect('submit_request')
    else:
        form = StudentRequestForm()
    return render(request, 'submit_request.html', {'form': form})


def professor_requests_view(request):
    # לצורך פשטות, נראה רק רשימת כל הבקשות ללא קשר לפרופסור ספציפי
    requests = StudentRequest.objects.all().order_by('-created_at')
    return render(request, 'professor_requests.html', {'requests': requests})


def respond_request_view(request, request_id):
    student_request = get_object_or_404(StudentRequest, pk=request_id)

    if request.method == 'POST':
        form = ProfessorResponseForm(request.POST, instance=student_request)
        if form.is_valid():
            student_request = form.save(commit=False)
            student_request.status = 'answered'
            student_request.save()

            # שליחת מייל חזרה לסטודנט עם תגובת המרצה
            subject = f"תשובה לבקשתך: {student_request.request_type}"
            message = f"""
שלום {student_request.student_name},

המרצה הגיב לבקשתך:

{student_request.professor_response}

בהצלחה,
מערכת ההודעות
"""
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [student_request.student_email],
                fail_silently=False,
            )
            messages.success(request, "התגובה נשלחה בהצלחה לסטודנט.")
            return redirect('professor_requests')
    else:
        form = ProfessorResponseForm(instance=student_request)

    return render(request, 'respond_request.html', {'form': form, 'student_request': student_request})




# views.py
from django.shortcuts import render
from .models import Feedback

def all_feedbacks_view(request):
    feedbacks = Feedback.objects.all().order_by('-id')  # מציג את החדשים קודם
    return render(request, 'all_feedbacks.html', {'feedbacks': feedbacks})














from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import DocumentRequest
from .forms import DocumentRequestForm,UploadedDocumentForm
from django.conf import settings

def submit_document_request(request):
    if request.method == 'POST':
        form = DocumentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "הבקשה נשלחה למזכירות.")
            return redirect('submit_document_request')
    else:
        form = DocumentRequestForm()
    return render(request, 'submit_document_request.html', {'form': form})

def secretary_requests_view(request):
    requests = DocumentRequest.objects.filter(is_completed=False).order_by('-created_at')
    return render(request, 'secretary_requests.html', {'requests': requests})
# views.py
from django.shortcuts import get_object_or_404

def document_request_detail(request, request_id):
    document_request = get_object_or_404(DocumentRequest, id=request_id)
    return render(request, 'document_request_detail.html', {'request': document_request})

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import UploadedDocumentForm
from .models import DocumentRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import UploadedDocumentForm
from .models import DocumentRequest
import os

import os
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import UploadedDocumentForm
from .models import DocumentRequest
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import UploadedDocumentForm
from .models import DocumentRequest

import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import UploadedDocumentForm
from .models import DocumentRequest, UploadedDocument

def upload_document_view(request, request_id):
    print(f"--- upload_document_view called with request_id={request_id} ---")
    doc_request = get_object_or_404(DocumentRequest, id=request_id)
    print(f"Loaded DocumentRequest: {doc_request}")

    if request.method == 'POST':
        print("Request method is POST")
        print(f"FILES in request: {request.FILES}")
        print(f"POST data: {request.POST}")

        form = UploadedDocumentForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form is valid")
            uploaded_doc = form.save(commit=False)
            uploaded_doc.document_request = doc_request
            uploaded_doc.save()
            print("UploadedDocument saved")

            doc_request.is_completed = True
            doc_request.save()
            print("Marked DocumentRequest as completed")

            email = EmailMessage(
                subject=f"אישור {doc_request.get_document_type_display()}",
                body=f"שלום {doc_request.student_name},\nמצורף האישור שביקשת.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[doc_request.student_email]
            )

            file_path = uploaded_doc.uploaded_file.path
            print(f"File path: {file_path}")

            if os.path.exists(file_path):
                email.attach_file(file_path)
                print("File attached to email")
            else:
                print(f"ERROR: File not found on disk at path: {file_path}")

            try:
                email.send()
                print("Email sent successfully")
                messages.success(request, "האישור נשלח לסטודנט.")
            except Exception as e:
                print(f"ERROR sending email: {e}")
                messages.error(request, "אירעה שגיאה בשליחת המייל.")

            return redirect('secretary_requests')
        else:
            print("Form invalid")
            print(form.errors)
            messages.error(request, "טופס לא תקין, בדוק את הנתונים והקובץ.")
    else:
        print("Request method is GET or other")
        form = UploadedDocumentForm()

    return render(request, 'upload_document.html', {'form': form, 'doc_request': doc_request})




from django.shortcuts import render, redirect, get_object_or_404
from .models import ScheduleSlot, Booking
from .forms import ScheduleSlotForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def lecturer_create_slot(request):
    if request.method == 'POST':
        form = ScheduleSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Slot created successfully!")
            return redirect('lecturer_create')
    else:
        form = ScheduleSlotForm()
    return render(request, 'lecturer_create.html', {'form': form})

def student_view_slots(request):
    slots = ScheduleSlot.objects.filter(is_booked=False).order_by('date', 'time')
    return render(request, 'student_view.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = get_object_or_404(ScheduleSlot, id=slot_id, is_booked=False)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')

        Booking.objects.create(
            slot=slot,
            student_name=student_name,
            student_email=student_email
        )
        slot.is_booked = True
        slot.save()

        send_mail(
            subject='New Booking Made',
            message=f"{student_name} booked a slot on {slot.date} at {slot.time}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[slot.lecturer_email],
        )

        messages.success(request, "Booking confirmed.")
        return redirect('student_view')

    return render(request, 'book_slot.html', {'slot': slot})

def cancel_booking(request, slot_id):
    slot = get_object_or_404(ScheduleSlot, id=slot_id)
    booking = get_object_or_404(Booking, slot=slot)

    if request.method == 'POST':
        student_name = booking.student_name
        booking.delete()
        slot.is_booked = False
        slot.save()

        send_mail(
            subject='Booking Cancelled',
            message=f"{student_name} cancelled the booking on {slot.date} at {slot.time}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[slot.lecturer_email],
        )

        messages.success(request, "Booking cancelled.")
        return redirect('student_view')

    return render(request, 'cancel_booking.html', {'slot': slot})




from django.shortcuts import render, redirect
from .models import StuProf
from .forms import StuProfForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import StuProf
from .forms import UserProfileForm, StuProfForm

User = get_user_model()


@login_required
def manage_my_profile(request):
    user = request.user
    profile, created = StuProf.objects.get_or_create(student=user)

    # אם הפרופיל כבר קיים (כלומר לא נוצר עכשיו) ויש לו נתונים - נעשה הפניה ל-profile_detail
    # אפשר לבדוק למשל שדה חובה כמו birth_date או כל שדה אחר שמאפיין שהפרופיל מלא
    if not created and profile.birth_date is not None:
        return redirect('profile_detail')

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        profile_form = StuProfForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_detail')
    else:
        user_form = UserProfileForm(instance=user)
        profile_form = StuProfForm(instance=profile)

    return render(request, 'manage_my_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def profile_detail(request):
    user = request.user
    profile = StuProf.objects.filter(student=user).first()
    return render(request, 'profile_detail.html', {
        'user': user,
        'profile': profile,
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .models import ReceptionHour, ReceptionBooking
from .forms import ReceptionHourForm


@login_required
def lecturer_reception_hours(request):
    if request.method == 'POST':
        form = ReceptionHourForm(request.POST)
        if form.is_valid():
            reception_hour = form.save(commit=False)
            reception_hour.lecturer = request.user
            reception_hour.save()
            return redirect('lecturer_reception_hours')
    else:
        form = ReceptionHourForm()

    reception_hours = ReceptionHour.objects.filter(lecturer=request.user).order_by('date', 'start_time')
    return render(request, 'lecturer_reception_hours.html',
                  {'form': form, 'reception_hours': reception_hours})


@login_required
def student_reception_hours(request):
    reception_hours = ReceptionHour.objects.all().order_by('date', 'start_time')
    bookings = ReceptionBooking.objects.filter(student=request.user)
    booked_reception_hour_ids = bookings.values_list('reception_hour_id', flat=True)

    return render(request, 'student_reception_hours.html', {
        'reception_hours': reception_hours,
        'booked_reception_hour_ids': booked_reception_hour_ids,
    })


@login_required
def book_reception_hour(request, reception_hour_id):
    reception_hour = get_object_or_404(ReceptionHour, pk=reception_hour_id)
    if ReceptionBooking.objects.filter(reception_hour=reception_hour).exists():
        return redirect('student_reception_hours')

    ReceptionBooking.objects.create(student=request.user, reception_hour=reception_hour)

    send_mail(
        subject=f"הזמנת פגישה לשעות קבלה",
        message=f"הסטודנט {request.user.username} הזמין פגישה ל-{reception_hour.date} בין {reception_hour.start_time} ל-{reception_hour.end_time}.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[reception_hour.lecturer.email],
        fail_silently=True,
    )

    return redirect('student_reception_hours')
# עדכון קטן לצורך commit
# עדכון קטן לצורך commit
# עדכון קטן לצורך commit
# עדכון קטן לצורך commit
# עדכון קטן לצורך commit



@login_required
def cancel_reception_booking(request, booking_id):
    booking = get_object_or_404(ReceptionBooking, pk=booking_id, student=request.user)
    reception_hour = booking.reception_hour
    lecturer_email = reception_hour.lecturer.email
    booking.delete()

    send_mail(
        subject=f"ביטול פגישה לשעות קבלה",
        message=f"הסטודנט {request.user.username} ביטל את הפגישה ל-{reception_hour.date} בין {reception_hour.start_time} ל-{reception_hour.end_time}.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[lecturer_email],
        fail_silently=True,
    )
    return redirect('student_reception_hours')





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ConsulForm
from .models import Consul

@login_required
def add1_consul(request):
    if request.method == 'POST':
        form = ConsulForm(request.POST)
        if form.is_valid():
            consul = form.save(commit=False)
            consul.created_by = request.user
            consul.save()
            return redirect('consul_list')
    else:
        form = ConsulForm()
    return render(request, 'consul_form.html', {'form': form})

@login_required
def consul_list(request):
    consuls = Consul.objects.all().order_by('date', 'time')
    return render(request, 'consul_list.html', {'consuls': consuls})

@login_required
def cancel_consul(request, consul_id):
    consul = get_object_or_404(Consul, id=consul_id)

    if request.method == 'POST':
        # שלח מייל
        send_mail(
            subject='ביטול שעת קבלה',
            message=f"השעה הבאה בוטלה:\n\nכותרת: {consul.title}\nתאריך: {consul.date}\nשעה: {consul.time}\nמיקום: {consul.location}",
            from_email='your_email@example.com',
            recipient_list=['elatrshnaghm@gmail.com'],
            fail_silently=False,
        )

        # מחק מהמסד נתונים
        consul.delete()

    return redirect('consul_list')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import DocumentRequest

@login_required
def my_document_requests(request):
    # סינון לפי כתובת המייל של המשתמש המחובר
    user_email = request.user.email
    my_requests = DocumentRequest.objects.filter(student_email=user_email).order_by('-created_at')
    return render(request, 'my_document_requests.html', {'requests': my_requests})

