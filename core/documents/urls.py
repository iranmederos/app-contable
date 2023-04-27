from django.urls import path, include
from rest_framework import routers
from documents import views

router = routers.DefaultRouter()
router.register(r'document-type', views.DocumentTypeView, 'document-type')
router.register(r'item-document', views.ItemDocumentView, 'item-document')
router.register(r'purchase-document', views.PurchaseDocumentView, 'purchase-document')
router.register(r'sale-document', views.SaleDocumentView, 'sale-document')
router.register(r'sale-sumary', views.SaleSummaryView, 'sale-sumary')
router.register(r'ret-iva', views.RetIVAView, 'ret-iva')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
