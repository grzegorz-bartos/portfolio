"""
URL configuration for Showcase project.

The `urlpatterns` list routes URLs to 1 For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the-include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("projects/", views.ProjectsView.as_view(), name="projects"),
    path(
        "projects/<slug:slug>/",
        views.ProjectDetailView.as_view(),
        name="project_details",
    ),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path(
        "blog/article/<int:article_id>/",
        views.BlogArticleView.as_view(),
        name="article",
    ),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path(
        "contact/success/",
        TemplateView.as_view(template_name="contact_success.html"),
        name="contact_success",
    ),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

# if settings.DEBUG and settings.ENVIRONMENT == "development":
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
