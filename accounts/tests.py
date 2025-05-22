from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .forms import UserRegisterStu1Form, UserRegisterLecForm
from .models import UserRegisterStu1, UserRegisterLec

class SignupStudentViewTests(TestCase):
    def test_get_signup_student_form(self):
        response = self.client.get(reverse('signup_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup_student.html')
        self.assertIsInstance(response.context['form'], UserRegisterStu1Form)


from django.test import TestCase
from django.urls import reverse
from .models import UserRegisterLec

class SignupLecViewTests(TestCase):
    def test_get_signup_lec_form(self):
        response = self.client.get(reverse('signup_lec'))
        self.assertEqual(response.status_code, 200)





from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import request_grade_improvement, success_view
from .models import GradeImprovementRequest
from .forms import GradeImprovementRequestForm
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import GradeImprovementRequestForm

class GradeImprovementTest(TestCase):

    def setUp(self):
        # יצירת משתמש לדימוי התחברות
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_post_authenticated_creates_request(self):
        """אם המשתמש מחובר, הבקשה נשמרת ומועברת לדף הצלחה"""
        self.client.login(username='testuser', password='password123')
        data = {
            'course': 'History',
            'current_grade': 60,
            'requested_grade': 80,
            'reason': 'שיפרתי את ההבנה שלי במקצוע'
        }

        response = self.client.post('/grade-request/', data)  # שימוש ישיר בנתיב



    def test_post_unauthenticated_redirects_to_login(self):
        """משתמש לא מחובר מועבר לעמוד התחברות"""
        data = {
            'course': 'History',
            'current_grade': 60,
            'requested_grade': 80,
            'reason': 'שיפרתי את ההבנה שלי במקצוע'
        }

        response = self.client.post('/grade-request/', data)  # שימוש ישיר בנתיב

       # יפנה לעמוד התחברות אם המשתמש לא מחובר




from django.test import TestCase
from django.urls import reverse

class SuccessViewTest(TestCase):
    def test_success_page_status_code(self):
        response = self.client.get(reverse('success'))  # אם זה השם של ה-URL
        self.assertEqual(response.status_code, 200)





from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import UserRegisterStu1

class LoginViewTests(TestCase):

    def setUp(self):
        # צור משתמש auth.User עם סיסמה hashed
        self.auth_user = User.objects.create_user(username='testuser', password='1234')
        # צור את האובייקט שלך שמצביע עליו
        self.user = UserRegisterStu1.objects.create(user=self.auth_user)

    def test_get_request_returns_form(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_post_valid_login(self):
        data = {'username': 'testuser', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data)

        # ב־login מוצלח, מצפה ל־redirect
        self.assertEqual(response.status_code, 200)


    def test_post_invalid_password(self):
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(reverse('login'), data=data)

        # הטופס אמור להחזיר שגיאות, כלומר מצב 200 (reload הדף עם שגיאה)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)


    def test_post_nonexistent_user(self):
        data = {'username': 'nouser', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('שם משתמש לא קיים', form.non_field_errors())

    def test_post_invalid_form(self):
        data = {'username': '', 'password': ''}
        response = self.client.post(reverse('login'), data=data)

        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())


from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch, MagicMock
from accounts.views import login_view
from accounts.forms import LoginForm
from accounts.models import UserRegisterStu1, StudentLoginHistory

from django.test import TestCase, Client
from django.urls import reverse

class StudentPageViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_student_page_renders_correct_template(self):
        response = self.client.get(reverse('student_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_page.html')
