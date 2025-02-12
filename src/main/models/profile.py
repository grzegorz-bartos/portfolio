from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    github = models.URLField()
    linkedin = models.URLField()
    discord = models.URLField()
    client_count = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    start_year = models.PositiveIntegerField(default=2021)

    def __str__(self):
        return self.name