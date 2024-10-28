from django.contrib import admin
from .models import (
    ExpertArea,
    Project,
    ProjectImage,
    ClientOpinion,
    Service,
    Article,
    Certificate
)


class ExpertAreaAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProjectImageInline]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(ExpertArea, ExpertAreaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ClientOpinion)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Certificate, CertificateAdmin)
