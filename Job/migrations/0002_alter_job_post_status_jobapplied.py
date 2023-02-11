# Generated by Django 4.1.5 on 2023-02-09 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_candidatedata_user_id'),
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'active'), ('0', 'deleted'), ('2', 'inactive'), ('3', 'closed')], max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='JobApplied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_status', models.CharField(choices=[('0', 'Applied'), ('1', 'Viewed'), ('2', 'Shortlisted'), ('3', 'Selected'), ('4', 'Rejected')], default='0', max_length=20)),
                ('created_at', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.candidatedata')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.job_post')),
            ],
            options={
                'db_table': 'AppliedJob',
            },
        ),
    ]