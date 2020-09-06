import json 

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Ting

@login_required

def api_add_ting(request):
  data = json.loads(request.body)
  body = data['body']

  ting = Ting.objects.create(body=body, created_by=request.user)
  return JsonResponse({'success': True})