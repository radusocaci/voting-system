from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    cnp = models.CharField(max_length=13, default=settings.GLOBAL_SETTINGS.get('default_value'))
    id_series = models.CharField(max_length=2, default=settings.GLOBAL_SETTINGS.get('default_value'))
    id_number = models.CharField(max_length=6, default=settings.GLOBAL_SETTINGS.get('default_value'))
    issued_by = models.CharField(max_length=20, default=settings.GLOBAL_SETTINGS.get('default_value'))
    address_1 = models.CharField(max_length=100, default=settings.GLOBAL_SETTINGS.get('default_value'))
    address_2 = models.CharField(max_length=100, default=settings.GLOBAL_SETTINGS.get('default_value'))
    city = models.CharField(max_length=20, default=settings.GLOBAL_SETTINGS.get('default_value'))
    county = models.CharField(max_length=30, default=settings.GLOBAL_SETTINGS.get('default_value'))
    postal_code = models.CharField(max_length=6, default=settings.GLOBAL_SETTINGS.get('default_value'))

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
