from django.contrib import admin
from User.models import *
# Register your models here.
@admin.register(EmployeeData)
class UserDataAdmin(admin.ModelAdmin):
    readonly_fields  = ["user_id"]
    list_display = ['user_id','first_name', 'last_name', 'phone_no', 'address', 'pincode', 'sex', 'status']
    

@admin.register(CompanyData)
class UserDataAdmin(admin.ModelAdmin):
    readonly_fields  = ["company_id"]
    list_display = ['company_id','company_name', 'gst_no', 'phone_no', 'address', 'pincode', 'status']
    


# admin.site.register(EmployeeData, UserDataAdmin)
