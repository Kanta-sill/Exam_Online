"""Exam_Online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from facultys import views as fa_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/', include('exams.urls')),
    path('students/', include('students.urls')),

    path('login/', auth_view.LoginView.as_view(template_name='faculty/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='faculty/logout.html'), name='logout'),
    path('profile/', fa_view.profilepage, name='profile'),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
