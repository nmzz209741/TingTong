from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TingerProfileForm

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

@login_required
def edit_profile(request):
  if request.method == 'POST':
    form = TingerProfileForm(request.POST, request.FILES, instance=request.user.tingerprofile)
    if form.is_valid():
      form.save()
      return redirect('tingerprofile', username = request.user.username)
  else:
    form = TingerProfileForm(instance=request.user.tingerprofile)
  context = {
    'user': request.user,
    'form': form,
  }
  return render(request, 'tingerprofile/edit_profile.html', context)