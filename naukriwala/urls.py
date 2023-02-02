"""naukriwala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from User.views import *
from Job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # user
    path('user/phone_register', phone_register),
    path('user/resend_otp', resend_otp),
    path('user/verify_otp', verify_otp),
    path('user/candidate_register', candidate_register),

    # company
    path('user/company_login', company_login),
    path('user/company_register', company_register),
    path('user/company_phone_register', company_phone_register),
    path('user/company_resend_otp', company_resend_otp),
    path('user/company_verify_otp', company_verify_otp),
    path('user/company_details', company_details),

    # job_post
    path('job/post_job', post_job),
    path('job/post_job_update', post_job_update),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
