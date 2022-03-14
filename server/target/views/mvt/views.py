from django.shortcuts import render






def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def top_companies(request):
    return render(request, 'top-companies.html')

def company_detail(request, id:str):
    return render(request, 'company-details.html')