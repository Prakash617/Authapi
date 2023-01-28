from django.urls import path,include
from . import views


urlpatterns = [
    path('carousel/', views.CarouselList.as_view()),
    path('carousel/<slug:slug>/', views.CarouselList.as_view()),
    path('visa/', views.VisaList.as_view()),
    path('team/', views.TeamList.as_view()),
    path('visa/<slug:slug>/', views.VisaList.as_view()),
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('changepassword/', views.UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset-password'),
    # path('', include(router.urls)),
]
