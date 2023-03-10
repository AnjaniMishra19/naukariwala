import requests
import datetime
from naukriwala.settings import *
from django.http import JsonResponse
from naukriwala.settings import *
import random
from User.views import *
from django.db.models import Q


def generateOTP(otp_size=6):
    final_otp = ''

    for i in range(otp_size):
        final_otp = final_otp + str(random.randint(0, 9))

    return final_otp


def send_otp(phone,user_id):

    otp = generateOTP()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ten_minutes_later = datetime.datetime.now() + datetime.timedelta(minutes=10)
    validity = ten_minutes_later.strftime("%Y-%m-%d %H:%M:%S")
    if CandidateData.objects.filter(Q(phone_no=phone) | Q(user_id=user_id)).exists():
        CandidateData.objects.filter(Q(phone_no=phone) | Q(user_id=user_id)).update(otp=otp, updated_at=date, otp_validity=validity)
    else:
        CandidateData.objects.create(phone_no=phone, user_id=user_id, otp=otp, otp_validity=validity, created_at=date)

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization": FSMS_KEY, "message": "To register on Naukriwala your OTP is" + otp,
                   "variables_values": str(otp), "route": "otp", "numbers": str(phone)}

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    print("dkkdkdkdk")

    if response.json()['return'] == True:
        print(otp)
        return JsonResponse({'status': 200, 'message': 'otp sent successfully'})
    else:
        return JsonResponse({'message': 'sms service failed', 'status': 400})
    # return JsonResponse({'status':200, 'message':'otp sent successfully'})

def company_send_otp(phone,company_id, otp):

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ten_minutes_later = datetime.datetime.now() + datetime.timedelta(minutes=10)
    validity = ten_minutes_later.strftime("%Y-%m-%d %H:%M:%S")
    if CompanyData.objects.filter(Q(phone_no=phone) | Q(company_id=company_id)).exists():
        CompanyData.objects.filter(Q(phone_no=phone) | Q(company_id=company_id)).update(otp=otp, updated_at=date, otp_validity=validity)


    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization": FSMS_KEY, "message": "To register on Naukriwala your OTP is" + otp,
                   "variables_values": str(otp), "route": "otp", "numbers": str(phone)}

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.json()['return'] == True:
        print(otp)
        return JsonResponse({'status': 200, 'message': 'otp sent successfully'})
    else:
        return JsonResponse({'message': 'sms service failed', 'status': 400})
    # return JsonResponse({'status':200, 'message':'otp sent successfully'})



def generate_token(user_id,phone):
    try:
        print("helllll")
        exp_time = datetime.datetime.now() + datetime.timedelta(days = 15)
        exp_time =exp_time.strftime("%Y-%m-%d %H:%M:%S")
        context = {
                    "user_id":user_id, 
                    "phone_no":phone, 
                    "exp_time":exp_time
                    }
        token = jwt.encode(context,SECRET_KEY,algorithm="HS256")
        print('===>',token)
        return token
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}   
        return JsonResponse({"error":response}), 200