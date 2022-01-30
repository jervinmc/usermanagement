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


class Events(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    event_name=models.CharField(_('event_name'),max_length=255,blank=True,null=True)
    event_start_date=models.DateTimeField(_('event_start_date'),blank=True,null=True)
    event_end_date=models.DateTimeField(_('event_end_date'),blank=True,null=True)
    venue=models.CharField(_('venue'),max_length=255,blank=True,null=True)
    event_type=models.CharField(_('event_type'),max_length=255,blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    no_going=models.CharField(_('no_going'),max_length=255,blank=True,null=True)
    no_interested=models.CharField(_('no_interested'),max_length=255,blank=True,null=True)
    is_approved=models.BooleanField(_('is_approved'),default=False)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/events_placeholder.png")

    class Meta:
        ordering = ["-id"]