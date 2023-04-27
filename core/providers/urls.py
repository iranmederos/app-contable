from django.urls import path, include
from rest_framework import routers
from customers import views

router = routers.DefaultRouter()
router.register(r'provider', views.CustomerView, 'provider')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
