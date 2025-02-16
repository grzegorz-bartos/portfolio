from django.core.validators import FileExtensionValidator
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=20)
    # fa_class = models.CharField(max_length=30, blank=True, null=True)
    image = models.FileField(
        upload_to="service_images",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "svg"])],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
