from django.db import models
from datetime import date
from django.contrib import auth


# models
class Profile(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(default=date.today().year - 2021)
    availability = models.BooleanField(default=True)
    github = models.URLField()
    linkedin = models.URLField()
    discord = models.URLField()
    client_count = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically calculate years of experience on save
        self.years_of_experience = date.today().year - 2021
        super().save(*args, **kwargs)


class ExpertArea(models.Model):
    title = models.CharField(max_length=10,)
    image = models.ImageField(upload_to='expert_area_icons')

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    position = models.CharField(max_length=10,)
    company_name = models.CharField(max_length=20,)


class Certificate(models.Model):
    SOURCE_CHOICES = [
        ('Udemy', 'Udemy'),
        ('Other', 'Other (Specify)'),
    ]

    title = models.CharField(max_length=30)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default='other')
    source_custom = models.CharField(max_length=30, blank=True, null=True, help_text="Specify if Other")
    date_issued = models.DateField(blank=True, null=True)
    icon = models.FileField(upload_to='certification_icons/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.source != 'other':
            self.source_custom = ''
        super().save(*args, **kwargs)

    def __str__(self):
        source_display = self.source_custom if self.source == 'other' and self.source_cusom else self.get_source_display()
        return f"{self.title} from {self.get_source_display()}"

    class Meta:
        ordering = ['-date_issued']


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(
        upload_to='project_images',
        blank=True, null=True
    )

    client = models.CharField(max_length=100, blank=True, null=True)
    services = models.ManyToManyField('Service', blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='project_images/additional_images')

    def __str__(self):
        return f"Image for {self.project.title}"


class ClientOpinion(models.Model):
    name = models.CharField(max_length=12)
    occupation = models.CharField(max_length=20)
    content = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return f"stars: {self.stars}, client: {self.name}"


class Service(models.Model):
    name = models.CharField(max_length=20)
    #fa_class = models.CharField(max_length=30, blank=True, null=True)
    image = models.FileField(
        upload_to='service_images',
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    class ArticleCategory(models.TextChoices):
        DEVELOPMENT = "Development"
        OTHER = "Other"

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

    content = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True, help_text="Comma-separated list of tags")
    views = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title

    def get_tags(self):
        """Return tags as a list of strings."""
        return self.tags.split(",") if self.tags else []
