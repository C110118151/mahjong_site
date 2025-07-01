"""
URL configuration for website_configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website_configs import views  # ← 加上這行

from mahjong_db import views as mahjong_views  # 改用 mahjong 的 view

urlpatterns = [
    path("", mahjong_views.home, name="homepage"),  # 設定首頁就是 mahjong 的首頁
    path("mahjong/", include("mahjong_db.urls")),
    path("admin/", admin.site.urls),
]
