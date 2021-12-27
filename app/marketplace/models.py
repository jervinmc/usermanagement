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


class Marketplace(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    user_email=models.CharField(_('user_email'),max_length=255,blank=True,null=True)
    name=models.CharField(_('name'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    price=models.DecimalField(_('price'),blank=True,decimal_places=6,max_digits=20)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/marketplace_placeholder.png")

