# website_configs/views.py
from django.shortcuts import redirect

def homepage(request):
    return redirect("mahjong_db:home")
