# mahjong_db/views.py
from django.shortcuts import render, redirect
from .models import MahjongRecord
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime

def home(request):
    records = MahjongRecord.objects.all().order_by('date', 'player')
    players = MahjongRecord.objects.values_list('player', flat=True).distinct()
    player_totals = {player: MahjongRecord.objects.filter(player=player).aggregate(Sum('amount'))['amount__sum'] or 0 for player in players}
    return render(request, 'mahjong_db/home.html', {
        'records': records,
        'players': players,
        'player_totals': player_totals,
    })

@csrf_exempt
def add_record(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date_str = data.get('date')
        player = data.get('player')
        amount = data.get('amount')
        try:
            MahjongRecord.objects.create(
                date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                player=player,
                amount=int(amount)
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
