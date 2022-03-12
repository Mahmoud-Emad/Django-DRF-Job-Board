from rest_framework.serializers import ModelSerializer, SerializerMethodField

from server.target.models.jobs import Job
from server.target.models.user import Employer, JobSeeker
from server.target.serializers.employers import EmployersCompanyInfoSerializer
from server.target.serializers.job_seekers import JobSeekerDetailForEmployerSerializer



class PostNewJobSerializers(ModelSerializer):
    """Serializer class to job table"""

    class Meta:
        model = Job
        exclude = ('created', 'modified','applied_users','closed')
        read_only_fields = ('company',)


class JobSearchSerializers(ModelSerializer):
    """Just serializer class to pass search field and return response."""
    company = SerializerMethodField()
    applied_users = SerializerMethodField()
    
    class Meta:
        model = Job
        exclude = ('modified',)

    def get_company(self, obj:Employer):
        """Get company information"""
        return EmployersCompanyInfoSerializer(obj.company).data

    def get_applied_users(self, obj:JobSeeker) -> int:
        """Get length of applied_users"""
        return obj.applied_users.count()


class JobDetailSerializers(ModelSerializer):
    """Serializer class to get who apply on employers jobs"""
    applied_users = SerializerMethodField()

    class Meta:
        model = Job
        exclude = ('modified',)

    def get_applied_users(self, obj:JobSeeker) -> int:
        """Get length of applied_users"""
        return JobSeekerDetailForEmployerSerializer(obj.applied_users.all(), many = True).data
