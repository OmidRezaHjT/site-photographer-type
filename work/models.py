from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Work(models.Model):
    image = models.ImageField(upload_to='work', blank=False)
    camera = models.CharField(max_length=255)
    album = models.ManyToManyField(Album)
    title = models.CharField(max_length=255)
    publish_date= models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
       return self.title