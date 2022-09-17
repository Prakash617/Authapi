"""consultancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('', views.CarouselList,basename="carousel")

urlpatterns = [
    path('carousel/', views.CarouselList.as_view()),
    path('carousel/<slug:slug>/', views.CarouselList.as_view()),
    path('visa/', views.VisaList.as_view()),
    path('visa/<slug:slug>/', views.VisaList.as_view()),
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('changepassword/', views.UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset-password'),
    # path('', include(router.urls)),
]
