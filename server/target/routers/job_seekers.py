from django.urls import path,include

from server.target.views.job_seekers import (
    JobSeekerDetailsView,
    JobSeekerHandlerAPIView,
    JobSeekerRegistrationAPIView,
    MyJobsApplicationsAPIView
)

urlpatterns = [
    path('', include([
        path('register/', JobSeekerRegistrationAPIView.as_view()),
        path('applications/', MyJobsApplicationsAPIView.as_view()),
        path('action/<int:id>/', JobSeekerHandlerAPIView.as_view()),
        path('<int:id>/', JobSeekerDetailsView.as_view()),
    ]))
]