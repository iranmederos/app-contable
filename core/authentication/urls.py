from django.urls import path
from authentication import views

urlpatterns = [
    path('api/v1/register/', views.RegisterUserView.as_view()),
    path('api/v1/login/', views.LoginView.as_view()),
    path('api/v1/user/', views.UserView.as_view()),
    path('api/v1/logout/', views.LogoutView.as_view())
]