from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_200_OK

from server.target.serializers.user import UserDetailSerializer
from server.target.services.user import get_user_by_id
from server.target.api.response import CustomResponse
from server.target.models.user import User



class UserDetailAPIView(GenericAPIView):
    """Return user object"""
    serializer_class = UserDetailSerializer
    def get(self, request: Request, id: int) -> Response:
        """This endpoint return any user with any type by passing id of user"""
        user:User = get_user_by_id(int(id))
        if user is not None:
            return CustomResponse.success(
                data=UserDetailSerializer(user).data,
                message="User created successfully.",
                status_code=HTTP_200_OK
            )
        return CustomResponse.not_found(message = f"User with id {id} not found.")