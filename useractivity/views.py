import json
from django.http import JsonResponse

def se(request):

   with open('user.json') as f:
      data = json.load(f)
      print (data)

   return JsonResponse(data)