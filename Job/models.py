from django.db import models
from User.models import *
# Create your models here.
gender = (('0', 'male'), ('1', 'female'),('2','all'))
job_status = (('1', 'active'), ('0', 'delete'),('2','inactive'), ('3','pending'))

class Job_Post(models.Model):
    company = models.ForeignKey(CompanyData, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True,unique=True ,auto_created=True)
    job_id = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    min_salary = models.CharField(max_length=10, null=True, blank=True)
    max_salary = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(choices=gender,max_length=50, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    lat = models.CharField(max_length=16, null=True, blank=True)
    long = models.CharField(max_length=16, null=True, blank=True)
    skills = models.CharField(max_length=500, null=True, blank=True)
    opening_time = models.CharField(max_length=10, null=True, blank=True)
    closing_time = models.CharField(max_length=10, null=True, blank=True)
    working_days = models.CharField(max_length=50, null=True, blank=True)
    ot_rate = models.CharField(max_length=7, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(choices=job_status,max_length=15, null=True, blank=True)

    class Meta:
        db_table="Job Data"
    def __str__(self,*args, **kwargs):
        if not self.job_id:
            suffix = str(self.id)
            while True:
                self.job_id = "NWJOB0000" + suffix
                try:
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    suffix = str(int(suffix) + 1)
        else:
            super().save(*args, **kwargs)
        if self.company.company_name != None and self.job_title != None:
            return str(self.company.company_name+' '+self.job_title)

