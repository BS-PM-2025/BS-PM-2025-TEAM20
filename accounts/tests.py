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
