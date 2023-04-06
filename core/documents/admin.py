from django.contrib import admin
from .models import SalesSummary,BuysDocument,SalesDocument,DocumentsItems,Totals,DocumentType
# Register your models here.


class SalesSummaryAdmin(admin.ModelAdmin):
    list_display = ("id","code", "description")

class BuysDocumentAdmin(admin.ModelAdmin):
    list_display = ("id","document_number", "document_type")

class SalesDocumentAdmin(admin.ModelAdmin):
    list_display = ("id","document_number", "document_type")

class DocumentsItemsAdmin(admin.ModelAdmin):
    list_display = ("id","description","amount","amount_iva")

class TotalsAdmin(admin.ModelAdmin):
    list_display = ("id","amount", "neto_amount")

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("id","type_doc")

admin.site.register(SalesSummary, SalesSummaryAdmin)
admin.site.register(BuysDocument, BuysDocumentAdmin)
admin.site.register(SalesDocument, SalesDocumentAdmin)
admin.site.register(DocumentsItems, DocumentsItemsAdmin)
admin.site.register(Totals, TotalsAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
