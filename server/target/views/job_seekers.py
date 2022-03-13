from typing import Dict

from django.contrib.auth.models import Group

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    HTTP_204_NO_CONTENT,
)

from server.target.serializers.job_seekers import JobSeekerRegistrationSerializer
from server.target.serializers.jobs import JobSearchSerializers
from server.target.api.permission import IsJobSeekers
from server.target.api.response import CustomResponse
from server.target.models.user import JobSeeker, UserType
from server.target.services.user import get_job_seeker_by_id
from server.target.utils.enc_password import encode_password
from server.target.services.jobs import get_jobs_based_on_job_seeker






class JobSeekerRegistrationAPIView(GenericAPIView):
    """register a new user endpoint"""
    serializer_class = JobSeekerRegistrationSerializer
    def post(self, request:Request) -> Response:
        """
        By using this endpoint you'll register as a job seeker
        """
        serializer:Dict = JobSeekerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            password:str = serializer.validated_data.get('password')
            en_password: str = encode_password(password)

            serializer.save(
                user_type = UserType.JOB_SEEKER,
                password = en_password
            )
            data: Dict = serializer.data

            del data["password"]
            del data["user_type"]

            user_group, created  = Group.objects.get_or_create(name='Job-Seekers')
            user:JobSeeker = JobSeeker.objects.get(email=data["email"])
            user_group.user_set.add(user)

            return CustomResponse.success(
                data=data,
                message="User created successfully.",
                status_code=HTTP_201_CREATED
            )
        return CustomResponse.bad_request(error=serializer.errors)


class JobSeekerDetailsView(GenericAPIView):
    """Job seekers CRUDs for job-seekers users"""
    serializer_class = JobSeekerRegistrationSerializer
    
    def get(self, request:Request, id:int) -> Response:
        """This endpoint will return a single job-seeker by passing its id"""
        user:JobSeeker = get_job_seeker_by_id(int(id))
        user_data:Dict = JobSeekerRegistrationSerializer(user).data
        
        del user_data["password"]
        if user is not None:
            return CustomResponse.success(
                message="Success Response",
                data=user_data,
                status_code=HTTP_200_OK
            )
        return CustomResponse.not_found(message = f"User with id {id} not found.")


class JobSeekerHandlerAPIView(GenericAPIView):
    """This class allows you to delete, update your account"""
    serializer_class = JobSeekerRegistrationSerializer
    permission_classes = [IsJobSeekers]

    def put(self, request:Request, id:int) -> Response:
        """
        Update Job-Seeker endpoint
        You can use this endpoint when you want to Update your Job-Seeker account
        """
        user:JobSeeker = get_job_seeker_by_id(int(id))
        if user is not None:
            if user.id == request.user.id:
                serializer = JobSeekerRegistrationSerializer(user, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse.success(
                        message="User updated successfully",
                        data=serializer.data,
                        status_code=HTTP_202_ACCEPTED
                    )
                return CustomResponse.bad_request(message = "Cant Update User", error = serializer.errors)
            return CustomResponse.bad_request(
                message="You don't have permission to perform this action",
                status_code=HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )
        return CustomResponse.not_found(message = f"User with id {id} not found.")
    
    def delete(self, request:Request, id:int) -> Response:
        """
        Delete Job-Seeker endpoint
        You can use this endpoint when you want to Delete your Job-Seeker account
        """
        user:JobSeeker = get_job_seeker_by_id(int(id))
        if user is not None:
            if user.id == request.user.id:
                user.delete()
                return CustomResponse.success(
                    status_code=HTTP_204_NO_CONTENT
                )
            return CustomResponse.bad_request(
                message="You don't have permission to perform this action",
                status_code=HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )
        return CustomResponse.not_found(message = f"User with id {id} not found.")


class MyJobsApplicationsAPIView(APIView):
    """Job-seekers can use this endpoint to get jobs who was applied on"""
    permission_classes = [IsJobSeekers]

    def get(self, request:Request) -> Response:
        """
        As a job seeker you can use this endpoint to get all of jobs that you applied,
        """
        job_seeker = get_job_seeker_by_id(request.user.id)
        jobs = get_jobs_based_on_job_seeker(int(job_seeker.id))
        if jobs is not None and job_seeker:
            return CustomResponse.success(data=JobSearchSerializers(jobs, many=True).data)
        return CustomResponse.success()