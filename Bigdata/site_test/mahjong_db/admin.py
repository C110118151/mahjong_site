# mahjong_db/admin.py

from django.contrib import admin
from .models import MahjongRecord

@admin.register(MahjongRecord)
class MahjongRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'player', 'amount')
    list_filter = ('player', 'date')
    search_fields = ('player',)
    ordering = ('-date',)
