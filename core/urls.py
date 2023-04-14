from django.urls import path

from core import views

urlpatterns = [
    path("signup", views.RegistrationView.as_view(), name='signup'),
]
