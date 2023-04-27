from django.urls import path, include
from rest_framework import routers
from tax_machine import views

router = routers.DefaultRouter()
router.register(r'tax_machine', views.CustomerView, 'tax_machine')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
