from . import models
from userprofile.models import Profile
from quotes.models import Quote,Rating
from userprofile import services
from quotes import services as quoteServices
from django.contrib.auth.models import User
from categorization import services as categorizationServices
import math
import operator
def getuserid(phone):
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -1
    profileobj=Profile.objects.filter(user=u[0])
    return profileobj[0].id
def pushGovtNotification(title, description, url):
	govtnotification = models.GovtNotification(title = categorizationServices.translate(title), body = categorizationServices.translate(description), url = url)
	govtnotification.save()
	return 1

def getGovtNotifications():
	govtnotifications = models.GovtNotification.objects.all()
	jsonout = []
	for e in govtnotifications:
		d = {}
		d['id']=e.id
		d['title']=e.title
		d['body']=e.body
		d['url']=e.url
		jsonout.append(d)
	return jsonout
def raiseInterest(senderphone, recieverphone,quoteid,price,quantity):
    senderid = getuserid(senderphone)
    recieverid = getuserid(recieverphone)
    print "hi"
    sender = Profile.objects.filter(id = senderid)
    reciever = Profile.objects.filter(id = recieverid)
    if len(sender)==0:
        return -1
    if len(reciever) == 0:
        return -2
    quote = Quote.objects.filter(id = quoteid)
    if len(quote)==0:
        return -3
    accountNotification = models.AccountNotification(sender = sender[0], reciever = reciever[0], quote = quote[0],price = price,quantity = quantity,status = 0)
    accountNotification.save()
    if price>quote[0].bidvalue:
        quote.update(bidvalue=price)
    return 1

def getNotifications(phone):
    userid = getuserid(phone)
    user = Profile.objects.filter(id = userid)
    if len(user)==0:
        return -1
    notifications = models.AccountNotification.objects.filter(reciever = user)
    jsonout=[]
    for n in notifications:
        d={}
        d['id']=n.id
        d['sender'] = services.getProfile({'userid':n.sender.id})
        #d['quote'] = quoteServices.getQuote(n.quote.id)
        d['quoteid'] = n.quote.id
        d['type'] = n.quote.type
        d['price'] = n.price
        d['quantity'] = n.quantity
        d['status'] = n.status
        jsonout.append(d)
    return jsonout

def negotiate(senderphone, recieverphone,quoteid,price,quantity):
	print "hi"
	senderid = getuserid(senderphone)
	recieverid = getuserid(recieverphone)
	sender1 = Profile.objects.filter(id = senderid)
	reciever1 = Profile.objects.filter(id = recieverid)
	print "hi"
	if len(sender1)==0:
		return -1
	if len(reciever1) == 0:
		return -2
	quote1 = Quote.objects.filter(id = quoteid)
	if len(quote1)==0:
		return -3
	print "hi"
	accountNotification = models.AccountNotification.objects.filter(reciever=sender1[0],sender=reciever1[0],quote=quote1[0])
	if len(accountNotification)==0:
		return -4
	print "hi"
	accountNotification.update(sender=sender1[0],reciever= reciever1[0],price=price,quantity=quantity)
	return 1

def endNegotiation(senderphone, recieverphone,quoteid,status):
    print "hi"
    senderid = getuserid(senderphone)
    recieverid = getuserid(recieverphone)
    sender = Profile.objects.filter(id = senderid)
    reciever = Profile.objects.filter(id = recieverid)
    if len(sender)==0:
        return -1
    if len(reciever) == 0:
		return -2
    quote = Quote.objects.filter(id = quoteid)
    if len(quote)==0:
		return -3
    accountNotification = models.AccountNotification.objects.filter(reciever =sender[0],sender=reciever[0],quote=quote[0])
    if len(accountNotification)==0:
        return -4
    print len(accountNotification)
    temp1=accountNotification[0].quantity
    if status != 1 and status != -1:
        return -5
    accountNotification.update(sender=sender[0],reciever= reciever[0],status = status)
    if status == 1:
        quote[0].quantity = quote[0].quantity - temp1
        quote[0].save()
    ratingobj=Rating.objects.filter(profile=quote[0].profile,subcategory=quote[0].subcategory)
    if len(ratingobj)!=0:
        ratingobj[0].rating = ratingobj[0].rating + 1
        ratingobj[0].save()
    return 1
def getNegotiationsOfUser(phone):
    userid = getuserid(phone)
    user = Profile.objects.filter(id = userid)
    if len(user)==0:
        return -1
    negotiations1 = models.AccountNotification.objects.filter(reciever = user).exclude(status=1).exclude(status=-1)
    negotiations2 = models.AccountNotification.objects.filter(sender = user).exclude(status=1).exclude(status=-1)
    print "hi"
    jsonout=[]
    for n in negotiations1:
        d={}
        d['id']=n.id
        d['sender'] = services.getProfile({'userid':n.sender.id})
        #d['quote'] = quoteServices.getQuote(n.quote.id)
        d['quoteid'] = n.quote.id
        d['type'] = n.quote.type
        d['price'] = n.price
        d['quantity'] = n.quantity
        d['status'] = "1"
        jsonout.append(d)
    for n in negotiations2:
        d={}
        d['id']=n.id
        d['sender'] = services.getProfile({'userid':n.reciever.id})
        #d['quote'] = quoteServices.getQuote(n.quote.id)
        d['quoteid'] = n.quote.id
        d['type'] = n.quote.type
        d['price'] = n.price
        d['quantity'] = n.quantity
        d['status'] = "2"
        jsonout.append(d)
    return jsonout

def getOrdersOfUser(phone):
    userid = getuserid(phone)
    user = Profile.objects.filter(id = userid)
    if len(user)==0:
        return -1
    negotiations1 = models.AccountNotification.objects.filter(reciever = user,status=1)
    negotiations2 = models.AccountNotification.objects.filter(sender = user,status=1)
    print "hi"
    jsonout=[]
    for n in negotiations1:
        d={}
        d['id']=n.id
        d['sender'] = services.getProfile({'userid':n.sender.id})
        #d['quote'] = quoteServices.getQuote(n.quote.id)
        d['quoteid'] = n.quote.id
        d['type'] = n.quote.type
        d['price'] = n.price
        d['quantity'] = n.quantity
        d['status'] = "1"
        jsonout.append(d)
    for n in negotiations2:
        d={}
        d['id']=n.id
        d['sender'] = services.getProfile({'userid':n.reciever.id})
        #d['quote'] = quoteServices.getQuote(n.quote.id)
        d['quoteid'] = n.quote.id
        d['type'] = n.quote.type
        d['price'] = n.price
        d['quantity'] = n.quantity
        d['status'] = "2"
        jsonout.append(d)
    return jsonout

def distance(lat1, lng1, lat2, lng2):
    #return distance as meter if you want km distance, remove "* 1000"
    radius = 6371
    dLat = (lat2-lat1) * math.pi / 180
    dLng = (lng2-lng1) * math.pi / 180
    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    val = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLng/2) * math.sin(dLng/2) * math.cos(lat1) * math.cos(lat2)  
    ang = 2 * math.atan2(math.sqrt(val), math.sqrt(1-val))
    return radius * ang

def nearbyusers(user1):
    users = Profile.objects.filter().exclude(user = user1.user)
    lat2 = user1.location.latitude
    long2 = user1.location.longitude
    usersnearby = []
    for u in users:
        lat1 = u.location.latitude
        long1 = u.location.longitude
        dis = distance(lat1,long1,lat2,long2)
        if dis < 113350:
            usersnearby.append(u)
    return usersnearby


def whatOthersSell(quotesnearby,subcategories):
    jsonout = []
    for subcategory in subcategories:
        d = {}
        d["subcategoryid"] = subcategory["id"]
        d["subcategoryname"] = subcategory["name"]
        p=[]
        for q in quotesnearby:
            print q
            if q.subcategory.id != subcategory["id"]:
                p.append(q)
        
        if len(quotesnearby) != 0 :
            percentOfQuotesInSubCategory = (float(len(quotesnearby) - len(p))/len(quotesnearby))*100.0
        else:
            percentOfQuotesInSubCategory = 'Nil'
        d["percent"] = percentOfQuotesInSubCategory
        jsonout.append(d)
    print jsonout

    return jsonout


def whatOthersBuy(subcategories,usersnearby):
    jsonout = []
    quotes = []
    for u in usersnearby:
        boughtproducts1 = models.AccountNotification.objects.filter(status=1,sender = u)
        boughtproducts2 = models.AccountNotification.objects.filter(status=1,reciever = u)
        for b in boughtproducts1:
            quotes.append(b.quote)
        for b in boughtproducts2:
            quotes.append(b.quote)
    jsonout = whatOthersSell(quotes,subcategories)
    return jsonout

def percentpricechange(quotesnearby,bidvalue,subcategories):
    jsonout = []
    for subcategory in subcategories:
        d = {}
        d["subcategoryid"] = subcategory["id"]
        d["subcategoryname"] = subcategory["name"]
        p=[]
        sr = 0
        sb = 0
        percentprice = 0
        i=0
        for q in quotesnearby:
            print q
            if q.subcategory.id == subcategory["id"]:
                print "-----"+str(bidvalue[i])
                sr = sr + q.price
                sb = sb + bidvalue[i]
            i=i+1
        print sr 
        print sb
        if sr !=0:
            percentprice = math.ceil(((sb - sr)/sr)*100)
        else:
            percentprice = 'Nil'
        d["percent"] = percentprice
        jsonout.append(d)
    return jsonout


def pricechangeSubcategories(subcategories,usersnearby):
    jsonout = []
    quotes = []
    bidvalue = []
    for u in usersnearby:
        boughtproducts1 = models.AccountNotification.objects.filter(status=1,sender = u)
        boughtproducts2 = models.AccountNotification.objects.filter(status=1,reciever = u)
        for b in boughtproducts1:
            quotes.append(b.quote)
            bidvalue.append(b.price)
        for b in boughtproducts2:
            quotes.append(b.quote)
            bidvalue.append(b.price)
    jsonout = percentpricechange(quotes,bidvalue,subcategories)
    return jsonout

def recommendation(p,q,r,n):
    x = []
    for i in xrange(n):
        point = 0
        if p[i]["subcategoryid"] == q[i]["subcategoryid"] and p[i]["subcategoryid"] == r[i]["subcategoryid"]:
            d={}
            d["subcategoryid"] = p[i]["subcategoryid"]
            d["subcategoryname"] = p[i]["subcategoryname"]
            l = p[i]["percent"]
            m = q[i]["percent"]
            n = r[i]["percent"]
            if p[i]["percent"]=="Nil":
                l = 0
            if q[i]["percent"]=="Nil":
                m = 0
            if r[i]["percent"]=="Nil":
                n = 0
            point = l+m+n
            d["point"] = point 
            x.append(d)
    x.sort(key=operator.itemgetter('point'))
    x.reverse()
    return x

def marketInsights(phone):
    userid = getuserid(phone)
    user = Profile.objects.filter(id = userid)
    if len(user)==0:
        return -1
    print "ji1"
    usersnearby = nearbyusers(user[0])
    print "ji"
    quotesnearby = []
    for u in usersnearby:
        quotes = Quote.objects.filter(profile=u)
        if len(quotes)!=0:
            quotesnearby.append(quotes[0])
    categories = categorizationServices.getCategories()
    jsonout = []
    for category in categories:
        subcategories = categorizationServices.getSubcategories(category["id"])
        d={}
        print "ji"
        d["category"] = category
        d["subcategories"] = subcategories
        p = whatOthersSell(quotesnearby,subcategories)
        d["whatOthersSell"] = p
        q = whatOthersBuy(subcategories,usersnearby)
        d["whatOthersBuy"] = q
        r = pricechangeSubcategories(subcategories,usersnearby)
        d["pricechange"] = r
        t = recommendation(p,q,r,len(subcategories))
        d["recommendation"] = t
        jsonout.append(d)
    return jsonout


