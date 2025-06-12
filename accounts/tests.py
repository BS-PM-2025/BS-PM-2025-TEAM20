
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import (
    UserRegisterStu1Form,
    UserRegisterLecForm,
    GradeImprovementRequestForm,
    LoginForm
)
from .models import (
    UserRegisterStu1,
    UserRegisterLec,
    GradeImprovementRequest,
    StudentLoginHistory
)

class SignupStudentViewTests(TestCase):
    def test_get_signup_student_form(self):
        response = self.client.get(reverse('signup_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup_student.html')
        self.assertIsInstance(response.context['form'], UserRegisterStu1Form)


class SignupLecViewTests(TestCase):
    def test_get_signup_lec_form(self):
        response = self.client.get(reverse('signup_lec'))
        self.assertEqual(response.status_code, 200)


class GradeImprovementTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_post_authenticated_creates_request(self):
        self.client.login(username='testuser', password='password123')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'course_name': 'History',
            'current_grade': 60,
            'desired_grade': 80,
            'reason': 'שיפרתי את ההבנה שלי במקצוע'
        }
        response = self.client.post(reverse('request_grade_improvement'), data)
        self.assertRedirects(response, reverse('request_success'))
        self.assertEqual(GradeImprovementRequest.objects.count(), 1)

    def test_post_unauthenticated_redirects_to_login(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'course_name': 'History',
            'current_grade': 60,
            'desired_grade': 80,
            'reason': 'שיפרתי את ההבנה שלי במקצוע'
        }
        response = self.client.post(reverse('request_grade_improvement'), data)
        self.assertRedirects(response, reverse('login'))


class GradeImprovementRequestFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'student1',
            'email': 'student@example.com',
            'course_name': 'Math',
            'current_grade': 60,
            'desired_grade': 90,
            'reason': 'Improved understanding'
        }
        form = GradeImprovementRequestForm(data=form_data)
        self.assertTrue(form.is_valid())


class SuccessViewTest(TestCase):
    def test_success_page_status_code(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)


class LoginViewTests(TestCase):
    def setUp(self):
        self.auth_user = User.objects.create_user(username='testuser', password='1234')
        self.user = UserRegisterStu1.objects.create(user=self.auth_user, username='testuser', email='user@example.com',
                                                    password='1234', first_name='Test', last_name='User')

    def test_get_request_returns_form(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_post_valid_login(self):
        data = {'username': 'testuser', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data)
        self.assertRedirects(response, reverse('student_page'))

    def test_post_invalid_password(self):
        data = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post(reverse('login'), data=data)
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


class StudentPageViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_student_page_renders_correct_template(self):
        response = self.client.get(reverse('student_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_page.html')
