from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def tingerprofile(request, username):
  user=get_object_or_404(User, username=username)

  context = {
    'user': user
  }

  return render(request, 'tingerprofile/tingerprofile.html', context)
   


