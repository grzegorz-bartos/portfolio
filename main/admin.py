from django.contrib import admin
from .models import (ExpertArea, Project, ClientOpinion, Service, Article)


class ExpertAreaAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('position',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(ExpertArea, ExpertAreaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ClientOpinion)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
