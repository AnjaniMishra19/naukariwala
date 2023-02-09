from django.contrib import admin
from User.models import *
# Register your models here.
@admin.register(CandidateData)
class CandidateDataAdmin(admin.ModelAdmin):
    readonly_fields  = ["user_id"]
    list_display = ['user_id','first_name', 'last_name', 'phone_no', 'address', 'pincode', 'gender', 'status']
    

@admin.register(CompanyData)
class CompanyDataAdmin(admin.ModelAdmin):
    readonly_fields  = ["company_id"]
    list_display = ['company_id','company_name', 'gst_no', 'phone_no', 'address', 'pincode', 'status']
    


