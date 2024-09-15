from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files.base import File


class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    image = models.ImageField(blank=True, upload_to='photos_buy_to_sell/%Y/%m')
    miniature = models.ImageField(blank=True, upload_to='miniature_photos_buy_to_sell/%Y/%m')
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, default='admin')
    phone_number = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        new_image = self.compress_images(self.miniature)
        self.miniature = new_image
        super().save(*args, **kwargs)

    def compress_images(self, miniature):
        img = Image.open(miniature)
        img.thumbnail((275, 257))
        img_io = BytesIO()
        img.save(img_io, img.format)
        new_image = File(img_io, name=miniature.name)
        return new_image

    def __str__(self):
        return self.title