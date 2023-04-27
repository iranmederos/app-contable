from django.urls import path, include
from rest_framework import routers
from company import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyView, 'company')
router.register(r'registration_data', views.RegistrationDataView, 'registration_data')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
