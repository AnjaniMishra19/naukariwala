from django.db import models
from django.contrib.auth.models import User

sex = (('0', 'male'), ('1', 'female'),('2','other'))
user_status = (('1', 'active'), ('0', 'delete'),('2','inactive'), ('3','pending'))
role = (('0','employee'),('1','company'))

# 1. For bussiness Active ,Pending,Inactive,Archive  For Student Active , For businesss Pending
# 1. add Resume

class CandidateData(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp_user')
    id = models.AutoField(primary_key=True,unique=True ,auto_created=True)
    candidate_identifier = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=240, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    user_id = models.CharField(max_length=50, null=True, blank=True)
    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True, blank=True)
    otp_validity = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(max_length=1000,null=True, blank=True)
    token = models.CharField(max_length=10000,null=True, blank=True)
    role = models.CharField(choices=role, max_length=10,null=True, blank=True)
    gender = models.CharField(choices=sex, max_length=10,null=True, blank=True)

    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)

    latitude = models.FloatField(max_length=16,null=True, blank=True)
    longitude = models.FloatField(max_length=16,null=True, blank=True)
    qualification = models.CharField(max_length=100,null=True, blank=True)
    professional_qualification = models.CharField(max_length=100,null=True, blank=True)
    technical_course_trade = models.CharField(max_length=100,null=True, blank=True)
    passout_year = models.CharField(max_length=6,null=True, blank=True)
    expierence_year = models.CharField(max_length=5,null=True, blank=True)
    expierence_month = models.CharField(max_length=5,null=True, blank=True)
    current_working_company = models.CharField(max_length=50,null=True, blank=True)
    current_monthly_salary = models.CharField(max_length=10,null=True, blank=True)
    salary_slip = models.FileField(upload_to='user_salary_slip', null=True)
    profile_pic = models.FileField(upload_to='user_profile_pic', null=True)
    resume = models.FileField(upload_to='user_resume', null=True)

    created_at = models.CharField(max_length=40,null=True, blank=True)
    updated_at = models.CharField(max_length=40,null=True, blank=True)

	
    status = models.CharField(choices=user_status,max_length=40, null=True, blank=True)
    class Meta:
        db_table="CandidateData"
    def __str__(self, *args, **kwargs):
        if not self.candidate_identifier:
            suffix = str(self.id)
            while True:
                self.candidate_identifier = "NC0000" + suffix
                try:
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    suffix = str(int(suffix) + 1)
        else:
            super().save(*args, **kwargs)
        if self.first_name != None and self.last_name != None:
            return str(self.first_name+' '+self.last_name)
        else:
            return str(self.phone_no)
        
       

class CompanyData(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='comp_user')
    id = models.AutoField(primary_key=True,unique=True ,auto_created=True)
    company_id = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    company_identifier = models.CharField(max_length=50, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=10000,null=True, blank=True)
    password = models.CharField(max_length=1000,null=True, blank=True)
    otp = models.CharField(max_length=6,null=True, blank=True)
    otp_validity = models.CharField(max_length=6,null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    gst_no = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField(max_length=20,null=True, blank=True)
    longitude = models.FloatField(max_length=20,null=True, blank=True)
    company_logo = models.FileField(upload_to='company_logo', null=True)

    created_at = models.CharField(max_length=40,null=True, blank=True)	
    updated_at = models.CharField(max_length=40,null=True, blank=True)	
    status = models.CharField(choices=user_status, max_length=40,null=True, blank=True)

    class Meta:
        db_table="CompanyData"
    def __str__(self,*args, **kwargs):
        if not self.company_identifier:
            print(self.company_identifier,self.id)
            suffix = str(self.id)
            while True:
                self.company_identifier = "NB0000" + suffix
                try:
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    suffix = str(int(suffix) + 1)
        else:
            super().save(*args, **kwargs)
        if self.company_name != None:
            return str(self.company_name)
        else:
            return str(self.company_id)
        

       
