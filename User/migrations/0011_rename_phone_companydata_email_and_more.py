# Generated by Django 4.1.5 on 2023-01-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_employeedata_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydata',
            old_name='phone',
            new_name='email',
        ),
        migrations.AddField(
            model_name='companydata',
            name='company_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companydata',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]