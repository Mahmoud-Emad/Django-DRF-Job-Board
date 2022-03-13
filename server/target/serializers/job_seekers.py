from rest_framework.serializers import ModelSerializer
from server.target.models.user import JobSeeker





class JobSeekerRegistrationSerializer(ModelSerializer):
    """JobSeekers registration serializer class"""
    class Meta:
        model = JobSeeker
        fields = [
            'email', 'first_name', 'last_name', 'password',
            "phone", "description","user_type","country", "city"
        ]
        read_only_fields = ("user_type",)

class JobSeekerDetailForEmployerSerializer(ModelSerializer):
    """
    This class will use when employer want see basic information about the job seeker
    """
    class Meta:
        model = JobSeeker
        fields = [
            'email', 'full_name', "phone", "description"
        ]
        read_only_fields = ("user_type",)