from django.urls import path,include

from server.target.views.jobs import (
    JobSearchAPIView,
    JobDetailAPIView,
    TopCompaniesAPIView,
    MostRecentJobsAPIView,
    ApplyOnJobAPIView,
)
from server.target.views.jobs import (
    PostNewJobAPIView,
)


urlpatterns = [
    path('', include([
        path('create/', PostNewJobAPIView.as_view()),
        path('detail/<int:id>/', JobDetailAPIView.as_view()),
        path('recent/', MostRecentJobsAPIView.as_view()),
        path('top-companies/', TopCompaniesAPIView.as_view()),
        path('search/<str:search_field>/', JobSearchAPIView.as_view()),
        path('apply/<int:job_id>/', ApplyOnJobAPIView.as_view()),
    ]))
]
