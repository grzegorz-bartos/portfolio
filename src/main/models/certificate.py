from django.core.validators import FileExtensionValidator
from django.db import models

from main.storages import get_storage


class Certificate(models.Model):
    SOURCE_CHOICES = [
        ("Udemy", "Udemy"),
        ("LinkedIn", "LinkedIn"),
        ("Other", "Other (Specify)"),
    ]

    title = models.CharField(max_length=30)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default="Other")
    source_custom = models.CharField(
        max_length=30, blank=True, null=True, help_text="Specify if Other"
    )
    date_issued = models.DateField(blank=True, null=True)
    icon = models.FileField(
        storage=get_storage(),
        upload_to="media/certification_icons",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "svg"])],
    )
    url = models.URLField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.source != "Other":
            self.source_custom = ""
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} from {self.get_source_display()}"

    class Meta:
        ordering = ["-date_issued"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
