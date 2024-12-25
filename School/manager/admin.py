from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'homework', 'deadline', 'created_at', 'update_at', 'course')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


admin.site.register(Course, CourseAdmin)
admin.site.register(Lessons, LessonAdmin)
