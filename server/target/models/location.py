from django.db import models
from server.target.models.abstracts import TimeStampedModel

class Location(TimeStampedModel):
    """Location table has [country and city] fields"""
    country = models.CharField(max_length=30)
    city    = models.CharField(max_length=30)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self) -> str:
        return f"{self.country} - {self.city}"