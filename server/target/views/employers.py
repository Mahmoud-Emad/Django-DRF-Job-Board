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
from server.target.api.permission import IsEmployer
from server.target.api.response import CustomResponse
from server.target.models.user import Employer, UserType

from server.target.serializers.employers import EmployersRegistrationSerializer
from server.target.serializers.jobs import JobDetailSerializers, JobSearchSerializers
from server.target.services.user import get_employer_by_id
from server.target.services.jobs import get_jobs_based_on_employer, get_job_by_id
from server.target.utils.enc_password import encode_password







class EmployersRegistrationAPIView(GenericAPIView):
    """register a new employer endpoint"""
    serializer_class = EmployersRegistrationSerializer
    def post(self, request:Request) -> Response:
        """
        By using this endpoint you'll register as a employers => Employer
        """
        serializer:Dict = EmployersRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            password:str = serializer.validated_data.get('password')
            en_password: str = encode_password(password)
            
            serializer.save(user_type = UserType.EMPLOYER, password = en_password)
            data:Dict = serializer.data
            del data["password"]
            del data["user_type"]

            user_group, created = Group.objects.get_or_create(name='Employers')
            user:Employer = Employer.objects.get(email=data["email"])
            user_group.user_set.add(user)

            return CustomResponse.success(
                data=data,
                message="Employer created successfully.",
                status_code=HTTP_201_CREATED
            )
        return CustomResponse.bad_request(error=serializer.errors)


class EmployersDetailsView(GenericAPIView):
    """employers CRUDs for employers users"""
    serializer_class = EmployersRegistrationSerializer

    def get(self, request:Request, id:int) -> Response:
        """This endpoint will return a single employer by passing its id"""
        user:Employer = get_employer_by_id(int(id))
        user_data:Dict = EmployersRegistrationSerializer(user).data
        
        del user_data["password"]
        if user is not None:
            return CustomResponse.success(
                message="Success Response",
                data=user_data,
                status_code=HTTP_200_OK
            )
        return CustomResponse.not_found(message = f"User with id {id} not found.")


class EmployerHandlerAPIView(GenericAPIView):
    """This class allows you to delete, update your account"""
    serializer_class = EmployersRegistrationSerializer
    permission_classes = [IsEmployer]

    def put(self, request:Request, id:int) -> Response:
        """
        Update employer endpoint
        You can use this endpoint when you want to Update your employer account
        """
        user:Employer = get_employer_by_id(int(id))
        if user is not None:
            if user.id == request.user.id:
                serializer = EmployersRegistrationSerializer(user, data = request.data)
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
        Delete employer endpoint
        You can use this endpoint when you want to Delete your employer account
        """
        user:Employer = get_employer_by_id(int(id))
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
    permission_classes = [IsEmployer]

    def get(self, request:Request) -> Response:
        """
        As a job seeker you can use this endpoint to get all of jobs that you applied,
        """
        employer = get_employer_by_id(request.user.id)
        jobs = get_jobs_based_on_employer(int(employer.id))
        if jobs is not None and employer:
            return CustomResponse.success(data=JobDetailSerializers(jobs, many=True).data)
        return CustomResponse.success()


class CloseJobAPIView(GenericAPIView):
    """Job-seekers can use this endpoint to apply on work"""
    permission_classes = [IsEmployer]
    def put(self, request:Request, job_id:str) -> Response:
        """
        As a employer you can use this endpoint to close jobs,
        id => id of job
        """
        job = get_job_by_id(int(job_id))
        employer = get_employer_by_id(request.user.id)
        if job:
            if job.company.id == employer.id:
                job.closed = True
                job.save()
                return CustomResponse.success(
                    message="Job was closed successfully.",
                    data=JobSearchSerializers(job).data
                )
            return CustomResponse.bad_request(
                message="You don't have permission to perform this action",
                status_code=HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )
        return CustomResponse.not_found("Job not found.")