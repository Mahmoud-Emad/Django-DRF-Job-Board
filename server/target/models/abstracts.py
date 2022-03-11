from django.db import models


class TimeStampedModel(models.Model):
    """
    database model for created at and updated at fields
    """
    created  = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True