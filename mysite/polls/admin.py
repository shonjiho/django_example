from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    fieldset = (
        (
            'Custom Field',
            {
                'fields': ('question_text', 'pub_date', "photo"),
            }
        ),
    )


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "choice_text",
        "votes",
    )
    
    

