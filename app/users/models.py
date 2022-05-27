from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.utils import timezone
from .managers import CustomUserManager
import uuid

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    MALE='Male'
    USERNAME_FIELD = 'email'
    FEMALE='Female'
    GENDER=[(MALE, "Male"),(FEMALE, "Female")]
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site.'),blank=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    ),blank=True)
    date_joined = models.DateTimeField(
        _('date_joined'), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True,blank=True)
    name=models.CharField(_('name'),max_length=255,blank=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True)
    address=models.CharField(_('address'),max_length=255,blank=True)
    password=models.CharField(_('password'),max_length=255,blank=True)
    email=models.CharField(_('email'),max_length=255,blank=True,unique=True)
    is_active=models.BooleanField(_('is_active'),default=True)
    is_verified=models.BooleanField(_('is_verified'),default=True)
    account_type=models.CharField(_('account_type'),max_length=255,blank=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    objects = CustomUserManager()
    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        ordering = ["-id"]
