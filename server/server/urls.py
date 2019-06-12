"""coding:utf-8"""

"""server URL Configuration

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
import os
import json
import random

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    """IndexPageView"""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)

        fpath = os.path.join(settings.STATIC_ROOT, 'menulist.json')

        with open(fpath, 'r') as out:
            context['menu_list'] = json.load(out)

        fpath = os.path.join(settings.STATIC_ROOT, 'datalist.json')
        with open(fpath, 'r') as out:
            context['data_list'] = json.load(out)

        context['randstr'] = random.randint(0, 10)
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view())
]
