from django.db import models

class WorkExperience(models.Model):
    position = models.CharField(max_length=10,)
    company_name = models.CharField(max_length=20,)

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"