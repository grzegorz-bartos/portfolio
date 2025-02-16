from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
