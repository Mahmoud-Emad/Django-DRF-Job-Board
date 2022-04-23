from typing import Optional
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST, 
    HTTP_404_NOT_FOUND
)


class CustomResponse:
    """Custom response methods"""

    @staticmethod
    def success(data: list = [], message: Optional[str] = None, status_code: Optional[int] = None) -> Response:
        """Http success response method including [CREATE, UPDATE, GET, DELETE]"""

        if not message:
            message = 'Success'
        if not status_code: 
            status_code = HTTP_200_OK

        return Response({
            'message' : message,
            'data':data,
            'status':status_code
        }, status = status_code)

    @staticmethod
    def not_found(message: Optional[str] = None, status_code: int = HTTP_404_NOT_FOUND) -> Response:
        """Http not found response method"""

        if not message: 
            message = 'Not Found'

        return Response({
            'message' : message,
            'status':status_code
        }, status = status_code)

    @staticmethod
    def bad_request(error: list = [], message: Optional[str] = None, data: list = [], status_code: int = HTTP_400_BAD_REQUEST) -> Response:
        """Http bad request method"""
        if not message:
            message = 'Make sure that you entered a valid data.'

        return Response({
            'message' : message,
            'data' : data,
            'error' : error,
            'status':status_code
        }, status = status_code)