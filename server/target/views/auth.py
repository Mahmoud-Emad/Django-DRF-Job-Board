from typing import Dict

from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from server.target.services.user import get_user_by_email_for_login
from server.target.utils.auth import get_tokens_for_user, validate_email
from server.target.api.response import CustomResponse
from server.target.models.user import User
from server.target.serializers.auth import (
    LoginSerializer,
)

class LoginApiView(GenericAPIView):
    """Login endpoint"""
    serializer_class = LoginSerializer
    def post(self, request:Request) -> Response:
        """
        Just pass your email and password to generate a simpleJWT token
        """
        serializer: Dict = self.get_serializer(data=request.data)
        email: str = request.data.get('email')
        if serializer.is_valid() and validate_email(email):
            password: str = serializer.validated_data.get('password')
            user: User = get_user_by_email_for_login(email)
            if user is not None:
                if user.check_password(password) or user.password == password:
                    return CustomResponse.success(
                        message="Valid email in our system.",
                        data=get_tokens_for_user(user)
                    )
                return CustomResponse.bad_request(message = 'Wrong Credential!')
            return CustomResponse.not_found(message = 'There are no user with this email.')
        return CustomResponse.bad_request(error=serializer.errors)