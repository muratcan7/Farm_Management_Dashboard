
# from django.test import TestCase
# from .models import Livestock
# from datetime import date

# class LivestockModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up data for the whole TestCase
#         Livestock.objects.create(
#             animal_type='Cow',
#             tag_number='12345',
#             breed='Angus',
#             age=24,
#             weight=500.00,
#             purchase_date=date(2020, 1, 1),
#             purchase_price=1500.00,
#             user_token='user123'
#         )

#     def test_age_in_months(self):
#         # Test the calculate_age_in_months method
#         livestock = Livestock.objects.get(tag_number='12345')
#         # You'll need to adjust the expected months based on the current date
#         expected_months = (date.today().year - livestock.purchase_date.year) * 12 + date.today().month - livestock.purchase_date.month
#         self.assertEqual(livestock.calculate_age_in_months(), expected_months)

# farm_management_app/tests.py

# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Crop
# from django.urls import reverse
# from datetime import date

# class CropViewSetTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create test data for crops
#         Crop.objects.create(
#             name='Tomato',
#             variety='Cherry',
#             planting_date=date(2023, 4, 1),
#             harvest_date=date(2023, 9, 30),
#             user_token='testtoken123'
#         )

#     def test_get_crops_list(self):
#         # Test to ensure we can get the list of crops
#         url = reverse('crop-list')  # This uses the 'name' parameter defined in your router.urls
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)  # Assuming there's only one crop in the test DB
#         self.assertEqual(response.data[0]['name'], 'Tomato')

# tests.py in your Django app

# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.contrib.auth.models import User

# class JWTAuthTestCase(APITestCase):
#     def setUp(self):
#         # Create a test user
#         self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
#         self.create_url = reverse('token_obtain_pair')

#     def test_create_token(self):
#         """
#         Ensure we can create a new token for a user.
#         """
#         data = {
#             'username': 'testuser',
#             'password': 'testpassword'
#         }
#         response = self.client.post(self.create_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue('access' in response.data)
#         self.assertTrue('refresh' in response.data)

#     def test_create_token_wrong_password(self):
#         """
#         Ensure token is not created if the wrong password is given.
#         """
#         data = {
#             'username': 'testuser',
#             'password': 'wrong'
#         }
#         response = self.client.post(self.create_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_create_token_no_user(self):
#         """
#         Ensure token is not created if the user does not exist.
#         """
#         data = {
#             'username': 'nouser',
#             'password': 'testpassword'
#         }
#         response = self.client.post(self.create_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from .models import Income

# class FinancialManagementAPITests(APITestCase):
#     def setUp(self):
#         # Create a user for authentication
#         self.user = User.objects.create_user(username='user', email='user@example.com', password='pass')
#         self.client.login(username='user', password='pass')

#         # URL for creating income entries
#         self.income_create_url = reverse('income-list')  # Adjust this if your URL name is different

#         # Sample income data
#         self.income_data = {
#             'description': 'Sale of crops',
#             'amount': 1200.00,
#             'date': '2023-04-01'
#         }

#     def test_create_income_valid(self):
#         """
#         Ensure we can create a new income record with valid data.
#         """
#         response = self.client.post(self.income_create_url, self.income_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Income.objects.count(), 1)
#         self.assertEqual(Income.objects.get().description, 'Sale of crops')

#     def test_create_income_invalid(self):
#         """
#         Ensure we cannot create a new income record with invalid data.
#         """
#         # Invalid data where amount is not a number
#         invalid_data = self.income_data.copy()
#         invalid_data['amount'] = "twelve hundred"
#         response = self.client.post(self.income_create_url, invalid_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(Income.objects.count(), 0)
