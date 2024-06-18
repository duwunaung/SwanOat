from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index_page, name="home"),
    path("about", views.about_page, name="about"),
    path("astrologers", views.astrologers_page, name="astrologers"),
    path("services", views.services_page, name="services"),
    path("service", views.service_page, name="service"),
    path("contact", views.contact_page, name="contact"),
    path("login", views.login_page, name="login"),
    path("register", views.register_page, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
