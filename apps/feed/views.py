from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Ting

@login_required
def feed(request):
  userids = [request.user.id]

  for tinger in request.user.tingerprofile.follows.all():
    userids.append(tinger.user.id)

  tings = Ting.objects.filter(created_by_id__in=userids)

  return render(request, 'feed/feed.html', {'tings': tings})


@login_required
def search(request):
  query = request.GET.get('query', '')

  if len(query)>0:
    tingers = User.objects.filter(username__icontains=query)
  else:
    tingers = []

  context = {
    'query': query,
    'tingers': tingers,
  }

  return render(request, 'feed/search.html', context)