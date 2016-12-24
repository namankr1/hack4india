# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from . import services
import json
# Create your views here.
def addquote(request):
    if request.method == 'POST':
        result=0
        try:
            
            jsonin = json.loads(request.body)
            
            if 'description' in jsonin:
                print "ko"
                result = services.addQuote(jsonin['phone'],jsonin['subcategoryId'], jsonin['type'],jsonin['quantity'],jsonin['price'],jsonin['description'])
            else:
                result = services.addQuote(jsonin['phone'],jsonin['subcategoryId'], jsonin['type'],jsonin['quantity'],jsonin['price'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Phone number is invalid;फ़ोन नंबर अमान्य है;ফোন নম্বর অবৈধ;ఫోన్ నంబర్ చెల్లదు;फोन नंबर अवैध आहे;தொலைபேசி எண் தவறானது;فون نمبر غلط ہے;ફોન નંબર અમાન્ય છે;ಫೋನ್ ಸಂಖ್ಯೆ ಅಮಾನ್ಯವಾಗಿದೆ;ഫോൺ നമ്പർ അസാധുവാണ്;ਫੋਨ ਨੰਬਰ ਗਲਤ ਹੈ;फोन नम्बर अवैध छ;فون نمبر غلط آهي'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Mobile number is not registered;मोबाइल नंबर पंजीकृत नहीं है;মোবাইল নম্বর নিবন্ধিত না হয়;మీ మైబైల్ నెంబర్ నమోదు కాలేదు;मोबाइल क्रमांक नोंदणीकृत नाही;மொபைல் எண் பதிவு இல்லை;موبائل نمبر دار نہیں ہے;મોબાઇલ નંબર રજીસ્ટર થયેલ નથી;ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನೋಂದಣಿಯಾಗಿಲ್ಲ;മൊബൈൽ നമ്പർ രജിസ്റ്റർ ചെയ്തിട്ടില്ല;ਮੋਬਾਈਲ ਨੰਬਰ ਦੀ ਰਜਿਸਟਰ ਕੀਤਾ ਹੈ, ਨਾ ਹੈ,;मोबाइल नम्बर दर्ता गरिएको छैन;موبائل نمبر داخل نه آهي'})
        elif result == -3:
            return JsonResponse({'status' : 'err', 'message' : 'Sub-category ID doesnot exist;उप-श्रेणी आईडी doesnot मौजूद;উপ-বিভাগ আইডি doesnot অস্তিত্ব;ఉప వర్గం ID doesnot ఉనికిలో;उप-श्रेणी आयडी doesnot अस्तित्वात;சப்-வகை அடையாள doesnot உள்ளன;ذیلی قسم کی شناخت سے doesnot موجود;પેટા શ્રેણી ને doesnot છે અસ્તિત્વ ધરાવે છે;ಉಪ ವರ್ಗದಲ್ಲಿ ID ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ ಅಸ್ತಿತ್ವದಲ್ಲಿವೆ;ഉപ വിഭാഗം ഐഡി ഉള്ക്കൊള്ളുന്ന നിലവിലില്ല;ਸਬ-ਸ਼੍ਰੇਣੀ ਦਾ ID doesnot ਮੌਜੂਦ;उप-श्रेणी आईडी doesnot अवस्थित;سب درجي جي ID doesnot موجود'})
        elif result == -4:
        	return JsonResponse({'status' : 'err', 'message' : 'Quotation of this sub-category already exists;इस उप-श्रेणी के उद्धरण पहले से मौजूद है;এই উপ-বিভাগ এর উদ্ধৃতি আগে থেকেই আছে;ఈ ఉప వర్గం యొక్క కొటేషన్ ఇప్పటికే ఉంది;या उप-श्रेणी अवतरण आधिपासूनच अस्तित्वात आहे;இந்த துணை வகை மேற்கோளைக் ஏற்கனவே உள்ளது;اس ذیلی زمرہ کے کوٹیشن پہلے سے موجود ہے;આ ઉપ-શ્રેણી ઓફ અવતરણ પહેલેથી હાજર જ છે;ಈ ಉಪ ವರ್ಗದಲ್ಲಿ ಉದ್ಧರಣ ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿದೆ;ഈ ഉപ-വിഭാഗത്തിലെ ക്വട്ടേഷൻ ഇതിനകം നിലവിലുണ്ട്;ਇਸ ਸਬ-ਸ਼੍ਰੇਣੀ ਦੇ ਕੁਟੇਸ਼ਨ ਹੀ ਮੌਜੂਦ ਹੈ;यस उप-श्रेणी को उद्धरण पहिले नै अवस्थित;هن جي ذيلي درجي جو Quotation ڏيندو اڳ ۾ ئي موجود آهي'})
        elif result == 1:
            return JsonResponse({'status' : 'ok', 'message' : 'Successfully added quotation;सफलता पूर्वक जोड़ उद्धरण;সফলভাবে যোগ উদ্ধৃতি;విజయవంతంగా జోడించారు కొటేషన్;यशस्वीरित्या जोडले अवतरण;வெற்றிகரமாக சேர்க்கப்பட்டது மேற்கோள்;کامیابی سے شامل کوٹیشن;સફળતાપૂર્વક ઉમેરી અવતરણ;ಯಶಸ್ವಿಯಾಗಿ ಸೇರಿಸಲಾಗಿದೆ ಉದ್ಧರಣ;വിജയകരമായി ചേർത്തു ഉദ്ധരണി;ਸਫਲਤਾਪੂਰਕ ਸ਼ਾਮਿਲ ਕੀਤਾ ਹਵਾਲੇ;सफलतापूर्वक थपियो उद्धरण;ڪاميابي سان شامل Quotation ڏيندو'})
        else:
            return JsonResponse({'status' : 'err', 'message' : 'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
    else:
    	return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getquote(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.getQuote(jsonin['quoteId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result ==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
        else:
            return JsonResponse({'status':'ok', 'quote':result})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getquotebyuser(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            print "ko"
            result = services.getQuotesbyUser(jsonin['phone'],jsonin['subcategoryId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Phone number is invalid;फ़ोन नंबर अमान्य है;ফোন নম্বর অবৈধ;ఫోన్ నంబర్ చెల్లదు;फोन नंबर अवैध आहे;தொலைபேசி எண் தவறானது;فون نمبر غلط ہے;ફોન નંબર અમાન્ય છે;ಫೋನ್ ಸಂಖ್ಯೆ ಅಮಾನ್ಯವಾಗಿದೆ;ഫോൺ നമ്പർ അസാധുവാണ്;ਫੋਨ ਨੰਬਰ ਗਲਤ ਹੈ;फोन नम्बर अवैध छ;فون نمبر غلط آهي'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Mobile number is not registered;मोबाइल नंबर पंजीकृत नहीं है;মোবাইল নম্বর নিবন্ধিত না হয়;మీ మైబైల్ నెంబర్ నమోదు కాలేదు;मोबाइल क्रमांक नोंदणीकृत नाही;மொபைல் எண் பதிவு இல்லை;موبائل نمبر دار نہیں ہے;મોબાઇલ નંબર રજીસ્ટર થયેલ નથી;ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನೋಂದಣಿಯಾಗಿಲ್ಲ;മൊബൈൽ നമ്പർ രജിസ്റ്റർ ചെയ്തിട്ടില്ല;ਮੋਬਾਈਲ ਨੰਬਰ ਦੀ ਰਜਿਸਟਰ ਕੀਤਾ ਹੈ, ਨਾ ਹੈ,;मोबाइल नम्बर दर्ता गरिएको छैन;موبائل نمبر داخل نه آهي'})
        elif result == -3:
            return JsonResponse({'status' : 'err', 'message' : 'Sub-category ID doesnot exist;उप-श्रेणी आईडी doesnot मौजूद;উপ-বিভাগ আইডি doesnot অস্তিত্ব;ఉప వర్గం ID doesnot ఉనికిలో;उप-श्रेणी आयडी doesnot अस्तित्वात;சப்-வகை அடையாள doesnot உள்ளன;ذیلی قسم کی شناخت سے doesnot موجود;પેટા શ્રેણી ને doesnot છે અસ્તિત્વ ધરાવે છે;ಉಪ ವರ್ಗದಲ್ಲಿ ID ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ ಅಸ್ತಿತ್ವದಲ್ಲಿವೆ;ഉപ വിഭാഗം ഐഡി ഉള്ക്കൊള്ളുന്ന നിലവിലില്ല;ਸਬ-ਸ਼੍ਰੇਣੀ ਦਾ ID doesnot ਮੌਜੂਦ;उप-श्रेणी आईडी doesnot अवस्थित;سب درجي جي ID doesnot موجود'})
        else:
            return JsonResponse({'status':'ok', 'quote':result})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def deletequote(request):
    if request.method == 'POST':
        result=0
        try:
            jsonin = json.loads(request.body)
            result = services.deleteQuote(jsonin['quoteId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result ==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
        else:
            return JsonResponse({'status' : 'ok', 'message' : 'Successfully deleted quote;सफलतापूर्वक नष्ट कर बोली;সফলভাবে মোছা উদ্ধৃতি;విజయవంతంగా తొలగించారు కోట్;यशस्वीरित्या हटविले कोट;வெற்றிகரமாக நீக்கப்பட்டது மேற்கோள்;کامیابی سے حذف اقتباس;સફળતાપૂર્વક કાઢી ભાવ;ಯಶಸ್ವಿಯಾಗಿ ಅಳಿಸಲಾಗಿದೆ ಉಲ್ಲೇಖ;ഇല്ലാതാക്കി ഉദ്ധരണി;ਸਫਲਤਾਪੂਰਕ ਹਟਾਇਆ ਹਵਾਲਾ;सफलतापूर्वक हटाइयो उद्धरण;ڪاميابي سان ختم ٿي اقتباس'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def updatequote(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.updateQuote(jsonin)
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result == -1:
            return JsonResponse({'status' : 'err', 'message' : 'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Quotation ID is invalid;कोटेशन आईडी अमान्य है;উদ্ধৃতি আইডি অবৈধ;కొటేషన్ ID చెల్లదు;अवतरण ID अवैध आहे;மேற்கோள் ஐடி தவறானது;کوٹیشن ID غلط ہے;અવતરણ ID ને અમાન્ય છે;ಉದ್ಧರಣ ಐಡಿ ಅಮಾನ್ಯವಾಗಿದೆ;ക്വട്ടേഷൻ ID അസാധുവാണ്;ਕੁਟੇਸ਼ਨ ID ਨੂੰ ਗਲਤ ਹੈ;उद्धरण आईडी अमान्य छ;Quotation ڏيندو سڃاڻپ غلط آهي'})
        elif result == 0:
            return JsonResponse({'status' : 'ok', 'message' : 'No update performed;कोई अद्यतन प्रदर्शन;কোন আপডেট সঞ্চালিত;నవీకరణ ప్రదర్శించారు;कोणतेही अद्यतन सादर;இல்லை மேம்படுத்தல் செய்யப்படுகிறது;کوئی اپ ڈیٹ کارکردگی;કોઈ સુધારો કરવામાં;ಯಾವುದೇ ಅಪ್ಡೇಟ್ ಪ್ರದರ್ಶನ;അപ്ഡേറ്റ് ഒന്നും നിർവഹിച്ച;ਕੋਈ ਅੱਪਡੇਟ ਕੀਤੀ;कुनै अद्यावधिक प्रदर्शन;ڪو ڪاري پرفارم ڪيو'})
        else:
            return JsonResponse({'status' : 'ok', 'message' : 'Updated data successfully;अद्यतन डेटा को सफलतापूर्वक;আপডেট করা হয়েছে ডেটা সফলভাবে;Updated డేటా విజయవంతంగా;अद्यतनित डेटा यशस्वीरित्या;வெற்றிகரமாக புதுப்பிக்கப்பட்டது தரவு;کامیابی سے حالیہ اعداد و شمار کے;અપડેટ માહિતી સફળતાપૂર્વક;ಯಶಸ್ವಿಯಾಗಿ ಸೇರಿಸಿದ ಅಂಕಿಅಂಶಗಳನ್ನು;അപ്ഡേറ്റ് ഡാറ്റ വിജയകരമായി;ਅੱਪਡੇਟ ਕੀਤਾ ਡਾਟਾ ਨੂੰ ਸਫਲਤਾਪੂਰਕ;अद्यावधिक डाटा सफलतापूर्वक;اپڊيٽ ڊيٽا ڪاميابي'})
    else:
        return JsonResponse({'status':'err', 'message': 'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def searchquotes(request):
    if request.method == 'POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.searchQuotes(jsonin['phone'],jsonin['subcategoryId'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result == 0:
            return JsonResponse({'status':'err','message':'Server encountered problem;सर्वर का सामना करना पड़ा समस्या;সার্ভার সম্মুখীন সমস্যা;సర్వర్ ఎదుర్కొన్న సమస్య;सर्व्हर आली समस्या;சர்வர் எதிர்கொண்ட சிக்கல்;سرور کا سامنا ہوا مسئلہ;સર્વર આવી સમસ્યા;ಸರ್ವರ್ ಎದುರಿಸಿದೆ ಸಮಸ್ಯೆ;സെർവർ നേരിട്ട പ്രശ്നം;ਸਰਵਰ ਆਈ ਸਮੱਸਿਆ ਨੂੰ;सामना समस्या सर्भर;سرور پيو مسئلو'})
        else:
            return JsonResponse({'status':'ok','results':result})
    else:
        return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})

def getallquotesbyuser(request):
    if request.method=='POST':
        result = 0
        try:
            jsonin = json.loads(request.body)
            result = services.getallQuotesbyUser(jsonin['phone'])
        except Exception:
            return JsonResponse({'status':'err','message':'Data given to server is invalid;सर्वर के लिए दिए गए डेटा अमान्य है;সার্ভার দেওয়া তথ্য অবৈধ;సర్వర్ ఇచ్చిన డేటా చెల్లదు;सर्व्हर देण्यात डेटा अवैध आहे;சர்வர் கொடுக்கப்பட்ட தரவு தவறானது;سرور کو دیا ڈیٹا غلط ہے;સર્વર આપવામાં ડેટા અમાન્ય છે;ಸರ್ವರ್ ನೀಡಿದ ಡೇಟಾ ಅಮಾನ್ಯವಾಗಿದೆ;സെർവറിലേക്ക് തന്നിരിക്കുന്ന ഡാറ്റ അസാധുവാണ്;ਸਰਵਰ ਨੂੰ ਦਿੱਤੇ ਡਾਟਾ ਗਲਤ ਹੈ;सर्भर दिइएको डाटा अमान्य छ;سرور کي ڏنو ڊيٽا غلط آهي'})
        if result==-1:
            return JsonResponse({'status' : 'err', 'message' : 'Phone number is invalid;फ़ोन नंबर अमान्य है;ফোন নম্বর অবৈধ;ఫోన్ నంబర్ చెల్లదు;फोन नंबर अवैध आहे;தொலைபேசி எண் தவறானது;فون نمبر غلط ہے;ફોન નંબર અમાન્ય છે;ಫೋನ್ ಸಂಖ್ಯೆ ಅಮಾನ್ಯವಾಗಿದೆ;ഫോൺ നമ്പർ അസാധുവാണ്;ਫੋਨ ਨੰਬਰ ਗਲਤ ਹੈ;फोन नम्बर अवैध छ;فون نمبر غلط آهي'})
        elif result == -2:
            return JsonResponse({'status' : 'err', 'message' : 'Mobile number is not registered;मोबाइल नंबर पंजीकृत नहीं है;মোবাইল নম্বর নিবন্ধিত না হয়;మీ మైబైల్ నెంబర్ నమోదు కాలేదు;मोबाइल क्रमांक नोंदणीकृत नाही;மொபைல் எண் பதிவு இல்லை;موبائل نمبر دار نہیں ہے;મોબાઇલ નંબર રજીસ્ટર થયેલ નથી;ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನೋಂದಣಿಯಾಗಿಲ್ಲ;മൊബൈൽ നമ്പർ രജിസ്റ്റർ ചെയ്തിട്ടില്ല;ਮੋਬਾਈਲ ਨੰਬਰ ਦੀ ਰਜਿਸਟਰ ਕੀਤਾ ਹੈ, ਨਾ ਹੈ,;मोबाइल नम्बर दर्ता गरिएको छैन;موبائل نمبر داخل نه آهي'})
        elif result == -3:
            return JsonResponse({'status' : 'err', 'message' : 'Sub-category ID doesnot exist;उप-श्रेणी आईडी doesnot मौजूद;উপ-বিভাগ আইডি doesnot অস্তিত্ব;ఉప వర్గం ID doesnot ఉనికిలో;उप-श्रेणी आयडी doesnot अस्तित्वात;சப்-வகை அடையாள doesnot உள்ளன;ذیلی قسم کی شناخت سے doesnot موجود;પેટા શ્રેણી ને doesnot છે અસ્તિત્વ ધરાવે છે;ಉಪ ವರ್ಗದಲ್ಲಿ ID ಸಂಗ್ರಹಿಸುವುದಿಲ್ಲ ಅಸ್ತಿತ್ವದಲ್ಲಿವೆ;ഉപ വിഭാഗം ഐഡി ഉള്ക്കൊള്ളുന്ന നിലവിലില്ല;ਸਬ-ਸ਼੍ਰੇਣੀ ਦਾ ID doesnot ਮੌਜੂਦ;उप-श्रेणी आईडी doesnot अवस्थित;سب درجي جي ID doesnot موجود'})
        else:
            return JsonResponse({'status':'ok', 'quote':result})
    else:
        return JsonResponse({'status':'err','message':'Bad Request;खराब अनुरोध;খারাপ অনুরোধ;తప్పుడు విన్నపం;खराब विनंती;தவறான கோரிக்கை;غلط فرمائش;ખરાબ વિનંતી;ಕೆಟ್ಟ ವಿನಂತಿ;മോശം അഭ്യർത്ഥന;ਬੁਰੀ ਗੁਜਾਰਸ਼;खराब अनुरोध;غلط درخواست'})


        
            
