"""
URL configuration for isha_training project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from courses import views


def google_verify(request):
    return HttpResponse("google-site-verification: googled8f6b869755f3971.html")


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('enroll/', views.enroll),

    path('googled8f6b869755f3971.html', google_verify),
]