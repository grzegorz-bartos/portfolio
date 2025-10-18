from django.core.validators import FileExtensionValidator
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from main.storages import get_storage


class Article(models.Model):
    class ArticleCategory(models.TextChoices):
        DEVELOPMENT = "Development"
        OTHER = "Other"

    title = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=ArticleCategory.choices)
    read_length = models.IntegerField()
    publication_date = models.DateField(
        verbose_name="Date when the article was published."
    )
    image = models.FileField(
        storage=get_storage(),
        upload_to="article_images",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
    )

    content = CKEditor5Field(blank=True, null=True)
    tags = models.CharField(
        max_length=100, blank=True, null=True, help_text="Comma-separated list of tags"
    )
    views = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title

    def get_tags(self):
        """Return tags as a list of strings."""
        return self.tags.split(",") if self.tags else []

    class Meta:
        ordering = [
            "-publication_date"
        ]  # Order articles by publication date (newest first)
        verbose_name = "Article"
        verbose_name_plural = "Articles"
