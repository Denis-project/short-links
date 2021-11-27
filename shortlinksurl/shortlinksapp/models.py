from django.db import models

class shortlinksapp(models.Model):
    shortId = models.AutoField(primary_key=True)
    OriginalUrl = models.CharField(max_length=1500)
    ShortUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.name
