
from django.contrib import admin

from .models import XQuestion, XChoice

class XQuestionAdmin( admin.ModelAdmin ):
    fields = [ "question_text" ]

class XChoiceAdmin( admin.ModelAdmin ):
    fieldsets = [
        (
            "General", { "fields": ["choice_text"] }
        )
    ]

admin.site.register( XQuestion, XQuestionAdmin )
admin.site.register( XChoice, XChoiceAdmin )
