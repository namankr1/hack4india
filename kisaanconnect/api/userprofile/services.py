from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import random
import json,urllib
from categorization import services as catservices

def getLatLon(address):
    address = urllib.quote_plus(address)
    geo = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % (address))
    return geo.read()

def sendOTP(phone):
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=models.Profile.objects.filter(user=u[0])
    #token = random.randrange(100000, 1000000, 1)
    token=112233
    otp = models.OTPRecord(otp=token,profile=profileobj[0]);
    otp.save()
    return 1
    

def profile_signup(firstName,lastName,phone,address,password):
    accountType='I'
    if(accountType!='I' and accountType!='C'):
        return -1
    if all(x.isalpha() or x.isspace() for x in firstName):
        pass
    else:
        return -2
    if all(x.isalpha() or x.isspace() for x in lastName):
        pass
    else:
        return -3
    if (not phone.isdigit()) or len(phone)!=10:
        return -4
    if len(password)<8:
        return -5
    u=User.objects.filter(username='I'+str(phone))
    if len(u)>0:
        return -7
    user = User.objects.create_user(username = accountType+str(phone), password = password,first_name=firstName,last_name= lastName,is_active=False)
    print password
    user.save()
    try:
        geo = json.loads(getLatLon(address))
    except Exception:
        user.delete()
        return -6
    loc = None
    if geo['status'] == "OK":
        loc = models.Location(address=address,latitude = geo['results'][0]['geometry']['location']['lat'],longitude = geo['results'][0]['geometry']['location']['lng'])
        loc.save();
    else:
        user.delete()
        return -6
    profileobj = models.Profile(user = user, accountType = accountType,location = loc  )
    profileobj.save();
    #token = random.randrange(100000, 1000000, 1)
    token = 112233
    otp = models.OTPRecord(otp=token,profile=profileobj);
    otp.save()
    sendOTP(phone)
    return 1;

def user_signin(phone, password,request):
    if len(phone) !=10:
        return -1
    if len(password)<8:
        return -2
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -3
    profileobj=models.Profile.objects.filter(user=u[0])
    print u[0].username+","+password
    #user = authenticate(username= u[0].username, password = password)
    
    if u[0].check_password(password):
        if u[0].is_active:
            login(request,u[0])
            return 1
        else:
            return -4
    else:
        return -5

def verifyOTP(phone,token):
    if len(phone)!=10:
        return -1
    if len(token)!=6:
        return -3
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=models.Profile.objects.filter(user=u[0])
    otpobj = models.OTPRecord.objects.filter(profile=profileobj[0])
    if len(otpobj)==0:
        return -4
    else:
        if otpobj[0].otp==token:
            otpobj[0].delete()
            u[0].is_active=True
            u[0].save()
            return 1
        else:
            return -5

def changePassword(phone,oldpassword,newpassword):
    if len(phone)!=10:
        return -1
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    if len(newpassword)<8:
        return -4
    profileobj=models.Profile.objects.filter(user=u[0])
    if(u[0].check_password(oldpassword)):
        u[0].set_password(newpassword)
        u[0].save()
        if(u[0].check_password(newpassword)):
            print "Changed"
        return 1
    else:
        return -3

def forgotPassword(phone,otp,newpassword):
    resultotp = verifyOTP(phone,otp)
    if resultotp == 1:
        u=User.objects.filter(username='I'+str(phone))
        if len(u)==0:
            return -2
        profileobj=models.Profile.objects.filter(user=u[0])
        u[0].set_password(newpassword)
        u[0].save()
        if(u[0].check_password(newpassword)):
            print "Changed"
        return 1
    else:
        return resultotp

def profileUpdate(jsonin, img=None):
    if 'phone' in jsonin:
        u=User.objects.filter(username='I'+str(jsonin['phone']))
        if len(u)==0:
            return -1
        profileobj=models.Profile.objects.filter(user=u[0])
    elif 'userid' in jsonin:
        profileobj = models.Profile.objects.filter(id=jsonin['userid'])
        if len(profileobj)==0:
            return -1
    flag=0
    #if 'phone' in jsonin:
        #if len(jsonin['phone'])!=10:
            #return -1
        #musers1 = User.objects.filter(username='I'+str(jsonin['phone']))
        #musers2 = User.objects.filter(username='C'+str(jsonin['phone']))
        #if len(musers1) !=0 or len(musers2)!=0:
            #return -2
        #user.username = user.username[0]+str(jsonin['phone'])
        #user.save()
        #flag=1
    if 'address' in jsonin:
        profileobj = models.Profile.objects.filter(user=u[0])
        if len(profileobj)==0:
            return -3
        geo = json.loads(getLatLon(jsonin['address']))
        loc = None
        if geo['status'] == "OK":
            loc = models.Location(latitude = geo['results'][0]['geometry']['location']['lat'],longitude = geo['results'][0]['geometry']['location']['lng'])
            loc.save();
            profileobj[0].location.delete()
            profileobj[0].location=loc
            profileobj[0].save()
            flag=1
        else:
            return -3
    if img != None:
        profileobj = models.Profile.objects.filter(user=u[0])
        if len(profileobj)==0:
            return -4
        profileobj[0].picture=img
        profileobj[0].save()
        flag =1
    if flag==1:
        return 1
    else:
        return 0

def getProfile(jsonin):
    print "his"
    if 'phone' in jsonin:
        u=User.objects.filter(username='I'+str(jsonin['phone']))
        if len(u)==0:
            return -1
        profileobj=models.Profile.objects.filter(user=u[0])
    elif 'userid' in jsonin:
        profileobj = models.Profile.objects.filter(id=jsonin['userid'])
        if len(profileobj)==0:
            return -1
    jsonout={}
    jsonout['userid'] = profileobj[0].id
    jsonout['name']=profileobj[0].user.get_full_name()
    jsonout['phone']=profileobj[0].user.username[1:]
    jsonout['type']=profileobj[0].user.username[0]
    jsonout['address']=profileobj[0].location.address
    return jsonout
