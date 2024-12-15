from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid 

class ApplicationUser(AbstractUser):
    api_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    