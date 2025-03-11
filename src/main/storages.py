from django.conf import settings
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage


class PublicS3Storage(S3Boto3Storage):
    """Storage class for public S3 files."""

    pass


def get_storage():
    """Returns the appropriate storage backend based on DEBUG setting."""
    return default_storage if settings.DEBUG else PublicS3Storage()
