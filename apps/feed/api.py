import json
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.notification.utilities import create_notification

from .models import Ting, Like


@login_required
def api_add_ting(request):
    data = json.loads(request.body)
    body = data['body']
    ting = Ting.objects.create(body=body, created_by=request.user)
    

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results:
        result = result[1]

        print(result)

        if User.objects.filter(username=result).exists() and result != request.user.username:
            create_notification(request, User.objects.get(username=result), 'mention')
    return JsonResponse({'success': True})


@login_required
def api_add_like(request):
    data = json.loads(request.body)
    ting_id = data['ting_id']
    if not Like.objects.filter(ting_id=ting_id).filter(created_by=request.user).exists():
        like = Like.objects.create(ting_id=ting_id, created_by=request.user)
        ting = Ting.objects.get(pk=ting_id)
        create_notification(request, ting.created_by, 'like')
    json_response = {'success': True}

    return JsonResponse(json_response)
