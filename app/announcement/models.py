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

class Announcement(models.Model):
    is_active=models.BooleanField(_('is_active'),default=False)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    title=models.CharField(_('title'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/announcement.png")
