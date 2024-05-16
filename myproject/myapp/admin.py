from django.contrib import admin
from .models import Team, Player, Tournament, Article

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Article)
