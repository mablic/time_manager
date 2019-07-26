from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.db import models
from tinymce.widgets import TinyMCE


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)