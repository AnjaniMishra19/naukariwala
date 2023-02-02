import re
import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from helpers import *
import json
import datetime
from django.db.models import Q

from naukriwala.settings import *
# Create your views here.

@csrf_exempt
def post_job(request):
    try:
        token = request.headers.get("token")
        data = json.loads(request.body)
        decoded_token =  jwt.decode(token,SECRET_KEY, algorithms='HS256')
        if decoded_token['user_id']:
            if decoded_token['exp_time'] > datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") and CompanyData.objects.filter(company_id=decoded_token['user_id']).exists():
                company_data = CompanyData.objects.get(company_id=decoded_token['user_id'])
                Job_Post.objects.create(
                    company = company_data,
                    job_title = data['job_title'],
                    position = data['position'],
                    min_salary = data['min_salary'],
                    max_salary = data['max_salary'],
                    gender = data['gender'],
                    location = data['location'],
                    lat = data['lat'],
                    long = data['long'],
                    skills = data['skills'],
                    opening_time = data['opening_time'],
                    closing_time = data['closing_time'],
                    working_days = data['working_days'],
                    ot_rate = data['ot_rate'],
                    contact = data['contact'],
                    description = data['description'],
                    status = "1"
                )

                response = {"status": 'success', "message":"Job posted successfully."}
            else:
                response = {"success":'error', 'message':"User signature expired"}
        else:
            response = {"success":'error', 'message':"User does not exist"}
        return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def post_job_update(request):
    try:
        token = request.headers.get("token")
        data = json.loads(request.body)
        decoded_token =  jwt.decode(token,SECRET_KEY, algorithms='HS256')
        if decoded_token['user_id']:
            if decoded_token['exp_time'] > datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") and CompanyData.objects.filter(company_id=decoded_token['user_id']).exists():
                Job_Post.objects.filter(company__company_id= decoded_token['user_id'],job_id = data['job_id']).update(
                    job_title = data['job_title'],
                    position = data['position'],
                    min_salary = data['min_salary'],
                    max_salary = data['max_salary'],
                    gender = data['gender'],
                    location = data['location'],
                    lat = data['lat'],
                    long = data['long'],
                    skills = data['skills'],
                    opening_time = data['opening_time'],
                    closing_time = data['closing_time'],
                    working_days = data['working_days'],
                    ot_rate = data['ot_rate'],
                    contact = data['contact'],
                    description = data['description'],
                    status = data['status']
                    )
                job_data = Job_Post.objects.filter(job_id=data['job_id']).values()[0]
                response = {"success":'success', 'message':"Job details updated successfully", "data":[job_data]}
                return JsonResponse(response)
            else:
                response = {"success":'error', 'message':"User signature expired"}
                return JsonResponse(response)
        else:
            response = {"success":'error', 'message':"User does not exist"}
            return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)