from rest_framework import status
from rest_framework.test import APITestCase, APIClient


from server.target.models import *
from server.target.tests.job_seekers import JobSeekerTests


client = APIClient()


class JobTests(APITestCase):
    """
    Since we are focusing on API testing,
    i'll create test cases for all Jobs features
    """
    def setUp(self):
        """Setup local database objects"""
        self.init = JobSeekerTests()
        return self.init.setUp()
    
    def test_recent_jobs(self) -> Job:
        """
        Ensure we can see the most recent jobs
        """
        url = '/api/jobs/recent/'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_top_companies(self) -> Job:
        """
        Ensure we can get top companies based on len(jobs)
        """
        url = "/api/jobs/top-companies/"
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search(self) -> Job:
        """
        Ensure that we can search about job
        """
        search_field = "python developer"
        url = f"/api/jobs/search/{search_field}/"
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_job_detail(self) -> Job:
        """
        Ensure that we can get job details
        """
        job = self.init.create_fake_job()
        url = f'/api/jobs/detail/{job.id}/'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        