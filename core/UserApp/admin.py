from django.contrib import admin

from UserApp.models import Player, Boost, PlayerBoost, PlayerLevel, Level, Prize, LevelPrize

admin.site.register(Player)
admin.site.register(Boost)
admin.site.register(PlayerBoost)
admin.site.register(Level)
admin.site.register(Prize)
admin.site.register(PlayerLevel)
admin.site.register(LevelPrize)
