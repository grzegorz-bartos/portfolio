from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)
    short_description = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(
        upload_to='project_images',
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    client = models.CharField(max_length=100, blank=True, null=True)
    services = models.ManyToManyField('Service', blank=True)
    website = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(
        upload_to='project_images/additional_images',
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return f"Image for {self.project.title}"
