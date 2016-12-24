from . import models
from django.contrib.auth.models import User
from userprofile import models as usermodels
from userprofile import services as userservices
from categorization import services as catservices
from categorization import models as categorymodels
from django.db.models import Q
import operator,math

def addQuote(phone,subcategoryId,type,quantity,price,description=None):
    if len(phone) !=10:
        return -1
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=usermodels.Profile.objects.filter(user=u[0])
    subcategoryobj=categorymodels.Subcategory.objects.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    quotes = models.Quote.objects.filter(profile = profileobj[0],subcategory = subcategoryobj[0])
    if len(quotes)!=0:
    	return -4
    quoteobj = models.Quote(profile = profileobj[0],subcategory = subcategoryobj[0],type=catservices.translate(type),quantity = quantity, price= price,bidvalue=price,description=catservices.translate(description),is_active=True)
    quoteobj.save()
    ratingobj=models.Rating.objects.filter(profile=profileobj[0],subcategory=subcategoryobj[0])
    if len(ratingobj)==0:
        newobj=models.Rating(profile=profileobj[0],subcategory=subcategoryobj[0],rating=0)
        newobj.save()
    return 1

def getQuote(quoteId):
    quoteobj = models.Quote.objects.filter(id=quoteId)
    print "hi"
    if len(quoteobj)==0:
        return -1
    else:
        jsonout={}
        jsonout['id']=quoteobj[0].id
        jsonout['type']=quoteobj[0].type
        jsonout['quantity']=quoteobj[0].quantity
        jsonout['price']=quoteobj[0].price
        jsonout['description']=quoteobj[0].description
        print "hi"
        jsonout['profile']=userservices.getProfile({"userid":quoteobj[0].profile.id})
        jsonout['subcategoryname']=quoteobj[0].subcategory.name
        print "hi"
        jsonout['is_active']=quoteobj[0].is_active
        jsonout['bidvalue']=quoteobj[0].bidvalue
        print "hi"
        ratingobj=models.Rating.objects.filter(profile=quoteobj[0].profile,subcategory=quoteobj[0].subcategory)
        print "hi"
        jsonout['rating']=ratingobj[0].rating
        
        return jsonout

def deleteQuote(quoteId):
    quoteobj = models.Quote.objects.filter(id=quoteId)
    if len(quoteobj)==0:
        return -1
    quoteobj[0].delete()

def updateQuote(jsonin):
    flag=0
    if 'quoteId' not in jsonin:
        return -1
    quoteobj = models.Quote.objects.filter(id=jsonin['quoteId'])
    if len(quoteobj)==0:
        return -2
    if 'type' in jsonin:
        quoteobj.update(type=catservices.translate(jsonin['type']))
        flag=1
    if 'quantity' in jsonin:
        quoteobj.update(quantity=jsonin['quantity'])
        flag=1
    if 'price' in jsonin:
        quoteobj.update(price=jsonin['price'])
        quoteobj.update(bidvalue=jsonin['price'])
        flag=1
    if 'is_active' in jsonin:
        quoteobj.update(is_active=jsonin['is_active'])
        flag=1
    if 'bidvalue' in jsonin:
        if quoteobj.bidvalue<jsonin['bidvalue']:
            quoteobj.update(bidvalue=jsonin['bidvalue'])
            flag=1
    if flag==1:
        return 1
    else:
        return 0
        
def getQuotesbyUser(phone,subcategoryId):
    print "hi"
    if len(phone) !=10:
        return -1
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=usermodels.Profile.objects.filter(user=u[0])
    if len(profileobj)==0:
        return -2
    subcategoryobj=categorymodels.Subcategory.objects.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    print "hi"
    quoteobj = models.Quote.objects.filter(profile=profileobj[0],subcategory=subcategoryobj[0])
    print len(quoteobj)
    jsonout=[]
    for q in quoteobj:
        j=getQuote(q.id)
        jsonout.append(j)
    return jsonout

def getallQuotesbyUser(phone):
    print "hi"
    if len(phone) !=10:
        return -1
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=usermodels.Profile.objects.filter(user=u[0])
    if len(profileobj)==0:
        return -2
    quoteobj = models.Quote.objects.filter(profile=profileobj[0])
    print len(quoteobj)
    jsonout=[]
    for q in quoteobj:
        j=getQuote(q.id)
        jsonout.append(j)
    return jsonout

def distance(lat1, lng1, lat2, lng2):
    #return distance as meter if you want km distance, remove "* 1000"
    radius = 6371 * 1000
    print "hi"
    dLat = (lat2-lat1) * math.pi / 180
    dLng = (lng2-lng1) * math.pi / 180
    print "hi"
    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    val = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLng/2) * math.sin(dLng/2) * math.cos(lat1) * math.cos(lat2)  
    print "hi"
    ang = 2 * math.atan2(math.sqrt(val), math.sqrt(1-val))
    return radius * ang

def searchQuotes(phone,subcategoryId):
    if len(phone) !=10:
        return -1
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -2
    profileobj=usermodels.Profile.objects.filter(user=u[0])
    if len(profileobj)==0:
        return -2
    subcategoryobj=categorymodels.Subcategory.objects.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    lat1 = profileobj[0].location.latitude
    lon1 = profileobj[0].location.longitude
    quoteobj = models.Quote.objects.filter(subcategory=subcategoryobj[0]).exclude(profile=profileobj[0])
    print len(quoteobj)
    jsonout=[]
    for q in quoteobj:
        d={}
        print "hi"
        lat2=q.profile.location.latitude
        print "hi"
        lon2 = q.profile.location.longitude
        print "hi"
        dis=distance(lat1,lon1,lat2,lon2)
        print "hi"
        ratingobj=models.Rating.objects.filter(profile=q.profile,subcategory=subcategoryobj[0])
        rating=ratingobj[0].rating
        d['quote']=getQuote(q.id)
        d['rating']=rating
        d['distance']=dis
        jsonout.append(d)
    jsonout.sort(key=operator.itemgetter('distance'))
    return jsonout
        
    
        
