from django.contrib import admin
from django.contrib import admin
from .models import Tournament, Team, Player, Registration

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Registration)

