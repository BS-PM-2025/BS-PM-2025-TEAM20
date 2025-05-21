
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterStu1Form, GradeImprovementRequestForm
from .models import UserRegisterStu1, GradeImprovementRequest, TimeExtensionRequest
from django.core.files.uploadedfile import SimpleUploadedFile

class SignupStudentTests(TestCase):
    def test_get_signup_student_form(self):
        response = self.client.get(reverse('signup_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup_student.html')
        self.assertIsInstance(response.context['form'], UserRegisterStu1Form)

    def test_post_valid_signup_student(self):
        user = User.objects.create_user(username='auth_user', password='pass123')
        response = self.client.post(reverse('signup_student'), {
            'username': 'teststu',
            'email': 'test@student.com',
            'password': '12345678',
            'first_name': 'Test',
            'last_name': 'Student',
            'user': user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserRegisterStu1.objects.filter(username='teststu').exists())


class GradeImprovementRequestTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student1', password='pass123')
        UserRegisterStu1.objects.create(
            user=self.user,
            username='student1',
            email='student1@email.com',
            password='12345678',
            first_name='Test',
            last_name='Student'
        )

    def test_post_grade_request_authenticated(self):
        self.client.login(username='student1', password='pass123')
        response = self.client.post(reverse('request_form'), {
            'course_name': 'Math',
            'current_grade': 60,
            'desired_grade': 85,
            'reason': 'Improved performance',
            'email': 'student1@email.com',
            'username': 'student1'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(GradeImprovementRequest.objects.exists())

    def test_post_grade_request_unauthenticated(self):
        response = self.client.post(reverse('request_form'), {
            'course_name': 'Math',
            'current_grade': 60,
            'desired_grade': 85,
            'reason': 'Improved performance'
        })
        self.assertEqual(response.status_code, 302)


class TimeExtensionRequestTests(TestCase):
    def test_submit_time_extension_valid(self):
        file = SimpleUploadedFile("support.pdf", b"test content")
        response = self.client.post(reverse('request_time_extension'), {
            'student_name': 'TimeTester',
            'email': 'time@test.com',
            'subject': 'Algorithms',
            'original_deadline': '2025-06-01',
            'requested_extension_time': 3,
            'reason_for_extension': 'Medical reason',
            'supporting_documents': file,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(TimeExtensionRequest.objects.filter(student_name='TimeTester').exists())


class SuccessViewTests(TestCase):
    def test_success_page_status_code(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request_success.html')
