from django.db import models

# Create your models here.

class AI_Images(models.Model):
    id= models.AutoField(primary_key=True)
    desc= models.CharField(max_length=200)
    ai_image= models.ImageField(max_length=200, upload_to= 'media/')

    def __str__(self):
        return str(self.desc)

