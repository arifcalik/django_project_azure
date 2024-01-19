from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    #obey the parent signature
    def save(self, *args, **kwargs):
        super().save()

        profile_img = Image.open(self.image.path)
        #filesystem space used
        if profile_img.height > 250 or profile_img.width > 250:
            output_size = (250, 250)
            profile_img.thumbnail(output_size)
            profile_img.save(self.image.path)

    




