from datetime import date
from django.db import models


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