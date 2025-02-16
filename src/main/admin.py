from django.contrib import admin

from .models import (
    Article,
    Certificate,
    ClientOpinion,
    ContactMessage,
    ExpertArea,
    Profile,
    Project,
    ProjectImage,
    Service,
    WorkExperience,
)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company_name")
    search_fields = ("position", "company_name")


class ClientOpinionAdmin(admin.ModelAdmin):
    list_display = ("name", "occupation", "stars")
    search_fields = ("name", "occupation")
    list_filter = ("stars",)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    readonly_fields = ("name", "email", "message", "created_at")


class ExpertAreaAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "date_issued")
    search_fields = ("title", "source")
    list_filter = ("source", "date_issued")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "publication_date")
    search_fields = ("title", "category")
    list_filter = ("publication_date", "category")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "website")
    search_fields = ("title", "client")
    list_filter = ("services",)
    inlines = [ProjectImageInline]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "availability", "client_count", "projects_completed")
    search_fields = ("name", "github", "linkedin")


admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(ClientOpinion, ClientOpinionAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ExpertArea, ExpertAreaAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
