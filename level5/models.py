from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # create additional attribute
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='picture',blank=True)
    

    def __str__(self):
        return self.user.username