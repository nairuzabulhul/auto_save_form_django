"""django_api11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

from auto import views as auto_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # TODO: These routes should be moved to auto/urls.py and this
    #       module should use include to bring them in.
    url(r'^$', auto_views.wizard_view, name="wizard_view"),
    url(r'^api/wizard/?$', auto_views.wizard_api_view, name="wizard_api_view"),
]
