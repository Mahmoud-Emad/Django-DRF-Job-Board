from django_countries.fields import CountryField
from django.db import models

from server.target.models.abstracts import TimeStampedModel
from server.target.models.user import Employer, JobSeeker
from server.target.utils.intger_range_field import IntegerRangeField



class JobType(models.TextChoices):
    """Enum model"""
    FULL_TIME   = 'Full Time', 'Full Time'
    PART_TIME   = 'Part Time', 'Part Time'
    FREELANCE   = 'Freelance', 'Freelance'


class Job(TimeStampedModel):
    """Job table"""
    company     = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='job_employer')
    title       = models.CharField(max_length=250)
    experience  = IntegerRangeField(default=0, min_value=0, max_value=20)
    country     = CountryField()
    city        = models.CharField(max_length=30)
    job_type    = models.CharField(max_length=30, choices=JobType.choices, default=None)
    description = models.TextField(max_length=255)
    closed      = models.BooleanField(default=False)
    applied_users = models.ManyToManyField(JobSeeker, related_name='applied_users', blank=True)
    
    def __str__(self) -> str:
        """String method"""
        return self.title

    @property
    def company_name(self):
        return self.company.company_name

    @property
    def fullname(self):
        return self.company.full_name
    
    @property
    def created_at(self):
        return self.created

    @property
    def job_title(self):
        return self.title if len(self.title) < 50 else self.title[:50]