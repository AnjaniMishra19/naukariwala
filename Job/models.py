from django.db import models
from User.models import *
# Create your models here.

# company job post 
job_status = (('1', 'active'), ('0', 'deleted'),('2','inactive'), ('3','closed'))

class Job_Post(models.Model):
    company = models.ForeignKey(CompanyData, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    min_salary = models.CharField(max_length=10, null=True, blank=True)
    max_salary = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
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
    status = models.CharField(max_length=15,choices=job_status, null=True, blank=True)

    class Meta:
        db_table="JobData"
    def __str__(self):
        if self.company.company_name != None and self.job_title != None:
            return str(self.company.company_name+' '+self.job_title)

applied_status = ( ('0', 'Applied'),('1', 'Viewed'),('2','Shortlisted'), ('3','Selected'), ('4','Rejected'))

class JobApplied(models.Model):
    candidate = models.ForeignKey(CandidateData, on_delete=models.CASCADE)
    job = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    cv_status = models.CharField(max_length=20, choices=applied_status,default="0")
    created_at = models.CharField(max_length=50, null=True, blank=True)
    updated_at = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table="AppliedJob"
    def __str__(self):
        if self.candidate.first_name != None and self.job.position != None:
            return str(self.candidate.first_name+' '+ self.candidate.last_name + ' '+ self.job.position)
# #candiate apply for job
# candidate ID 
# Candidate Name
# Designation (Fresher/experienced)
# JOB TITLE
# JOB POST ID 
# COMPANY NAME
# COMPANY ID
# JOB Expirey DATE
# CV Status (Shortlisted,Reviwed by HR , Selected)
# FIELD status (Active...)
# created 
# Upadted
