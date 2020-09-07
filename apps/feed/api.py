import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Ting, Like


@login_required
def api_add_ting(request):
    data = json.loads(request.body)
    body = data['body']
    ting = Ting.objects.create(body=body, created_by=request.user)
    return JsonResponse({'success': True})


@login_required
def api_add_like(request):
    data = json.loads(request.body)
    ting_id = data['ting_id']
    if not Like.objects.filter(ting_id=ting_id).filter(created_by=request.user).exists():
        like = Like.objects.create(ting_id=ting_id, created_by=request.user)

    json_response = {'success': True}

    return JsonResponse(json_response)
