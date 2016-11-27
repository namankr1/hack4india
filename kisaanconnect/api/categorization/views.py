from django.shortcuts import render
import json
from django.http import JsonResponse
from . import services
# Create your views here.

def getcategories(request):
    if request.method == 'GET':
        result=0
        try:
            result = services.getCategories()
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == 0:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem'})
        else:
            return JsonResponse({'status' : 'ok', 'categories' : result })
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def getsubcategories(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin=json.loads(request.body)
            print jsonin['categoryid']
            result = services.getSubcategories(jsonin['categoryid'])
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem'})
        else:
            return JsonResponse({'status' : 'ok', 'subcategories' : result })
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request'})

def addcategories(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.addCategories(jsonin['name'],jsonin['description'])
		except:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result ==1 :
			return JsonResponse({'status':'ok', 'message':'Successfully added category'})
def addsubcategories(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.addSubCategories(json['name'],json['description'],json['categoryid'])
		except:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result ==1 :
			return JsonResponse({'status':'ok', 'message':'Successfully added category'})
		elif result == -1:
			return JsonResponse({'status':'err','message':'Category id given is invalid'})

