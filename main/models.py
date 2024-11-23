from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.utils.text import slugify


# models
class Profile(models.Model):
    name = models.CharField(max_length=100)
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

    @property
    def years_of_experience(self):
        return date.today().year - 2021


class ExpertArea(models.Model):
    title = models.CharField(max_length=10,)
    image = models.ImageField(
        upload_to='expert_area_icons',
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Expert Area"
        verbose_name_plural = "Expert Areas"


class WorkExperience(models.Model):
    position = models.CharField(max_length=10,)
    company_name = models.CharField(max_length=20,)

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"


class Certificate(models.Model):
    SOURCE_CHOICES = [
        ('Udemy', 'Udemy'),
        ('Other', 'Other (Specify)'),
    ]

    title = models.CharField(max_length=30)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default='Other')
    source_custom = models.CharField(max_length=30, blank=True, null=True, help_text="Specify if Other")
    date_issued = models.DateField(blank=True, null=True)
    icon = models.FileField(
        upload_to='certification_icons/',
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'svg'])]
    )
    url = models.URLField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.source != 'other':
            self.source_custom = ''
        super().save(*args, **kwargs)

    def __str__(self):
        source_display = self.source_custom if self.source == 'other' and self.source_custom else self.get_source_display()
        return f"{self.title} from {self.get_source_display()}"

    class Meta:
        ordering = ['-date_issued']
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"


class Project(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
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


class ClientOpinion(models.Model):
    name = models.CharField(max_length=12)
    occupation = models.CharField(max_length=20)
    content = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"stars: {self.stars}, client: {self.name}"

    @property
    def stars_range(self):
        """Returns a range object for the number of stars."""
        return range(self.stars)

    class Meta:
        verbose_name = "Client Opinion"
        verbose_name_plural = "Client Opinions"


class Service(models.Model):
    name = models.CharField(max_length=20)
    #fa_class = models.CharField(max_length=30, blank=True, null=True)
    image = models.FileField(
        upload_to='service_images',
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'svg'])]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


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
        blank=True, null=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )

    content = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True, help_text="Comma-separated list of tags")
    views = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.title

    def get_tags(self):
        """Return tags as a list of strings."""
        return self.tags.split(",") if self.tags else []

    class Meta:
        ordering = ['-publication_date']  # Order articles by publication date (newest first)
        verbose_name = "Article"
        verbose_name_plural = "Articles"
