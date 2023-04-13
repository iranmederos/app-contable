from django.contrib import admin
from .models import SaleSummary,PurchaseDocument,SaleDocument,ItemDocument,DocumentType,RetIVA
# Register your models here.


class SaleSummaryAdmin(admin.ModelAdmin):
    list_display = ("id","code", "description")

class PurchaseDocumentAdmin(admin.ModelAdmin):
    list_display = ("id","document_number", "document_type")

class SaleDocumentAdmin(admin.ModelAdmin):
    list_display = ("id","document_number", "document_type")

class ItemDocumentAdmin(admin.ModelAdmin):
    list_display = ("id","description","amount","amount_iva")

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("id","type_doc")

class RetIVAAdmin(admin.ModelAdmin):
    list_display=("id","nro_ret","date_ret_iva")


admin.site.register(SaleSummary, SaleSummaryAdmin)
admin.site.register(PurchaseDocument, PurchaseDocumentAdmin)
admin.site.register(SaleDocument, SaleDocumentAdmin)
admin.site.register(ItemDocument, ItemDocumentAdmin)
admin.site.register(RetIVA, RetIVAAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
