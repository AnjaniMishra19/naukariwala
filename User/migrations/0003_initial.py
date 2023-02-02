# Generated by Django 4.1.5 on 2023-01-25 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0002_remove_employeedata_user_delete_companydata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_validity', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(blank=True, choices=[('male', '0'), ('female', '1'), ('other', '2')], max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('latitude', models.FloatField(blank=True, max_length=16, null=True)),
                ('longitude', models.FloatField(blank=True, max_length=16, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('technical_course_trade', models.CharField(blank=True, max_length=100, null=True)),
                ('professional_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('passout_year', models.CharField(blank=True, max_length=6, null=True)),
                ('expierence_year', models.CharField(blank=True, max_length=5, null=True)),
                ('expierence_month', models.CharField(blank=True, max_length=5, null=True)),
                ('current_working_company', models.CharField(blank=True, max_length=50, null=True)),
                ('current_monthly_salary', models.CharField(blank=True, max_length=10, null=True)),
                ('salary_slip', models.FileField(upload_to='employee_salary_slip')),
                ('profile_pic', models.FileField(upload_to='employee_profile_pic')),
                ('created_at', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, choices=[('active', '1'), ('delete', '0'), ('inactive', '2')], max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='emp_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Employee Data',
            },
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_validity', models.CharField(blank=True, max_length=6, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.FloatField(blank=True, max_length=20, null=True)),
                ('longitude', models.FloatField(blank=True, max_length=20, null=True)),
                ('company_logo', models.FileField(upload_to='company_logo')),
                ('created_at', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, max_length=40, null=True, verbose_name=(('active', '1'), ('delete', '0'), ('inactive', '2')))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comp_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Company Data',
            },
        ),
    ]