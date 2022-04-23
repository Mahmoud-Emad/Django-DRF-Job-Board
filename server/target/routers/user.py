from django.urls import path,include

from server.target.views.user import UserDetailAPIView




urlpatterns = [
    path('', include([
        path('<int:id>/', UserDetailAPIView.as_view()),
    ]))
]