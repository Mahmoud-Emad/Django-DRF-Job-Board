from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import Group

from server.target.models import *
from server.target.tests.employers import FakeEmployerTests
from server.target.services.user import get_employer_by_email


client = APIClient()


class JobSeekerTests(APITestCase):
    """
    Since we are focusing on API testing,
    i'll create test cases for all JobSeeker features
    """
    def setUp(self):
        """Setup local database objects"""
        job_seeker, created = JobSeeker.objects.get_or_create(
            email = 'test@jobseeker.target',first_name = 'Mahmoud',
            last_name = 'Emad',password ='000000000',
            country = "EG", city = "Giza"
        )
        self.job_seeker = job_seeker
        
        employer_test_class = FakeEmployerTests()
        self.employer = get_employer_by_email(employer_test_class.create_fake_employer())
        
        job, created = Job.objects.get_or_create(
            title= "EX-Chief",experience= 5,
            country= "EG",city= "Giza",
            job_type= "Full Time",description= "Some",
            company = self.employer
        )
        self.job = job

        job_seeker_group, created = Group.objects.get_or_create(name='Job-Seekers')
        job_seeker_group.user_set.add(self.job_seeker)
        
        self.access_token = self.get_token()
        self.headers = client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
    
    def create_fake_job(self):
        """
        Create a job obj in database to use it outside this file
        """
        job, created = Job.objects.get_or_create(
            title= "EX-Chief",experience= 5,
            country= "EG",city= "Giza",
            job_type= "Full Time",description= "Some",
            company = self.employer
        )
        return job if job else None

    def get_token(self):
        """Get token for job-seeker user."""
        url = f'/api/auth/sign-in/'
        data = {'email': self.job_seeker.email,'password': self.job_seeker.password}
        response = client.post(url, data, format='json')
        return response.data['data']['access_token']

    def test_login_job_seeker(self):
        """
        Ensure we can login as job-seeker user.
        """
        url = f'/api/auth/sign-in/'
        data = {
            'email': self.job_seeker.email,
            'password': self.job_seeker.password
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['data']['access_token']

    def test_register_new_job_seeker(self) -> JobSeeker:
        """
        Ensure we can register a new job-seeker account.
        """
        url = f'/api/job-seekers/register/'
        data = {
            'email': 'test_2@employer.target',
            "first_name": "Mahmoud",
            "last_name": "Emad",
            "password": "000000000",
            "country": "EG",
            "city": "Giza"
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_job_seeker_by_id(self) -> JobSeeker:
        """
        Ensure we can get an job-seeker account.
        """
        if self.job_seeker:
            url = f'/api/job-seekers/{self.job_seeker.id}/'
            response = client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_job_seeker_by_id(self) -> JobSeeker:
        """
        Ensure we can update an job-seeker account.
        """
        if self.job_seeker:
            url = f'/api/job-seekers/action/{self.job_seeker.id}/'
            data = {
                "email": "updated@employer.target",
                "first_name": "Mahmoud",
                "last_name": "Emad",
                "password": "000000000",
                "country": "EG",
                "city": "Giza"
            }
            response = client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_delete_employer_by_id(self) -> JobSeeker:
        """
        Ensure we can delete an job-seeker account.
        """
        if self.job_seeker:
            url = f'/api/job-seekers/action/{self.job_seeker.id}/'
            response = client.delete(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_job_seeker_apply_to_job(self) -> JobSeeker:
        """
        Ensure we can apply on job by current job-seeker account.
        """
        if self.job_seeker:
            url = f'/api/jobs/apply/{self.job.id}/'
            response = client.post(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_seeker_applications(self) -> JobSeeker:
        """
        Ensure we can get all of applications that applied by current job-seeker account.
        """
        if self.job_seeker:
            url = '/api/job-seekers/applications/'
            response = client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
