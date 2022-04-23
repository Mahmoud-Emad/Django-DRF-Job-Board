from rest_framework.serializers import ModelSerializer

from server.target.models.user import User



class UserDetailSerializer(ModelSerializer):
    """User serializer class"""
    class Meta:
        model = User
        fields = [
            "user_type"
        ]