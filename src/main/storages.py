from django.conf import settings
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage


class MediaS3Storage(S3Boto3Storage):
    """Storage class for media files in S3."""

    location = "media"
    default_acl = "public-read"


def get_storage():
    """Returns the appropriate storage backend based on DEBUG setting."""
    return default_storage if settings.DEBUG else MediaS3Storage()
