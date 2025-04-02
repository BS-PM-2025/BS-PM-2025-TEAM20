from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

from django.shortcuts import render, redirect
from .forms import UserDataForm

def signup_view(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # שנה את הכתובת לאן שתרצה להפנות אחרי שהטופס יישלח
    else:
        form = UserDataForm()
    return render(request, 'signup.html', {'form': form})




from django.shortcuts import render, redirect
from .forms import UserDataForm  # טופס הרשמה (וודא שהוא קיים)

def signup_student(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_page')  # לאחר ההרשמה, הפנייה לדף התלמיד
    else:
        form = UserDataForm()
    return render(request, 'signup_student.html', {'form': form})  # הטופס יוצג ב-HTML

def signup_lec(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lec_page')  # לאחר ההרשמה, הפנייה לדף התלמיד
    else:
        form = UserDataForm()
    return render(request, 'signup_lec.html', {'form': form})  # הטופס יוצג ב-HTML

def signup_lecc(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecc_page')  # לאחר ההרשמה, הפנייה לדף התלמיד
    else:
        form = UserDataForm()
    return render(request, 'signup_lecc.html', {'form': form})  # הטופס יוצג ב-HTML

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
from .models import UserData  # Importing the UserData model


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user = UserData.objects.get(username=username)
                if user.password == password:  # בדוק אם הסיסמה תואמת
                    # אם הסיסמה נכונה, צור אובייקט משתמש של Django ואותך לאימות
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # התחבר למערכת
                        login(request, django_user)
                        return redirect('student_page')  # הפנה את המשתמש לדף הבית
                    else:
                        return redirect('student_page')   # אם לא נמצא משתמש
                else:
                    form.add_error(None, 'סיסמה לא נכונה')  # שגיאה אם הסיסמה לא נכונה
            except UserData.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# accounts/views.py
from django.shortcuts import render

def student_page(request):
    return render(request, 'student_page.html')  # Render the student page template


def login_student(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user = UserData.objects.get(username=username)
                if user.password == password:  # בדוק אם הסיסמה תואמת
                    # אם הסיסמה נכונה, צור אובייקט משתמש של Django ואותך לאימות
                    django_user = authenticate(request, username=username, password=password)

                    if django_user is not None:
                        # התחבר למערכת
                        login(request, django_user)
                        return redirect('student_page')  # הפנה את המשתמש לדף הבית
                    else:
                        return redirect('student_page')   # אם לא נמצא משתמש
                else:
                    form.add_error(None, 'סיסמה לא נכונה')  # שגיאה אם הסיסמה לא נכונה
            except UserData.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def login_lec(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user = UserData.objects.get(username=username)
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
            except UserData.DoesNotExist:
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
                user = UserData.objects.get(username=username)
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
            except UserData.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login_sec.html', {'form': form})



def signup_sec(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sec_page')  # לאחר ההרשמה, הפנייה לדף התלמיד
    else:
        form = UserDataForm()
    return render(request, 'signup_sec.html', {'form': form})  # הטופס יוצג ב-HTML



def lec_page(request):
    return render(request, 'sec_page.html')  # Render the lecturer page template



def login_lecc(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # חיפוש המשתמש ב- UserData לפי שם המשתמש
            try:
                user = UserData.objects.get(username=username)
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
            except UserData.DoesNotExist:
                form.add_error(None, 'שם משתמש לא קיים')  # שגיאה אם שם המשתמש לא קיים
    else:
        form = LoginForm()

    return render(request, 'login_lecc.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm


@login_required
def request_grade_improvement(request):
    if request.method == 'POST':
        form = GradeImprovementRequestForm(request.POST)
        if form.is_valid():
            grade_request = form.save(commit=False)
            grade_request.student = request.user
            grade_request.save()
            return redirect('request_success')
    else:
        form = GradeImprovementRequestForm()

    return render(request, 'request_form.html', {'form': form})


from django.shortcuts import render

def success_view(request):
    return render(request, 'request_success.html')  # עמוד הצלחה



@login_required
def student_requests(request):
    requests = GradeImprovementRequest.objects.filter(student=request.user)
    return render(request, 'student_requests.html', {'requests': requests})
# בקובץ views.py של


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


def request_form(request):
    if request.method == "POST":
        form = GradeImprovementRequestForm(request.POST)
        if form.is_valid():
            # יצירת אובייקט חדש במודל ושמירה למסד נתונים
            grade_improvement_request = form.save(commit=False)
            grade_improvement_request.student = request.user  # קביעת הסטודנט הנוכחי (אם יש צורך)
            grade_improvement_request.save()  # שמירה למסד נתונים

            # הפניית המשתמש לדף הצלחה
            return redirect('success')  # החלף בנתיב המתאים לדף הצלחה
    else:
        form = GradeImprovementRequestForm()

    return render(request, 'request_form.html', {'form': form})




def request_list(request):
    requests = GradeImprovementRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})
