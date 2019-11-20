"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic.base import TemplateView
from acctz import views as core_views
from shop import views as shop_views
from users import views as users_views

urlpatterns = [
    path('', shop_views.items),
    path('acct/', include('allauth.urls')),
    path('project/', include('shop.urls')),
    path('chat/', include('chatroom.urls')),
    path('forum/', include('forum.urls')),
    path('classifiers/', include('pickleclassifier.urls')),
    path('programming-projects/<str:langu>/', shop_views.search_by_lang),
    path('user/', users_views.user_page),
    path('user/<str:un>/', core_views.user_profile),
    path('edit-profile/', users_views.edit_prof),
    path('admin/', admin.site.urls),
    path('403.shtml/', core_views.hacked),
]
