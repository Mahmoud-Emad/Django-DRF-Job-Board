from django.urls import path,include

from server.target.views.mvt.views import *



urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('top-companies/', top_companies, name='top_companies'),
    path('companies/<str:id>/', company_detail, name='company_detail'),
]