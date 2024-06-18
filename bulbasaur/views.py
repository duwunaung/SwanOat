from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about_us.html")

def astrologers_page(request):
    return render(request, "astrologers.html")

def services_page(request):
    return render(request, "services.html")

def contact_page(request):
    return render(request, "contact_us.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def service_page(request):
    return render(request, "service_request.html")