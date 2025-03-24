from django.core.validators import FileExtensionValidator
from django.db import models

from main.storages import get_storage


class ExpertArea(models.Model):
    title = models.CharField(
        max_length=10,
    )
    image = models.ImageField(
        storage=get_storage(),
        upload_to="media/expert_area_icons",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Expert Area"
        verbose_name_plural = "Expert Areas"
