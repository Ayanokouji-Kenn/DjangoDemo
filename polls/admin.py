from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #默认出现几个选项插槽


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 表明choice对象在Question页进行编辑
    inlines = [ChoiceInline]

    #  修改列表页显示的字段  默认是只显示str()
    list_display = ('question_text','pub_date','was_published_recently')
    #  增加过滤器
    list_filter = ['pub_date']
    #  增加搜索框
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
