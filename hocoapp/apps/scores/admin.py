from django.contrib import admin

from .models import ScoreBoard

# Register your models here.


class ScoreBoardAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScoreBoard, ScoreBoardAdmin)
