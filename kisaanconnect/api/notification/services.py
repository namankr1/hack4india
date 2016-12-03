from . import models
from userprofile.models import Profile
from quotes.models import Quote
from userprofile import services
from quotes import services as quoteServices
from django.contrib.auth.models import User
def getuserid(phone):
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -1
    profileobj=Profile.objects.filter(user=u[0])
    return profileobj[0].id
def pushGovtNotification(title, description, url):
	govtnotification = models.GovtNotification(title = title, body = description, url = url)
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
	print "hi"
	accountNotification = models.AccountNotification.objects.filter(reciever =sender[0],sender=reciever[0],quote=quote[0])
	if len(accountNotification)==0:
		return -4
	print len(accountNotification)
	if status != 1 and status != -1:
		return -5
	accountNotification.update(sender=sender[0],reciever= reciever[0],status = status)
	return 1
