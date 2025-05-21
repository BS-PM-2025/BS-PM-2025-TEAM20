
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegisterStu1Form, UserRegisterLecForm, GradeImprovementRequestForm
from .models import UserRegisterStu1, UserRegisterLec, GradeImprovementRequest, TimeExtensionRequest
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
            'user': user.id  # ربط المستخدم بـ auth_user
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserRegisterStu1.objects.filter(username='teststu').exists())


from django.contrib.auth.models import User
from .models import UserRegisterStu1, UserRegisterLec
from django.urls import reverse
from django.test import TestCase

class SignupLecturerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='realuser', password='pass123')
        UserRegisterStu1.objects.create(
            user=self.user,
            username='realuser',
            email='realuser@email.com',
            password='pass123',
            first_name='Real',
            last_name='User'
        )

    def test_post_valid_signup_lec(self):
        response = self.client.post(reverse('signup_lec'), {
            'username': 'lectest',
            'email': 'lec@test.com',
            'password': '12345678',
            'first_name': 'Lecturer',
            'last_name': 'Test'
        })

        print("\nResponse content:", response.content.decode())

        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserRegisterLec.objects.filter(username='lectest').exists())


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
        self.assertEqual(response.status_code, 302)  # Redirect to login


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

from .models import StudentRequest, DocumentRequest, Feedback, OfficeHours11

class DocumentRequestTests(TestCase):
    def test_post_valid_document_request(self):
        response = self.client.post(reverse('submit_document_request'), {
            'student_name': 'Yaqeen',
            'student_email': 'yaqeen@example.com',
            'document_type': 'אישור לימודים',
            'additional_info': 'Need it for work'
        }, format='multipart')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(DocumentRequest.objects.filter(student_name='Yaqeen').exists())
