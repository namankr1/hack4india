from django.shortcuts import render
import json
from django.http import JsonResponse
from . import services

def pushgovtnotification(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.pushGovtNotification(jsonin['title'],jsonin['description'],jsonin['url'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result ==1:
			return JsonResponse({'status':'ok','message':'Message successfully broadcasted to all users'})
	else:
		return JsonResponse({'status':'err','message':'Bad request'})

def getgovtnotifications(request):
	if request.method == 'GET':
		result = 0
		try:
			result = services.getGovtNotifications()
		except Exception:
			return JsonResponse({'status':'err','message':'Server encountered a problem. Try refreshing again'})
		return JsonResponse({'status':'ok','govtNotifications':result})
	else:
		return JsonResponse({'status':'err','message':'Bad request'})

def raiseinterest(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.raiseInterest(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['price'],jsonin['quantity'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Interest is successfully recorded'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered a problem'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request'})

def getnotifications(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.getNotifications(jsonin['phone'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to the server is invalid'})
		if result == 0:
			return JsonResponse({'status':'err','message':'Server encountered a problem'})
		else:
			return JsonResponse({'status':'ok', 'notifications':result})
	else:
		return JsonResponse({'status':'err','message':'Bad request'})

def negotiate(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.negotiate(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['price'],jsonin['quantity'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid'})
		elif result == -4:
			return JsonResponse({'status':'err','message':'Deal is not initialized yet'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Negotiation successful'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered a problem'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request'})

def endnegotiation(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.endNegotiation(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['status'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid'})
		elif result == -4:
			return JsonResponse({'status':'err','message':'Deal is not initialized yet'})
		elif result == -5:
			return JsonResponse({'status':'err','message':'Status code invalid'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Negotiation terminated'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered a problem'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request'})
