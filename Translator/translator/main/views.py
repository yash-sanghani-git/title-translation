from django.shortcuts import render
from sqlalchemy.orm import Session
from .serializers import LanguageSerializer, TitleSerializer
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils.translation import to_locale
from .models import Profile
import json
from django.conf import settings
from translate import Translator

@api_view(['POST'])
def home(request):
    if request.method == "POST":
        text_serializer = LanguageSerializer(data=request.data)
        if text_serializer.is_valid():   
            textt = request.data.get("title")
            language = request.data.get("language")
            translator= Translator(to_lang=language)
            translation = translator.translate(textt)                
            Qs = Profile.objects.filter(title = textt)   
            if Qs.exists() :
                pref = Qs[0].preferences
                pref[language] = translation
                Qs.update(preferences=pref)
                jsondata = [{"title" : textt,
                            "language" : language,
                            "translation"  : translation}]
                return JsonResponse(jsondata, status=status.HTTP_201_CREATED, safe=False)
            else:
                p = Profile(title=textt, language=language, preferences={settings.LANGUAGE_CODE: textt, to_locale(settings.LANGUAGE_CODE): translation})
                p.save()
                jsondata = [{"title" : textt,
                            "language" : language,
                            "translation" : translation}]
                return JsonResponse(jsondata, status=status.HTTP_201_CREATED,safe=False)        


@api_view(['POST'])
def translator(request):
    if request.method == "POST":
        text_serializer = TitleSerializer(data=request.data)
        if text_serializer.is_valid():   
            textt = request.data.get("title")
            language = settings.LANGUAGES
            # dct = dict((x, y) for x, y in language)
            dict= {}
            all_lang = []
            Qs = Profile.objects.filter(title = textt) 
            if Qs.exists() :
                content = {"message" :"Data Already Available",}
                return Response(content, status=status.HTTP_201_CREATED)
            else:
                for lang in language:
                    translator= Translator(to_lang = lang[0])
                    translation = translator.translate(textt)                
                    dict[lang[0]] = translation
                    all_lang.append(lang[0])
                
                p = Profile(title=textt,language =",".join(all_lang) ,preferences = dict)
                p.save()
            jsondata = [{"title" : textt,
                        "translation" : dict}]
            return JsonResponse(jsondata, status=status.HTTP_201_CREATED,safe=False)