from django.db import models

# Create your models here.


class User(models.Model):
    """Модель юзера"""

    email = models.EmailField()
    name = models.CharField(max_length=124)
    surname = models.CharField(max_length=124)
    avatar = models.ImageField()
    phone = models.PhoneNumberField(_("phone"))
    github_url = models.URLField(blank=True)
    about = models.TextField(max_length=256, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
