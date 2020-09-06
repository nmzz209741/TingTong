from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def tingerprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }

    return render(request, 'tingerprofile/tingerprofile.html', context)


@login_required
def follow_tinger(request, username):
    user = get_object_or_404(User, username=username)
    request.user.tingerprofile.follows.add(user.tingerprofile)

    return redirect('tingerprofile', username=username)

@login_required
def unfollow_tinger(request, username):
  user = get_object_or_404(User, username=username)
  request.user.tingerprofile.follows.remove(user.tingerprofile)

  return redirect('tingerprofile', username=username)

def followers(request, username):
  user = get_object_or_404(User, username=username)
  return render(request, 'tingerprofile/followers.html', {'user': user})