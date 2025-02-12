from django.core.validators import FileExtensionValidator
from django.db import models

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