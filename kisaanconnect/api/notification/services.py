from . import models
from userprofile.models import Profile
from quotes.models import Quote
from userprofile import services
from quotes import services as quoteServices
def getuserid(phone):
    u=User.objects.filter(username='I'+str(phone))
    if len(u)==0:
        return -1
    profileobj=models.Profile.objects.filter(user=u[0])
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
	sender = Profile.objects.filter(id = senderid)
	reciever = Profile.objects.filter(id = recieverid)
	qu
	if len(sender)==0:
		return -1
	if len(reciever) == 0:
		return -2
	quote = Quote.objects.filter(id = quoteid)
	if len(quote)==0:
		return -3
	accountNotification = models.AccountNotification(sender = sender[0], reciever = reciever[0], quote = quote[0],price = price,quantity = quantity,status = 1)
	accountNotification.save()
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
		d['reciever'] = services.getProfile({'userid':n.reciever.id})
		d['quote'] = quoteServices.getQuote(n.quote.id)
		d['price'] = n.price
		d['quantity'] = n.quantity
		jsonout.append(d)
	return jsonout

def negotiate(senderphone, recieverphone,quoteid,price,quantity):
    senderid = getuserid(senderphone)
    recieverid = getuserid(recieverphone)
	sender = Profile.objects.filter(id = senderid)
	reciever = Profile.objects.filter(id = recieverid)
	qu
	if len(sender)==0:
		return -1
	if len(reciever) == 0:
		return -2
	quote = Quote.objects.filter(id = quoteid)
	if len(quote)==0:
		return -3
	accountNotification = models.AccountNotification.filter(sender =sender,reciever=reciever,quote=quote)
	if len(accountNotification)==0:
		return -4
	accountNotification.update(price=price,quantity=quantity)
	accountNotification.save()
	return 1

def endNegotiation(senderphone, recieverphone,quoteid,status):
    senderid = getuserid(senderphone)
    recieverid = getuserid(recieverphone)
	sender = Profile.objects.filter(id = senderid)
	reciever = Profile.objects.filter(id = recieverid)
	qu
	if len(sender)==0:
		return -1
	if len(reciever) == 0:
		return -2
	quote = Quote.objects.filter(id = quoteid)
	if len(quote)==0:
		return -3
	accountNotification = models.AccountNotification.filter(sender =sender,reciever=reciever,quote=quote)
	if len(accountNotification)==0:
		return -4
	if status != 1 and status != -1:
		return -5
	accountNotification[0].update(status = status)
	accountNotification[0].save()
	return 1
