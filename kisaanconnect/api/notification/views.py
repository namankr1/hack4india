# -*- coding: utf-8 -*-
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
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		return JsonResponse({'status':'ok','govtNotifications':result})
	else:
		return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def raiseinterest(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.raiseInterest(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['price'],jsonin['quantity'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid;प्रेषक प्रोफ़ाइल आईडी अमान्य है;প্রেরকের প্রোফাইল আইডি অবৈধ;పంపినవారు ప్రొఫైల్ ID చెల్లదు;प्रेषक प्रोफाइल ID अवैध आहे;அனுப்புநர் சுயவிவர ஐடி தவறானது;مرسل پروفائل ID غلط ہے;પ્રેષક પ્રોફાઇલ ID ને અમાન્ય છે;ಕಳುಹಿಸಿದವರ ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;പ്രേഷിതനാമം പ്രൊഫൈൽ ID അസാധുവാണ്;ਪ੍ਰੇਸ਼ਕ ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;प्रेषक प्रोफाइल आईडी अमान्य छ;مرسل سلامت سڃاڻپ غلط آهي'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid;रिसीवर प्रोफ़ाइल आईडी अमान्य है;Reciever প্রোফাইল আইডি অবৈধ;తీసుకొను ప్రొఫైల్ ID చెల్లదు;Reciever प्रोफाइल ID अवैध आहे;Reciever சுயவிவர ஐடி தவறானது;reciever کے پروفائل ID غلط ہے;Reciever પ્રોફાઇલ ID ને અમાન્ય છે;Reciever ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;Reciever പ്രൊഫൈൽ ID അസാധുവാണ്;Reciever ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;Reciever प्रोफाइल आईडी अमान्य छ;Reciever سلامت سڃاڻپ غلط آهي'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Interest is successfully recorded;ब्याज सफलतापूर्वक दर्ज की गई है;সুদের সফলভাবে রেকর্ড করা হয়;వడ్డీ విజయవంతంగా నమోదయింది;व्याज यशस्वीरित्या रेकॉर्ड केले आहे;வட்டி வெற்றிகரமாக பதிவு செய்யப்பட்டுள்ளது;دلچسپی کامیابی سے ریکارڈ کیا جاتا ہے;વ્યાજ સફળતાપૂર્વક રેકોર્ડ છે;ಬಡ್ಡಿ ಯಶಸ್ವಿಯಾಗಿ ದಾಖಲಿಸಲಾಗಿದೆ;പലിശ വിജയകരമായി രേഖപ്പെടുത്തിയിരിക്കുന്നു;ਵਿਆਜ ਸਫਲਤਾਪੂਰਕ ਦਰਜ ਹੈ;ब्याज सफलतापूर्वक रेकर्ड गरिएको छ;فائدي ڪاميابي رڪارڊ آهي'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getnotifications(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.getNotifications(jsonin['phone'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == 0:
			return JsonResponse({'status':'err','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
		else:
			return JsonResponse({'status':'ok', 'notifications':result})
	else:
		return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def negotiate(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.negotiate(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['price'],jsonin['quantity'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid;प्रेषक प्रोफ़ाइल आईडी अमान्य है;প্রেরকের প্রোফাইল আইডি অবৈধ;పంపినవారు ప్రొఫైల్ ID చెల్లదు;प्रेषक प्रोफाइल ID अवैध आहे;அனுப்புநர் சுயவிவர ஐடி தவறானது;مرسل پروفائل ID غلط ہے;પ્રેષક પ્રોફાઇલ ID ને અમાન્ય છે;ಕಳುಹಿಸಿದವರ ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;പ്രേഷിതനാമം പ്രൊഫൈൽ ID അസാധുവാണ്;ਪ੍ਰੇਸ਼ਕ ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;प्रेषक प्रोफाइल आईडी अमान्य छ;مرسل سلامت سڃاڻپ غلط آهي'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid;रिसीवर प्रोफ़ाइल आईडी अमान्य है;Reciever প্রোফাইল আইডি অবৈধ;తీసుకొను ప్రొఫైల్ ID చెల్లదు;Reciever प्रोफाइल ID अवैध आहे;Reciever சுயவிவர ஐடி தவறானது;reciever کے پروفائل ID غلط ہے;Reciever પ્રોફાઇલ ID ને અમાન્ય છે;Reciever ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;Reciever പ്രൊഫൈൽ ID അസാധുവാണ്;Reciever ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;Reciever प्रोफाइल आईडी अमान्य छ;Reciever سلامت سڃاڻپ غلط آهي'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
		elif result == -4:
			return JsonResponse({'status':'err','message':'Deal is not initialized yet;सौदा अभी तक आरंभ नहीं है;ডীল এখনো শুরু করা হয়নি;డీల్ ఇంకా initialized లేదు;करार अद्याप आरंभ केलेला नाही;ஒப்பந்தம் இன்னும் தொடங்கப்படவில்லை;سودا نے ابھی سے initialized نہیں ہے;ડીલ હજુ સુધી નથી આરંભ છે;ಡೀಲ್ ಇನ್ನೂ ಆರಂಭಿಸಲಾಗಿಲ್ಲ;മുളയങ്കാവ് ഇതുവരെ സമാരംഭിച്ചിട്ടില്ല;ਡੀਲ ਅਜੇ ਤੱਕ ਸ਼ੁਰੂ ਨਾ ਕੀਤਾ ਗਿਆ ਹੈ;सम्झौता अझै आरम्भ भएको छैन;ڊيل موجود initialized نه آهي'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Negotiation successful;बातचीत सफल;আলোচনার মাধ্যমে সফল;నెగోషియేషన్ విజయవంతమైన;बोलणी यशस्वी;வெற்றிகரமான பேச்சுவார்த்தைத்;کامیاب مذاکرات;નેગોશીયેશન સફળ;ಸಮಾಲೋಚನಾ ಯಶಸ್ವಿ;കൂടിയാലോചന വിജയകരം;ਗੱਲਬਾਤ ਸਫਲ;वार्ता सफल;ڳالهين ڪامياب'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def endnegotiation(request):
	if request.method == 'POST':
		result = 0
		try:
			jsonin = json.loads(request.body)
			result = services.endNegotiation(jsonin['senderphone'],jsonin['recieverphone'],jsonin['quoteid'],jsonin['status'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == -1:
			return JsonResponse({'status':'err','message':'Sender profile ID is invalid;प्रेषक प्रोफ़ाइल आईडी अमान्य है;প্রেরকের প্রোফাইল আইডি অবৈধ;పంపినవారు ప్రొఫైల్ ID చెల్లదు;प्रेषक प्रोफाइल ID अवैध आहे;அனுப்புநர் சுயவிவர ஐடி தவறானது;مرسل پروفائل ID غلط ہے;પ્રેષક પ્રોફાઇલ ID ને અમાન્ય છે;ಕಳುಹಿಸಿದವರ ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;പ്രേഷിതനാമം പ്രൊഫൈൽ ID അസാധുവാണ്;ਪ੍ਰੇਸ਼ਕ ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;प्रेषक प्रोफाइल आईडी अमान्य छ;مرسل سلامت سڃاڻپ غلط آهي'})
		elif result == -2:
			return JsonResponse({'status':'err','message':'Reciever profile ID is invalid;रिसीवर प्रोफ़ाइल आईडी अमान्य है;Reciever প্রোফাইল আইডি অবৈধ;తీసుకొను ప్రొఫైల్ ID చెల్లదు;Reciever प्रोफाइल ID अवैध आहे;Reciever சுயவிவர ஐடி தவறானது;reciever کے پروفائل ID غلط ہے;Reciever પ્રોફાઇલ ID ને અમાન્ય છે;Reciever ಪ್ರೊಫೈಲ್ ID ಅಮಾನ್ಯವಾಗಿದೆ;Reciever പ്രൊഫൈൽ ID അസാധുവാണ്;Reciever ਪਰੋਫਾਇਲ ID ਗਲਤ ਹੈ;Reciever प्रोफाइल आईडी अमान्य छ;Reciever سلامت سڃاڻپ غلط آهي'})
		elif result == -3:
			return JsonResponse({'status':'err','message':'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
		elif result == -4:
			return JsonResponse({'status':'err','message':'Deal is not initialized yet;सौदा अभी तक आरंभ नहीं है;ডীল এখনো শুরু করা হয়নি;డీల్ ఇంకా initialized లేదు;करार अद्याप आरंभ केलेला नाही;ஒப்பந்தம் இன்னும் தொடங்கப்படவில்லை;سودا نے ابھی سے initialized نہیں ہے;ડીલ હજુ સુધી નથી આરંભ છે;ಡೀಲ್ ಇನ್ನೂ ಆರಂಭಿಸಲಾಗಿಲ್ಲ;മുളയങ്കാവ് ഇതുവരെ സമാരംഭിച്ചിട്ടില്ല;ਡੀਲ ਅਜੇ ਤੱਕ ਸ਼ੁਰੂ ਨਾ ਕੀਤਾ ਗਿਆ ਹੈ;सम्झौता अझै आरम्भ भएको छैन;ڊيل موجود initialized نه آهي'})
		elif result == -5:
			return JsonResponse({'status':'err','message':'Status code invalid;स्थिति कोड अमान्य;স্থিতি কোড অবৈধ;స్థితి కోడ్ చెల్లదు;स्थिती कोड अवैध;நிலை குறியீடு தவறான;حیثیت کوڈ ناموزوں;સ્થિતિ કોડ અમાન્ય;ಸ್ಥಿತಿ ಕೋಡ್ ಅಮಾನ್ಯವಾಗಿದೆ;സ്റ്റാറ്റസ് കോഡ് അസാധുവാണ്;ਹਾਲਤ ਕੋਡ ਗਲਤ;स्थिति कोड अमान्य;اسٽيٽس ڪوڊ غلط'})
		elif result == 1:
			return JsonResponse({'status':'ok','message':'Negotiation terminated;निगोसिएशन समाप्त;আলোচনার মাধ্যমে সমাপ্ত;నెగోషియేషన్ రద్దు;बोलणी निरस्त;பேச்சுவார்த்தைத் நிறுத்தப்பட்டது;مذاکرات معطل کردیے;નેગોશીયેશન સમાપ્ત;ಸಮಾಲೋಚನಾ ರದ್ದು;കൂടിയാലോചന അവസാനിപ്പിച്ചു;ਗੱਲਬਾਤ ਸਮਾਪਤ;वार्ता समाप्त;ڳالهين ختم'})
		else:
			return JsonResponse({'status':'ok','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
	else:
		return JsonResponse({'status':'ok','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getnegotiationsofuser(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.getNegotiationsOfUser(jsonin['phone'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == 0:
			return JsonResponse({'status':'err','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
		else:
			return JsonResponse({'status':'ok', 'negotiations':result})
	else:
		return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getordersofuser(request):
	if request.method == 'POST':
		result=0
		try:
			jsonin = json.loads(request.body)
			result = services.getOrdersOfUser(jsonin['phone'])
		except Exception:
			return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
		if result == 0:
			return JsonResponse({'status':'err','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
		else:
			return JsonResponse({'status':'ok', 'negotiations':result})
	else:
		return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getmarketinsights(request):
	if request.method == 'POST':
		result=0
		# try:
		jsonin = json.loads(request.body)
		result = services.marketInsights(jsonin['phone'])
		# except Exception:
		# 	return JsonResponse({'status':'err','message':'Data given to the server is invalid'})
		if result == 0:
			return JsonResponse({'status':'err','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
		else:
			return JsonResponse({'status':'ok', 'insights':result})
	else:
		return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})