from ast import Dict
from django.db.models import Q, Count

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
)

from server.target.serializers.jobs import PostNewJobSerializers, JobSearchSerializers, MustRecentJobsSerializer
from server.target.serializers.employers import TopCompaniesSerializer
from server.target.api.permission import IsJobSeekers
from server.target.api.response import CustomResponse
from server.target.api.permission import IsEmployer
from server.target.models.user import Employer
from server.target.models.jobs import Job
from server.target.services.user import get_employer_by_id
from server.target.services.user import get_job_seeker_by_id
from server.target.services.jobs import get_job_by_id


class PostNewJobAPIView(GenericAPIView):
    """Class post job for posting a new job and push it into database."""
    serializer_class = PostNewJobSerializers
    permission_classes = [IsEmployer]

    def post(self, request:Request) -> Response:
        """Only employers can access this endpoint, this will create a new job"""
        serializer = PostNewJobSerializers(data = request.data)
        if serializer.is_valid():
            employer:Employer = get_employer_by_id(request.user.id)
            serializer.save(company = employer)
            return CustomResponse.success(
                data=serializer.data,
                message="Job created successfully.",
                status_code=HTTP_201_CREATED
            )
        return CustomResponse.bad_request(error=serializer.errors)


class JobDetailAPIView(GenericAPIView):
    """You have to use this class when you need to know more about exact job"""
    serializer_class = JobSearchSerializers

    def get(self, request:Request, id:int) -> Response:
        """This endpoint will return a single job by passing its id"""
        job:Job = get_job_by_id(int(id))
        if job is not None:
            return CustomResponse.success(
                message="Success Response",
                data=JobSearchSerializers(job).data,
                status_code=HTTP_200_OK
            )
        return CustomResponse.not_found(message = f"Job with id {id} not found.")


class JobSearchAPIView(GenericAPIView):
    """Users can search about job by passing a title or keywords"""
    serializer_class = JobSearchSerializers

    def get(self, request:Request, search_field:str) -> Response:
        l_search_field = search_field.split()
        jobs = Job.objects.filter(
            Q(description__in = l_search_field) | Q(title__icontains = search_field)
        ).order_by('-created')
        serializer = JobSearchSerializers(jobs, many=True).data
        return CustomResponse.success(data=serializer)


class TopCompaniesAPIView(APIView):
    """
    Users can see the top companies (by number of jobs posted)
    """
    serializer_class = TopCompaniesSerializer
    def get(self, request:Request) -> Response:
        employers = Employer.objects.annotate(jobs=Count('job_employer')).order_by('-jobs')
        serializer = TopCompaniesSerializer(employers, many=True)
        return CustomResponse.success(data=serializer.data, message="Top companies based on jobs posted")

class MostRecentJobsAPIView(ListAPIView):
    """
    Users can see the most recent posted jobs ordered by [created] field
    """
    serializer_class = MustRecentJobsSerializer
    def get_queryset(self) -> Response:
        queryset = Job.objects.all().order_by('-created')
        return queryset


class ApplyOnJobAPIView(GenericAPIView):
    """Job-seekers can use this endpoint to apply on work"""
    permission_classes = [IsJobSeekers]
    def post(self, request:Request, job_id:str) -> Response:
        """
        As a job seeker you can use this endpoint to apply on any job,
        id => id of job
        """
        job = get_job_by_id(int(job_id))
        job_seeker = get_job_seeker_by_id(request.user.id)
        if job is not None and job_seeker:
            job.applied_users.add(job_seeker)
            job.save()
            return CustomResponse.success(message="Applied successfully.", data=JobSearchSerializers(job).data)
        return CustomResponse.not_found("Job not found.")