from . import models
from userprofile import services as userservices
from categorization import services as catservices
from categorization import models
from django.db.models import Q

def addQuote(phone,subcategoryId,type,quantity,price,description=None):
    if len(phone) !=10:
        return -1
    profileobj = models.Profile.filter(phone=username)
    if len(profileobj)==0:
        return -2
    subcategoryobj=models.Subcategory.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    quoteobj = models.Quote(profile = profileobj,subcategory = subcategoryobj,type=type,quantity = quantity, price= price,description = description,is_active=True)
    quoteobj.save()
    ratingobj=models.Rating.filter(profile=profileobj,subcategory=subcategoryobj)
    if len(ratingobj)==0:
        newobj=models.Rating(profile=profileobj,subcategory=subcategoryobj,rating=0)
        newobj.save()
    return 1

def getQuote(quoteId):
    quoteobj = models.Quote.filter(id=quoteId)
    if len(quoteobj)==0:
        return -1
    else:
        jsonout={}
        jsonout['id']=quoteobj[0].id
        jsonout['type']=quoteobj[0].type
        jsonout['quantity']=quoteobj[0].quantity
        jsonout['price']=quoteobj[0].price
        jsonout['description']=quoteobj[0].description
        jsonout['profile']=userservices.getProfile(quoteobj[0].profile.id)
        jsonout['subcategoryname']=quoteobj[0].subcategory.name
        jsonout['is_active']=quoteobj[0].is_active
        jsonout['bidvalue']=quoteobj[0].bidvalue
        ratingobj=models.Rating.filter(profile=profileobj,subcategory=subcategoryobj)
        jsonout['rating']=ratingobj[0].rating
        return jsonout

def deleteQuote(quoteId):
    quoteobj = models.Quote.filter(id=jsonin['quoteId'])
    if len(quoteobj)==0:
        return -1
    quoteobj[0].delete()

def updateQuote(jsonin):
    flag=0
    if 'quoteId' not in jsonin:
        return -1
    quoteobj = models.Quote.filter(id=jsonin['quoteId'])
    if len(quoteobj)==0:
        return -2
    if 'type' in jsonin:
        quoteobj.update(type=json['type'])
        flag=1
    if 'quantity' in jsonin:
        quoteobj.update(quantity=json['quantity'])
        flag=1
    if 'price' in jsonin:
        quoteobj.update(price=json['price'])
        flag=1
    if 'is_active' in jsonin:
        quoteobj.update(is_active=json['is_active'])
        flag=1
    if 'bidvalue' in jsonin:
        if quoteobj.bidvalue<jsonin['bidvalue']:
            quoteobj.update(bidvalue=json['bidvalue'])
            flag=1
    if flag==1:
        return 1
    else:
        return 0
        
def getQuotesbyUser(phone,subcategoryId):
    if len(phone) !=10:
        return -1
    profileobj = models.Profile.filter(phone=username)
    if len(profileobj)==0:
        return -2
    subcategoryobj=models.Subcategory.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    quoteobj = models.Quote.filter(profile=profileobj,subcategory=subcategoryobj)
    jsonout=[]
    for q in quoteobj:
        j=getQuote(q.id)
        jsonout.append(j)
    return jsonout

def distance(lat1, lng1, lat2, lng2):
    #return distance as meter if you want km distance, remove "* 1000"
    radius = 6371 * 1000
    dLat = (lat2-lat1) * math.pi / 180
    dLng = (lng2-lng1) * math.pi / 180
    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(lat1) * cos(lat2)    
    ang = 2 * atan2(sqrt(val), sqrt(1-val))
    return radius * ang

def searchQuotes(phone,subcategoryId):
    if len(phone) !=10:
        return -1
    profileobj = models.Profile.filter(phone=username)
    if len(profileobj)==0:
        return -2
    subcategoryobj=models.Subcategory.filter(id = subcategoryId)
    if len(subcategoryobj)==0:
        return -3
    lat1 = profileobj.location.latitude
    lon1 = profileobj.location.longitude
    quoteobj = models.Quote.filter(Q(subcategory=subcategoryobj) & ~Q(profile=profileobj))
    for q in quoteobj:
        lat2=q.profile.location.latitude
        lon2 = q.profile.location.longitude
        dis=distance(lat1,lon1,lat2,lon2)
        ratingobj=models.Rating.filter(profile=q.profile,subcategory=subcategoryobj)
        rating=ratingobj[0].rating
        
    
        
