"""tingtong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.tingerprofile.views import tingerprofile, follow_tinger, unfollow_tinger, followers, edit_profile
from apps.feed.api import api_add_ting, api_add_like
from apps.notification.views import notifications
from apps.conversation.views import conversations_list, conversation_detail
from apps.conversation.api import api_add_message
from django.contrib.auth import views

urlpatterns = [
    #
    # Admin
    #
    path('admin/', admin.site.urls),
    #
    #
    #
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    #
    # App Views
    #
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    # 
    path('notifications/', notifications, name='notifications'),

    #
    path('u/<str:username>/', tingerprofile, name='tingerprofile'),
    path('u/<str:username>/follow/', follow_tinger, name='follow_tinger'),
    path('u/<str:username>/unfollow/', unfollow_tinger, name='unfollow_tinger'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    # 
    path('conversations/', conversations_list, name='conversations_list'), 
    path('conversation/<str:user_id>/', conversation_detail, name='conversation_detail'), 

    #
    # API
    #
    path('api/add_message/', api_add_message, name='api_add_message'),
    path('api/add_ting/', api_add_ting, name='api_add_ting'),
    path('api/add_like/', api_add_like, name='api_add_like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
