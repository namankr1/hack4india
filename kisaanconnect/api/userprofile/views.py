from django.shortcuts import render
import json
from django.contrib.auth import logout
from django.http import JsonResponse
from . import services
# Create your views here.

def signup(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin=json.loads(request.body)
            result = services.profile_signup(jsonin['firstName'],jsonin['lastName'],jsonin['phone'],jsonin['address'],jsonin['password']);
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Account type is incorrect'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'First name field input contains characters other than space and letters'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'Last name field input contains characters other than space and letters'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'Phone number is not correct'})
        elif result == -5:
            return JsonResponse({'status':'err', 'message': 'Password is too short'})
        elif result == -6:
            return JsonResponse({'status':'err', 'message': 'Location cannot be retrieved successfully'})
        elif result == -7:
            return JsonResponse({'status':'err', 'message': 'Mobile number already registered'})
        elif result==1:
            return JsonResponse({'status':'ok', 'message': 'User is successfully registered'})
        else:
            return JsonResponse({'status':'err', 'message': 'Server encountered unknown problem. Try again'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad request'})
        
def signin(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin=json.loads(request.body)
            result = services.user_signin(jsonin['phone'],jsonin['password'],request);
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is invalid'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'Password length is invalid'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'The mobile number is not registered'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'User account is disabled'})
        elif result == -5:
            return JsonResponse({'status':'err', 'message': 'Password is incorrect'})
        elif result == 1:
            return JsonResponse({'status':'ok', 'message': 'Successfully logged in'})
        else:
            return JsonResponse({'status':'err', 'message': 'Server encountered unknown problem. Try again'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})
def verifyOTP(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin=json.loads(request.body)
            result = services.verifyOTP(jsonin['phone'],jsonin['otp'])
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is invalid'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'OTP is invalid'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'The mobile number is not registered'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'There is no OTP to verify for this mobile phone'})
        elif result == -5:
            return JsonResponse({'status':'err', 'message': 'OTP is incorrect'})
        elif result == 1:
            return JsonResponse({'status':'ok', 'message': 'OTP verified successfully'})
        else:
            return JsonResponse({'status':'err', 'message': 'Server encountered unknown problem. Try again'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def signout(request):
    logout(request)
    return JsonResponse({'status':'ok','message':'Signed out successfully'})

def sendOTP(request):
    if request.method == 'POST':
        jsonin = json.loads(request.body)
        result = services.sendOTP(jsonin['phone'])
        if result==1:
            return JsonResponse({'status':'ok', 'message': 'OTP sent'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def changepassword(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin = json.loads(request.body)
            result = services.changePassword(jsonin['phone'],jsonin['oldpassword'],jsonin['newpassword'])
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is invalid'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'Mobile number is not registered'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'Current password is incorrect'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'New password is short'})
        elif result == 1:
            return JsonResponse({'status':'ok', 'message': 'Successfully changed password'})
        else:
            return JsonResponse({'status':'err', 'message': 'Server encountered unknown problem. Try again'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def forgotpassword(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.forgotPassword(jsonin['phone'],jsonin['otp'],jsonin['newpassword'])
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is invalid'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'OTP is invalid'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'The mobile number is not registered'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'There is no OTP to verify for this mobile phone'})
        elif result == -5:
            return JsonResponse({'status':'err', 'message': 'OTP is incorrect'})
        elif result == 1:
            return JsonResponse({'status':'ok', 'message': 'Password changed successfully'})
        else:
            return JsonResponse({'status':'err', 'message': 'Server encountered unknown problem. Try again'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def profileupdate(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.profileUpdate(jsonin)
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is out of length'})
        elif result == -2:
            return JsonResponse({'status':'err', 'message': 'Phone number is already registered'})
        elif result == -3:
            return JsonResponse({'status':'err', 'message': 'Failed to get valid address. Try again'})
        elif result == -4:
            return JsonResponse({'status':'err', 'message': 'Failed to upload profile picture'})
        elif result == 0:
            return JsonResponse({'status':'ok', 'message': 'No update happened'})
        elif result == 1:
            return JsonResponse({'status':'ok', 'message': 'Update successful'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})
def getprofile(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.getProfile(jsonin)
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status':'err', 'message': 'Phone number is invalid'})
        else:
            return JsonResponse({'status':'ok', 'profile':result})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})
