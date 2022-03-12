from django.urls import path,include

from server.target.views.job_seekers import (
    JobSeekerDetailsView,
    JobSeekerRegistrationAPIView,
    MyJobsApplicationsAPIView
)

urlpatterns = [
    path('', include([
        path('register/', JobSeekerRegistrationAPIView.as_view()),
        path('applications/', MyJobsApplicationsAPIView.as_view()),
        path('<int:id>/', JobSeekerDetailsView.as_view()),
    ]))
]