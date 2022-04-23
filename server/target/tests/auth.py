from rest_framework import status
from rest_framework.test import APITestCase

from server.target.models.user import Employer, JobSeeker






class AuthenticationTests(APITestCase):
    """
    Since we are focusing on API testing,
    i'll create test cases for all features
    """
    def test_create_job_seeker_account(self) -> JobSeeker:
        """
        Ensure we can create a job-seeker account.
        """
        url = '/api/job-seekers/register/'
        data = {
            'email': 'test1@jobseeker.target',
            'first_name': 'Mahmoud',
            'last_name': 'Emad',
            'password':'000000000',
            'phone':'01027906014',
            'description':'Python Developer',
            'country': "EG",
            'city':'Giza'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employers_account(self) -> Employer:
        """
        Ensure we can create a employer account.
        """
        url = '/api/employers/register/'
        data = {
            'email': 'test2@employer.target',
            'first_name': 'Mahmoud',
            'last_name': 'Emad',
            'password':'000000000',
            'company_name': 'TestCompany',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)