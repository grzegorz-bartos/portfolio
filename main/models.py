from django.db import models
from django.contrib import auth


# models
class ExpertArea(models.Model):
    title = models.CharField(max_length=10,)
    image = models.ImageField(upload_to='expert_area_icons')

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    position = models.CharField(max_length=10,)
    company_name = models.CharField(max_length=20,)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='project_images',
        blank=True, null=True
    )

    def __str__(self):
        return self.title


class ClientOpinion(models.Model):
    name = models.CharField(max_length=12)
    occupation = models.CharField(max_length=20)
    content = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return f"stars: {self.stars}, client: {self.name}"


class Service(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(
        upload_to='service_images',
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    class ArticleCategory(models.TextChoices):
        DEVELOPMENT = "DEVELOPMENT", "Development"
        OTHER = "OTHER", "Other"

    title = models.CharField(max_length=30)
    category = models.CharField(
        max_length=20,
        choices=ArticleCategory.choices
    )
    read_length = models.IntegerField()
    publication_date = models.DateField(
        verbose_name="Date when the article was published."
    )
    image = models.FileField(
        upload_to='article_images',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
