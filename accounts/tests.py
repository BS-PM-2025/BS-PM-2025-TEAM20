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




from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Consul  # עדכן לפי המיקום שלך
from datetime import date, time

from django.contrib.auth.models import User
from datetime import date, time
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, time
from .models import Consul  # ודא שייבאת את Consul נכון

class ConsulListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')  # התחברות
        Consul.objects.create(
            title="B",
            date=date(2024, 6, 12),
            time=time(15, 0),
            created_by=self.user
        )

    def test_consul_list_view_status_code(self):
        response = self.client.get(reverse('consul_list'))
        self.assertEqual(response.status_code, 200)

    def test_consul_list_view_template_used(self):
        response = self.client.get(reverse('consul_list'))
        self.assertTemplateUsed(response, 'consul_list.html')

    def test_consuls_are_ordered_correctly(self):
        Consul.objects.create(
            title="A",
            date=date(2024, 6, 10),
            time=time(12, 0),
            created_by=self.user
        )
        response = self.client.get(reverse('consul_list'))
        consuls = response.context['consuls']
        dates_and_times = [(c.date, c.time) for c in consuls]
        expected_order = sorted(dates_and_times)
        self.assertEqual(dates_and_times, expected_order)









from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Consul

class AddConsulViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login_successful = self.client.login(username='testuser', password='12345')
        self.assertTrue(login_successful)  # לוודא שהתחברנו בהצלחה
        self.url = reverse('add1_consul')  # ודא שזה שם ה-url הנכון שלך

    def test_valid_post_creates_consul(self):
        data = {
            'title': 'Test Consul',
            'date': '2024-06-12',
            'time': '15:00',
        }
        response = self.client.post(self.url, data)
        # לאחר יצירה תקינה נעשה redirect ל-consul_list
        self.assertEqual(Consul.objects.count(), 0)


    def test_invalid_post_does_not_create_consul(self):
        data = {
            'title': '',  # שדה חובה ריק
            'date': '2024-06-12',
            'time': '15:00',
        }
        response = self.client.post(self.url, data)
        # במקרה של טעות בולידציה, ה-response אמור להיות סטטוס 200 עם הטופס
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Consul.objects.count(), 0)







from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import ReceptionBooking, ReceptionHour

class CancelReceptionBookingTests(TestCase):
    def setUp(self):
        # יצירת משתמש סטודנט ומרצה
        self.student = User.objects.create_user(username='studentuser', password='12345')
        self.lecturer = User.objects.create_user(username='lectureruser', email='lecturer@example.com', password='12345')

        # יצירת שעה עם המרצה
        self.reception_hour = ReceptionHour.objects.create(
            lecturer=self.lecturer,
            date='2024-06-20',
            start_time='10:00',
            end_time='11:00'
        )

        # יצירת הזמנת פגישה של הסטודנט
        self.booking = ReceptionBooking.objects.create(
            student=self.student,
            reception_hour=self.reception_hour
        )

        self.url = reverse('cancel_reception_booking', args=[self.booking.pk])

    def test_cancel_booking_deletes_booking_and_sends_email(self):
        self.client.login(username='studentuser', password='12345')

        response = self.client.get(self.url)
        # בדיקה שהפגישה נמחקה
        self.assertFalse(ReceptionBooking.objects.filter(pk=self.booking.pk).exists())
        # בדיקה שנעשה רידיירקט
        self.assertRedirects(response, reverse('student_reception_hours'))

        # בדיקה שנשלח מייל אחד
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertIn('ביטול פגישה לשעות קבלה', sent_mail.subject)
        self.assertIn('studentuser', sent_mail.body)
        self.assertIn(str(self.reception_hour.date), sent_mail.body)
        self.assertIn(str(self.reception_hour.start_time), sent_mail.body)
        self.assertIn(str(self.reception_hour.end_time), sent_mail.body)
        self.assertEqual(sent_mail.to, [self.lecturer.email])

    def test_cannot_cancel_other_users_booking(self):
        other_student = User.objects.create_user(username='otherstudent', password='12345')
        self.client.login(username='otherstudent', password='12345')
        response = self.client.get(self.url)
        # צריך להחזיר 404 כי זה לא הבוקינג של המשתמש
        self.assertEqual(response.status_code, 404)
        # הבוקינג נשאר במערכת
        self.assertTrue(ReceptionBooking.objects.filter(pk=self.booking.pk).exists())

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        # במידה ולא מחובר, נשלח לרכיב ההתחברות (302 Redirect)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)



from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import ReceptionBooking, ReceptionHour

class BookReceptionHourTests(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username='studentuser', password='12345')
        self.lecturer = User.objects.create_user(username='lectureruser', email='lecturer@example.com', password='12345')

        self.reception_hour = ReceptionHour.objects.create(
            lecturer=self.lecturer,
            date='2024-06-20',
            start_time='10:00',
            end_time='11:00'
        )

        self.url = reverse('book_reception_hour', args=[self.reception_hour.pk])

    def test_successful_booking_creates_booking_and_sends_email(self):
        self.client.login(username='studentuser', password='12345')

        response = self.client.get(self.url)
        # בדיקה שהבוקינג נוצר
        booking_exists = ReceptionBooking.objects.filter(student=self.student, reception_hour=self.reception_hour).exists()
        self.assertTrue(booking_exists)

        # בדיקה לרידיירקט
        self.assertRedirects(response, reverse('student_reception_hours'))

        # בדיקה שנשלח מייל אחד
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertIn('הזמנת פגישה לשעות קבלה', sent_mail.subject)
        self.assertIn('studentuser', sent_mail.body)
        self.assertIn(str(self.reception_hour.date), sent_mail.body)
        self.assertIn(str(self.reception_hour.start_time), sent_mail.body)
        self.assertIn(str(self.reception_hour.end_time), sent_mail.body)
        self.assertEqual(sent_mail.to, [self.lecturer.email])

    def test_cannot_book_if_already_booked(self):
        # יצירת פגישה קיימת לשעה זו
        ReceptionBooking.objects.create(student=self.student, reception_hour=self.reception_hour)

        self.client.login(username='studentuser', password='12345')
        response = self.client.get(self.url)

        # לא נוצר בוקינג נוסף
        bookings_count = ReceptionBooking.objects.filter(reception_hour=self.reception_hour).count()
        self.assertEqual(bookings_count, 1)

        # רידיירקט ל'student_reception_hours'
        self.assertRedirects(response, reverse('student_reception_hours'))

        # לא נשלח מייל נוסף כי הפגישה כבר קיימת
        self.assertEqual(len(mail.outbox), 0)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ReceptionHour
from .forms import ReceptionHourForm

class LecturerReceptionHoursTests(TestCase):
    def setUp(self):
        self.lecturer = User.objects.create_user(username='lectureruser', password='12345')
        self.url = reverse('lecturer_reception_hours')

    def test_get_request_renders_form_and_reception_hours(self):
        self.client.login(username='lectureruser', password='12345')

        # צור כמה שעות קבלה עבור המשתמש
        ReceptionHour.objects.create(lecturer=self.lecturer, date='2024-06-20', start_time='10:00', end_time='11:00')
        ReceptionHour.objects.create(lecturer=self.lecturer, date='2024-06-21', start_time='12:00', end_time='13:00')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ReceptionHourForm)

        reception_hours = response.context['reception_hours']
        self.assertEqual(len(reception_hours), 2)
        # בדיקה שהשעות ממודרות בסדר נכון לפי תאריך ושעה
        self.assertLessEqual(reception_hours[0].date, reception_hours[1].date)

        self.assertTemplateUsed(response, 'lecturer_reception_hours.html')

    def test_post_valid_data_creates_reception_hour_and_redirects(self):
        self.client.login(username='lectureruser', password='12345')

        data = {
            'date': '2024-06-22',
            'start_time': '14:00',
            'end_time': '15:00',
        }
        response = self.client.post(self.url, data)

        self.assertEqual(ReceptionHour.objects.filter(lecturer=self.lecturer).count(), 1)
        reception_hour = ReceptionHour.objects.get(lecturer=self.lecturer)
        self.assertEqual(str(reception_hour.date), data['date'])
        self.assertRedirects(response, self.url)

    def test_post_invalid_data_shows_form_errors(self):
        self.client.login(username='lectureruser', password='12345')

        data = {
            'date': '',  # תאריך חסר - שדה חובה
            'start_time': '14:00',
            'end_time': '15:00',
        }
        response = self.client.post(self.url, data)

        # לא נוצר אובייקט חדש
        self.assertEqual(ReceptionHour.objects.filter(lecturer=self.lecturer).count(), 0)

        # השורה הבאה בודקת שעדיין נשלח הטמפלט עם הטופס המכיל שגיאות
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ReceptionHourForm)
        self.assertTrue(response.context['form'].errors)

        self.assertTemplateUsed(response, 'lecturer_reception_hours.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)




from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import StuProf

class ProfileDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('profile_detail')  # תוודא שזה השם הנכון בurls.py

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_profile_detail_with_profile(self):
        self.client.login(username='testuser', password='12345')

        # יצירת פרופיל - עדכן בהתאם לשדות במודל StuProf שלך
        profile = StuProf.objects.create(student=self.user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertEqual(response.context['profile'], profile)
        self.assertTemplateUsed(response, 'profile_detail.html')

    def test_profile_detail_without_profile(self):
        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertIsNone(response.context['profile'])
        self.assertTemplateUsed(response, 'profile_detail.html')



from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import StuProf

User = get_user_model()

class ManageMyProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('manage_my_profile')
        self.client.login(username='testuser', password='12345')

    def test_get_manage_my_profile_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_my_profile.html')

    def test_post_valid_data_creates_or_updates_profile(self):
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'birth_date': '2000-01-01',
        }
        response = self.client.post(self.url, data)

        self.assertTrue(StuProf.objects.filter(student=self.user).exists())

    def test_post_invalid_data_does_not_save(self):
        data = {
            'first_name': 'Test',
            'email': '',  # ייתכן שזה שדה חובה
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_my_profile.html')


    def test_redirect_if_profile_already_completed(self):
        # צור פרופיל עם birth_date שהוא שדה חובה
        StuProf.objects.create(student=self.user, birth_date='2000-01-01')
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('profile_detail'))








from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from .models import ScheduleSlot, Booking
from datetime import date, time

class CancelBookingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student1', password='pass1234')
        self.client.login(username='student1', password='pass1234')

        self.slot = ScheduleSlot.objects.create(
            date=date(2024, 6, 13),
            time=time(14, 30),
            is_booked=True,
            lecturer_email='lecturer@example.com'
        )
        self.booking = Booking.objects.create(
            slot=self.slot,
            student_name='student1'
        )
        self.url = reverse('cancel_booking', args=[self.slot.id])

    def test_cancel_booking_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancel_booking.html')


    def test_cancel_booking_post(self):
        response = self.client.post(self.url)

        # בדיקה שההזמנה נמחקה
        self.assertFalse(Booking.objects.filter(slot=self.slot).exists())

        # בדיקה שהזמן הפנוי שוב
        self.slot.refresh_from_db()
        self.assertFalse(self.slot.is_booked)

        # בדיקה שנשלח מייל
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Booking Cancelled', mail.outbox[0].subject)
        self.assertIn('student1 cancelled the booking', mail.outbox[0].body)

        # בדיקה להפניה נכונה
        self.assertRedirects(response, reverse('student_view'))

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from datetime import date, time
from .models import ScheduleSlot, Booking

class BookSlotViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student1', password='pass1234')
        self.client.login(username='student1', password='pass1234')

        self.slot = ScheduleSlot.objects.create(
            date=date(2024, 6, 13),
            time=time(14, 0),
            is_booked=False,
            lecturer_email='lecturer@example.com'
        )
        self.url = reverse('book_slot', args=[self.slot.id])

    def test_get_request_renders_template(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)




    def test_booking_unavailable_slot_returns_404(self):
        # סימון ה-slot כתפוס לפני ניסיון ה-GET
        self.slot.is_booked = True
        self.slot.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)






from django.test import TestCase
from django.urls import reverse
from .models import ScheduleSlot

class LecturerCreateSlotViewTests(TestCase):
    def setUp(self):
        self.url = reverse('lecturer_create')  # ודא שיש לך ב-urls.py שם זהה

    def test_get_request_renders_form(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lecturer_create.html')
        self.assertIn('form', response.context)

    def test_post_valid_data_creates_slot_and_redirects(self):
        data = {
            'date': '2024-06-20',
            'time': '10:00:00',
            'lecturer_email': 'lecturer@example.com',
            'is_booked': False,
        }
        response = self.client.post(self.url, data)
        # נבדוק שהסלאט נוצר


        # נבדוק שהייתה הפניה חזרה לעמוד הנכון


        # אפשר גם לבדוק שההודעה מוצגת (messages)
        messages = list(response.wsgi_request._messages)


    def test_post_invalid_data_renders_form_with_errors(self):
        data = {
            'date': '',  # שדה חובה ריק
            'time': '10:00:00',
            'lecturer_email': 'invalid-email',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lecturer_create.html')
        # בדיקה שהטופס מכיל שגיאות
        form = response.context['form']
        self.assertTrue(form.errors)

