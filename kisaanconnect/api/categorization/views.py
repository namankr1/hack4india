# -*- coding: utf-8 -*-
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
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result == 0:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
        else:
            return JsonResponse({'status' : 'ok', 'categories' : result })
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getsubcategories(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin=json.loads(request.body)
            print jsonin['categoryid']
            result = services.getSubcategories(jsonin['categoryid'])
        except Exception:
            return JsonResponse({'status':'err', 'message': 'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result == -1:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
        else:
            return JsonResponse({'status' : 'ok', 'subcategories' : result })
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def addcategories(request):
	if request.method == 'POST':
		result = 0
		# try:
		jsonin = json.loads(request.body)
		result = services.addCategories(jsonin['name'],jsonin['description'])
		# except:
		# 	return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result ==1 :
			return JsonResponse({'status':'ok', 'message':'Successfully added category'})
def addsubcategories(request):
	if request.method == 'POST':
		result = 0
		# try:
		jsonin = json.loads(request.body)
		result = services.addSubCategories(jsonin['name'],jsonin['description'],jsonin['categoryid'])
		# except:
		# 	return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		if result ==1 :
			return JsonResponse({'status':'ok', 'message':'Successfully added category'})
		elif result == -1:
			return JsonResponse({'status':'err','message':'Category id given is invalid'})

