from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):#use tabular Inline to conserve space
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [ (None,        {'fields': ['question_text']}),
                  ('Date information', {'fields': ['pub_date']}),
                  ]
    inlines = [ChoiceInline]
    #First element of the Field Set is the TITLE 

admin.site.register(Question, QuestionAdmin)
# Register your models here.
