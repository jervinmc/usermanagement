from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Announcement(models.Model):
    is_active=models.BooleanField(_('is_active'),default=False)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
