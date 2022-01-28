from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Comments(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    comments=models.CharField(_('title'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    discussion_id=models.CharField(_('discussion_id'),max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-id"]
