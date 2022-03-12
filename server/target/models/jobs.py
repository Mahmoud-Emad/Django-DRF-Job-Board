from django_countries.fields import CountryField
from django.db import models

from server.target.models.abstracts import TimeStampedModel
from server.target.models.user import Employer, JobSeeker



class JobType(models.TextChoices):
    """Enum model"""
    FULL_TIME   = 'Full Time', 'Full Time'
    PART_TIME   = 'Part Time', 'Part Time'
    FREELANCE   = 'Freelance', 'Freelance'


class Job(TimeStampedModel):
    """Job table"""
    company     = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='job_employer')
    title       = models.CharField(max_length=50)
    experience  = models.IntegerField(default=0)
    country     = CountryField()
    city        = models.CharField(max_length=30)
    job_type    = models.CharField(max_length=30, choices=JobType.choices, default=None)
    description = models.TextField(max_length=255)
    closed      = models.BooleanField(default=False)
    applied_users = models.ManyToManyField(JobSeeker, related_name='applied_users')
    
    def __str__(self) -> str:
        """String method"""
        return self.title