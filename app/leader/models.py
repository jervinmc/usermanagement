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


class Leader(models.Model):
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    position=models.CharField(_('position'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["id"]
