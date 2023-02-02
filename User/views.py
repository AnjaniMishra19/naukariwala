import jwt
import re
import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from helpers import *
import json
from django.contrib.auth.hashers import make_password, check_password
import datetime
from django.db.models import Q
import uuid

from naukriwala.settings import *


# Create your views here.

@csrf_exempt
def phone_register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            phone = data['phone_no']
            user_id = uuid.uuid4().hex
            if phone == "":
                response = {"status": 200, "message": 'Phone number required.'}
            elif phone.isdigit() != True:
                response = {"status": 200, "message": 'Please enter numeric value only.'}

            elif EmployeeData.objects.filter(phone_no=phone).exists():
                response = {"status": 200, "message": 'Phone number already exist.'}
            else:
                send_otp(phone, user_id)
                response = {"status": 200, "data": [{'phone_no': phone, 'user_id': user_id}],
                            "message": "OTP sent to your phone number " + str(phone) + "."}

            # return HttpResponse({"status":"Success", "data":data})
            return JsonResponse(response)

    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        # return HttpResponse({"status":"Success", "data":data})
        return JsonResponse(response)


@csrf_exempt
def resend_otp(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            phone = data['phone_no']
            user_id = data['user_id']
            if EmployeeData.objects.filter(user_id=user_id).exists():
                send_otp(phone, user_id)
                response = {"status": 200, "data": phone,
                            "message": "OTP resent to your phone number " + str(phone) + "."}
            else:
                response = ({"status": 200, "data": phone, "message": "Phone number doesnot exist"})

            return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def verify_otp(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            phone = data['phone_no']
            user_id = data['user_id']
            otp = data['otp']
            token = generate_token(user_id, phone)
            # token = jwt.decode(token,SECRET_KEY,algorithms="HS256")
            user_data = EmployeeData.objects.get(phone_no=phone)
            if user_data.otp_validity > datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                if user_data.otp == otp:
                    EmployeeData.objects.filter(user_id=user_id).update(otp="", verified=True, otp_validity="",
                                                                        token=token)
                    response = {"status": 'success', "message": "OTP verified successfully."}
                    return JsonResponse(response)
                else:
                    response = {"status": 'error', "message": "OTP mismatched"}
                    return JsonResponse(response)
            else:
                response = {"status": 'error', "message": "OTP expired"}
                return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def candidate_register(request):
    try:
        if request.method == 'POST':
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  # For special character
            pattern = re.compile("^[a-zA-Z]+$")

            # data = request.data
            first_name = request.POST["first_name"] or ""
            last_name = request.POST["last_name"] or ""
            print(first_name)

            email = request.POST["email"] or ""
            user_id = request.POST["user_id"]
            print(first_name)
            password = make_password(request.POST['password']) or ""
            email_verified = True
            sex = request.POST["sex"] or ""
            latitude = request.POST["latitude"] or ""
            longitude = request.POST["longitude"] or ""
            qualification = request.POST["qualification"] or ""
            professional_qualification = request.POST["professional_qualification"] or ""
            technical_course_trade = request.POST["technical_course_trade"] or ""
            passout_year = request.POST["passout_year"] or ""
            expierence_year = request.POST["expierence_year"] or ""
            expierence_month = request.POST["expierence_month"] or ""
            current_working_company = request.POST["current_working_company"] or ""
            current_monthly_salary = request.POST["current_monthly_salary"] or ""

            salary_slip = request.FILES['salary_slip'] or ""
            profile_pic = request.FILES['profile_pic'] or ""
            resume = request.FILES['resume'] or ""
            role_id = request.POST["role_id"] or ""
            sex = request.POST["sex"] or ""
            pincode = request.POST["pincode"] or ""
            state = request.POST["state"] or ""
            city = request.POST["city"] or ""
            address = request.POST["address"] or ""
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            token = request.headers.get('token')
            print(token)
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            print(decoded_token)

            # Email already exist
            if EmployeeData.objects.filter(user_id=decoded_token['user_id']).exists():
                if EmployeeData.objects.filter(email=email, status=1):
                    response = {"message": "email Already exist", "status": "error"}
                # Special character not allowed in first name and last name
                elif (regex.search(first_name) != None):
                    response = {"message": "Special character are not allowed in first name", "status": "error"}

                elif (regex.search(last_name) != None):
                    response = {"message": "Special character are not allowed in last name", "status": "error"}

                elif (pattern.search(first_name) == None):
                    response = {"message": "Only alphabets are allowed in firstname", "status": "error"}

                elif (pattern.search(last_name) == None):
                    response = {"message": "Only alphabets are allowed in lastname", "status": "error"}

                # email_sent = email_notification(email,data["password"],first_name)
                else:
                    EmployeeData.objects.filter(user_id=user_id).update(
                        first_name=first_name,
                        last_name=last_name,
                        sex=sex,
                        password=password,
                        latitude=latitude,
                        longitude=longitude,
                        address=address,
                        city=city,
                        state=state,
                        pincode=pincode,
                        qualification=qualification,
                        professional_qualification=professional_qualification,
                        technical_course_trade=technical_course_trade,
                        passout_year=passout_year,
                        expierence_year=expierence_year,
                        expierence_month=expierence_month,
                        current_working_company=current_working_company,
                        current_monthly_salary=current_monthly_salary,
                        salary_slip=salary_slip,
                        profile_pic=profile_pic,
                        resume=resume,
                        status="1",
                        created_at=date,
                        role=role_id

                    )
                    response = {"status": 'success',
                                "message": first_name + last_name + 'your account registered successfully.'}
            else:
                response = {"status": 'error', "message": 'User not found.'}
            return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


############################################################################################################
# company register


@csrf_exempt
def company_phone_register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            phone = data['phone_no']
            company_id = uuid.uuid4().hex
            otp = generateOTP()
            if phone == "":
                response = {"status": 200, "message": 'Phone number required.'}
            elif phone.isdigit() != True:
                response = {"status": 200, "message": 'Please enter numeric value only.'}

            elif CompanyData.objects.filter(phone_no=phone).exists():
                response = {"status": 200, "message": 'Phone number already exist.'}
            else:
                company_send_otp(phone, company_id, otp)
                response = {"status": 200, "data": phone,
                            "message": "OTP sent to your phone number " + str(phone) + "."}

            # return HttpResponse({"status":"Success", "data":data})
            return JsonResponse(response)

    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        # return HttpResponse({"status":"Success", "data":data})
        return JsonResponse(response)


@csrf_exempt
def company_resend_otp(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            phone = data['phone_no']
            company_id = data['company_id']
            if CompanyData.objects.filter(company_id=company_id).exists():
                company_send_otp(phone, company_id)
                response = {"status": 200, "data": phone,
                            "message": "OTP resent to your phone number " + str(phone) + "."}
            else:
                response = ({"status": 200, "data": phone, "message": "Phone number doesnot exist"})
            return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def company_verify_otp(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            phone = data['phone_no']
            company_id = data['company_id']
            otp = data['otp']
            token = generate_token(company_id, phone)
            # token = jwt.decode(token,SECRET_KEY,algorithms="HS256")
            user_data = CompanyData.objects.get(phone_no=phone)
            if user_data.otp_validity > datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                if user_data.otp == otp:
                    CompanyData.objects.filter(company_id=company_id).update(otp="", phone_verified=True,
                                                                             otp_validity="", token=token)
                    response = {"status": 'success', "message": "OTP verified successfully."}
                    return JsonResponse(response)
                else:
                    response = {"status": 'error', "message": "OTP mismatched"}
                    return JsonResponse(response)
            else:
                response = {"status": 'error', "message": "OTP expired"}
                return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def company_register(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            if CompanyData.objects.filter(email=email).exists() or CompanyData.objects.filter(
                    phone_no=request.POST['phone_no']).exists():
                response = {'status': 'error', 'message': 'Email or phone already exist.'}
                return JsonResponse(response)
            else:
                email = request.POST['email']
                password = request.POST['password']
                company_name = request.POST['company_name']
                password = make_password(request.POST['password'])
                phone_no = request.POST['phone_no']
                gst_no = request.POST['gst_no']
                pincode = request.POST['pincode']
                address = request.POST['address']
                company_id = uuid.uuid4().hex
                lat = request.POST['lat']
                long = request.POST['long']
                company_logo = request.FILES['company_logo']
                otp = generateOTP()
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ten_minutes_later = datetime.datetime.now() + datetime.timedelta(minutes=10)
                validity = ten_minutes_later.strftime("%Y-%m-%d %H:%M:%S")
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if CompanyData.objects.filter(company_name=company_name).exists():
                    response = {'status': 'error', 'message': 'Company name already exists.'}
                elif CompanyData.objects.filter(gst_no=gst_no).exists():
                    response = {'status': 'error', 'message': 'Company GST number already exists.'}
                else:
                    CompanyData.objects.create(
                        phone_no=phone_no, otp=otp,
                        otp_validity=validity,
                        created_at=date,
                        company_id=company_id,
                        email=email,
                        password=password,
                        company_name=company_name,
                        address=address,
                        pincode=pincode,
                        latitude=lat,
                        longitude=long,
                        gst_no=gst_no,
                        company_logo=company_logo
                    )
                    company_send_otp(phone_no, company_id, otp)
                    response = {"status": 200, "data": phone_no,
                                "message": "OTP sent to your phone number " + str(phone_no) + "."}
            return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def company_login(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            Company = CompanyData.objects.get(phone_no=data['phone_no'])
            print(Company.password)
            print(data['password'])
            print(check_password(data['password'], Company.password))
            if Company and check_password(data['password'], Company.password):
                token = generate_token(Company.company_id, Company.phone_no)
                CompanyData.objects.filter(company_id=Company.company_id).update(token=token)
                company_data = CompanyData.objects.filter(company_id=Company.company_id).values()[0]

                request.session['token'] = Company.token
                response = {"status": 'success', "message": 'Company logged in successfully', "data": [company_data]}
            else:
                response = {"status": 'error', "message": 'Invalid Company'}
            return JsonResponse(response)

    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)


@csrf_exempt
def company_details(request):
    try:
        if request.method == 'POST':
            token = request.headers.get("token")
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            if decoded_token['user_id']:
                if decoded_token['exp_time'] > datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S") and CompanyData.objects.filter(
                    company_id=decoded_token['user_id']).exists():
                    data = CompanyData.objects.filter(company_id=decoded_token['user_id']).values()[0]

                    response = {"status": 'success', "message": data['company_name'] + " details retrived successfully",
                                "data": [data]}
                    return JsonResponse(response)
            else:
                response = {"status": 'error', "message": "Unathorized Access"}

    except Exception as e:
        traceback.print_exc()
        response = {"status": 'error', "message": f'{str(e)}'}
        return JsonResponse(response)
