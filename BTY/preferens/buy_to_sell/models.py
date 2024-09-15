from django.db import models

from io import BytesIO
from PIL import Image
from django.core.files.base import File
from pathlib import Path


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
        print(f'pathhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh {self.miniature}')
        new_image = self.compress_images(self.miniature)
        self.miniature = new_image
        super().save(*args, **kwargs)

    def compress_images(self, miniature):
        print(f'miniat: {miniature}')
        img = Image.open(miniature)#.convert('RGB')
        img.thumbnail((275, 257))




        img_io = BytesIO()
        print(f'img_io: {img_io}')
        img.save(img_io, img.format)
        print(f'pathhhhhhhhhhhhhhhh miniat_iiiiiiiiiiiiiiiimg: {miniature}')
        print(f'miniat_typeeeeeeeeeee:' + str(type(miniature)))
        new_image = File(img_io, name=miniature.name)

        print(f'new inaaaaaaaaageeeeeeeee_typeeeeeeeeeee:' + str(type(new_image)))
        #print(f'newwwwwwwwwwwwwwwwwwwwwwwwwwwwww img: {new_image}')
        return new_image

#



    def __str__(self):
        return self.title



    #     def save(self, *args, **kwargs):
    #         super().save(*args, **kwargs)
    #
    #     def compress_images(self, miniature):
    #         img = Image.open(miniature)
    #         img.thumbnail((275, 257))
    #         img_io = BytesIO()
    #         img.save(img_io, optimize=True)
    #         new_image = File(img_io, name=miniature.name)
    #         return new_image




    #
    # def save(self, *args, **kwargs):
    #     new_image = self.compress_images(self.image)
    #     self.miniature = new_image
    #     super().save(*args, **kwargs)
