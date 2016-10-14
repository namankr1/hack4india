from django.shortcuts import render
from . import services
# Create your views here.
def addquote(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin = json.loads(request.body)
            if 'description' in jsonin:
                result = services.addQuote(jsonin['phone'],jsonin['subcategoryId'], jsonin['type'],jsonin['quantity'],jsonin['price'],jsonin['description'])
            else:
                result = services.addQuote(jsonin['phone'],jsonin['subcategoryId'], jsonin['type'],jsonin['quantity'],jsonin['price'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Phone number is invalid'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Mobile number is not registered'})
        elif result == -3:
            return JsonResponse({'status' : 'err', 'message' : 'Sub category ID doesnot exist'})
        elif result == 1:
            return JsonResponse({'status' : 'ok', 'message' : 'Successfully added quote'})
        else:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem'})
    else:
    	return JsonResponse({'status':'err', 'message': 'Bad request'})

def getquote(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.getQuote(jsonin['quoteId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result ==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Quote Id does not exist'})
        else:
            return JsonResponse({'status':'ok', 'quote':result})
    else:
    	return JsonResponse({'status':'err', 'message':'Bad request'})

def getquotebyuser(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.getQuotebyUser(jsonin['phone'],jsonin['subcategoryId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result ==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Phone number is invalid'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Mobile number is not registered'})
        elif result == -3:
            return JsonResponse({'status' : 'err', 'message' : 'Sub category not found'})
        else:
            return JsonResponse({'status':'ok', 'quote':result})
    else:
    	return JsonResponse({'status':'err', 'message':'Bad request'})

def deletequote(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin = json.loads(request.body)
            result = services.deleteQuote(jsonin['quoteId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status' : 'err', 'message' : 'Quote Id does not exist'})
        else:
            return JsonResponse({'status' : 'ok', 'message' : 'Successfully deleted quote'})
    else:
    	return JsonResponse({'status':'err', 'message':'Bad request'})

def updatequote(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.updateQuote(jsonin)
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result == -1:
            return JsonResponse({'status' : 'err', 'message' : 'Quote Id does not exist in input'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Quote Id does not exist in database'})
        elif result == 0:
            return JsonResponse({'status' : 'ok', 'message' : 'No update performed'})
        else:
            return JsonResponse({'status' : 'ok', 'message' : 'Updated data successfully'})
    else:
    	return JsonResponse({'status':'err', 'message':'Bad request'})

def searchquotes(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.searchQuotes(jsonin['phone'],jsonin['subcategoryId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid'})
        if result == 0:
            return JsonResponse({'status':'err','message':'Server encountered a problem'})
        else:
            return JsonResponse({'status':'ok','results':result})
    else:
        return JsonResponse({'status':'err','message':'Bad request'})


        
            