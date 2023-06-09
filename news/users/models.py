from django.db import models
from django.contrib.auth.models import User
from gamenews.models import Post
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')
    profile_image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='users_pic')
    favourite = models.ManyToManyField(Post)

    def __str__(self) -> str:
        return str(self.user)
        
# Default set profile picture
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)