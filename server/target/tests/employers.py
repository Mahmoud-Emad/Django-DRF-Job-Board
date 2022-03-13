from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import Group

from server.target.models import *


client = APIClient()


class EmployerTests(APITestCase):
    """
    Since we are focusing on API testing,
    i'll create test cases for all Employer features
    """
    def setUp(self):
        """Setup local database objects"""
        employer, created = Employer.objects.get_or_create(
            email = 'test@employer.target',first_name = 'Mahmoud',
            last_name = 'Emad',password ='0000',
            company_name = 'TestCompany'
        )
        self.employer = employer
        job, created = Job.objects.get_or_create(
            title= "EX-Chief",experience= 5,
            country= "EG",city= "Giza",
            job_type= "Full Time",description= "Some",
            company = self.employer
        )
        self.job = job
        user_group, created = Group.objects.get_or_create(name='Employers')
        user_group.user_set.add(self.employer)
        self.access_token = self.get_token()
        self.headers = client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def get_token(self):
        """Get token for employer user."""
        url = f'/api/auth/sign-in/'
        data = {'email': self.employer.email,'password': self.employer.password}
        response = client.post(url, data, format='json')
        return response.data['Data']['access_token']

    def test_login_employer(self):
        """
        Ensure we can login as employer user.
        """
        url = f'/api/auth/sign-in/'
        data = {
            'email': self.employer.email,
            'password': self.employer.password
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['Data']['access_token']
    
    def test_register_new_employer(self) -> Employer:
        """
        Ensure we can register a new employer account.
        """
        url = f'/api/employers/register/'
        data = {
            'email': 'test_@employer.target',
            'first_name': 'Mahmoud',
            'last_name': 'Emad',
            'password':'0000',
            'company_name': 'TestCompany',
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employer_by_id(self) -> Employer:
        """
        Ensure we can get an employer account.
        """
        if self.employer:
            url = f'/api/employers/{self.employer.id}/'
            response = client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employer_by_id(self) -> Employer:
        """
        Ensure we can update an employer account.
        """
        if self.employer:
            url = f'/api/employers/action/{self.employer.id}/'
            data = {
                'email': 'updated@employer.target',
                'first_name': 'Mahmoud',
                'last_name': 'Emad',
                'password':'0000',
                'company_name': 'TestCompany',
            }
            response = client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_employer_by_id(self) -> Employer:
        """
        Ensure we can delete an employer account.
        """
        if self.employer:
            url = f'/api/employers/action/{self.employer.id}/'
            response = client.delete(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_employer_jobs(self) -> Employer:
        """
        Ensure we can get an employer account.
        """
        if self.employer:
            url = f'/api/employers/applications/'
            response = client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_close_employer_job(self) -> Employer:
        """
        Ensure we can close job by employer account.
        """
        if self.employer:
            url = f'/api/employers/close-job/{self.job.id}/'
            response = client.put(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_employer_jobs(self) -> Employer:
        """
        Ensure we can post a new job by employer account.
        """
        if self.employer:
            url = f'/api/jobs/create/'
            data = {
                "title": "EX-Chief",
                "experience": 5,
                "country": "EG",
                "city": "Giza",
                "job_type": "Full Time",
                "description": "Some"
            }
            response = client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FakeEmployerTests(APITestCase):
    def create_fake_employer(self) -> Employer:
        """
        Ensure we can register a new employer account.
        """
        url = f'/api/employers/register/'
        data = {
            'email': 'test_fake@employer.target',
            'first_name': 'Mahmoud',
            'last_name': 'Emad',
            'password':'0000',
            'company_name': 'TestCompany',
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['Data']['email']