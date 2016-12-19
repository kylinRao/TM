#coding=utf-8
from django.contrib import admin
from .models import Todo
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
# Register your models here.
'''
class DemoFilter(SimpleListFilter):

    title = _('userID')
    parameter_name = 'user_name'


    def lookups(self, request,model_admin):
        qs = Todo.objects.filter(user_name=request.user)
        for item in qs:
            yield (item.user_name, _(item.user_name))
        
    def queryset(self, request, queryset):
        return queryset.filter(user_name=request.user)

'''
'''
class DemoFilter(SimpleListFilter):

    title = _('用户ID')
    parameter_name = 'userId'


    def lookups(self, request, model_admin):
        qs = model_admin.queryset(request).filter(user_name=request.GET['id']).values('userId').distinct()
        for item in qs:
            yield (item['userId'], _(item['userId']))
        
    def queryset(self, request, queryset):
        return queryset.filter(user_name=request.GET['userId'])
'''
class TodoAdmin(admin.ModelAdmin):
    list_display =('user_name','remind_time','remind_title','remind_content','remind_close')
    list_filter = ['user_name']
   # list_filter = (Todo__user_name,)
admin.site.register(Todo,TodoAdmin)
