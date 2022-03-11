from django.db import models

from server.target.models.abstracts import TimeStampedModel
from server.target.models.location import Location
from server.target.models.user import Company



class JobType(models.TextChoices):
    """Enum model"""
    FULL_TIME   = 'Full Time', 'Full Time'
    PART_TIME   = 'Part Time', 'Part Time'
    FREELANCE  = 'Freelance', 'Freelance'


class Job(TimeStampedModel):
    """Job table"""
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='job_location')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_company')
    title = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    job_type = models.CharField(max_length=30, choices=JobType.choices, default=None)

    def __str__(self) -> str:
        """String method"""
        return super().__str__(self.title)