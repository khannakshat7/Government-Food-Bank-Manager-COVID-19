from django.contrib import admin
from FoodBankManage.models import FoodBankBeneficiary,GramPanchayat,Block,FoodBankInventryDry,FoodBankInventrymid,FoodBankInventrycook
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(FoodBankBeneficiary)
# admin.site.register(GramPanchayat)
# admin.site.register(Block)

@admin.register(FoodBankBeneficiary)
@admin.register(GramPanchayat)
@admin.register(Block)
@admin.register(FoodBankInventryDry)
@admin.register(FoodBankInventrymid)
@admin.register(FoodBankInventrycook)
class ViewAdmin(ImportExportModelAdmin):
    pass
