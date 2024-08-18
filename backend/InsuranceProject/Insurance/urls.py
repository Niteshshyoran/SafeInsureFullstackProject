from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import RegisterView,LoginView,LogoutView,CompanyRegisterView,CompanyUpdateView,PolicyRegisterView,PolicyUpdateView,ClaimRegisterView,ClaimUpdateView,PaymentRegisterView,PaymentUpdateView
urlpatterns = [
    # path('resetpassword/', PasswordResetRequestView.as_view(),name='reset'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(),name = "login"),
    path('logout/', LogoutView.as_view(),name = "logout"),
    path('company/', CompanyRegisterView.as_view(),name = 'company'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(),name='update'),
    path('policy/', PolicyRegisterView.as_view(),name = 'policy'),
    path('policy/<int:pk>/update/', PolicyUpdateView.as_view(),name='update'),
    path('claim/', ClaimRegisterView.as_view(),name = 'claim'),
    path('claim/<int:pk>/update/', ClaimUpdateView.as_view(),name='update'),
    path('payment/', PaymentRegisterView.as_view(),name = 'payment'),
    path('payment/<int:pk>/update/', PaymentUpdateView.as_view(),name='update'),
]
