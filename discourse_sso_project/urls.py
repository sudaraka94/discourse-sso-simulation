"""discourse_sso_project URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
	path('discourse/', views.sso),
]
