from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Ting

@login_required
def feed(request):
  userids = [request.user.id]

  for tinger in request.user.tingerprofile.follows.all():
    userids.append(tinger.user.id)

  tings = Ting.objects.filter(created_by_id__in=userids)

  return render(request, 'feed/feed.html', {'tings': tings})
