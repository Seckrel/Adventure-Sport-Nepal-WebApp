from django.contrib import admin
from .models import *


class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer


class FaqAdmin(admin.ModelAdmin):
    model = Faq
    inlines = [QuestionAnswerInline]


admin.site.register(Faq, FaqAdmin)
