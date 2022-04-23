from django.urls import path,include

from server.target.views.employers import (
    EmployersDetailsView,
    EmployerHandlerAPIView,
    EmployersRegistrationAPIView,
    MyJobsApplicationsAPIView,
    CloseJobAPIView
)



urlpatterns = [
    path('', include([
        path('register/', EmployersRegistrationAPIView.as_view()),
        path('applications/', MyJobsApplicationsAPIView.as_view()),
        path('close-job/<int:job_id>/', CloseJobAPIView.as_view()),
        path('<int:id>/', EmployersDetailsView.as_view()),
        path('action/<int:id>/', EmployerHandlerAPIView.as_view()),
    ]))
]