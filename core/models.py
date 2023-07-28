from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    Group,
    User
)
import uuid


# Create your models here.
class BaseModel(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_modifiedby",
        null=True,
        blank=True,
    )
    trash = models.BooleanField(default=False)

    class Meta:
        abstract = True
