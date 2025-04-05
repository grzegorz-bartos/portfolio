from django.core.validators import FileExtensionValidator
from django.db import models

from main.storages import get_storage


class Profile(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    github = models.URLField()
    linkedin = models.URLField()
    discord = models.URLField()
    client_count = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    start_year = models.PositiveIntegerField(default=2021)

    image = models.ImageField(
        storage=get_storage(),
        upload_to="media/profile_images",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
    )

    resume = models.FileField(
        storage=get_storage(),
        upload_to="media/pdfs",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["pdf"])],
    )

    def __str__(self):
        return self.name
