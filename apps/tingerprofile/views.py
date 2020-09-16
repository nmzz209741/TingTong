from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TingerProfileForm

def tingerprofile(request, username):
    user = get_object_or_404(User, username=username)
    tings = user.tings.all()
    for ting in tings:
      likes = ting.likes.filter(created_by_id=request.user.id)

      if likes.count() > 0:
        ting.liked = True
      else:
        ting.liked=False
 
    context = {
        'user': user,
        'tings': tings
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