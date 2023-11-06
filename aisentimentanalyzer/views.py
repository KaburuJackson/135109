from django.shortcuts import render

from .apps import AisentimentanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.

class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            #get from request
            text = request.GET.get('text')

            #vectorize text 
            vector = AisentimentanalyzerConfig.vectorizer.transform([text])

            #predict based on vectorizer 
            prediction = AisentimentanalyzerConfig.model.predict(vector)[0]

            #build response 
            response = {'text_sentiment' : prediction}

            return JsonResponse(response)